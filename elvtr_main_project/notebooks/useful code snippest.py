# Check if the specified columns are in new_features
columns_to_check = ['term_kn', 'emp_length_kn']
missing_columns = [col for col in columns_to_check if col not in new_features]

# Display results
if not missing_columns:
    print("Both columns are in new_features.")
else:
    print(f"The following columns are missing from new_features: {missing_columns}")

###########################################################################################

# List update
# List of columns to remove
columns_to_remove = ['zip_code', 'emp_title']

# Remove specified columns from new_features if they exist
new_features = [col for col in new_features if col not in columns_to_remove]

###########################################################################################

# Get the set of columns in df_dropped
df_dropped_columns = set(df_dropped.columns)

# Convert new_features to a set for comparison
new_features_set = set(new_features)

# Find columns in new_features that are missing in df_dropped
missing_in_df_dropped = new_features_set - df_dropped_columns

# Find columns in df_dropped that are not in new_features (if relevant)
extra_in_df_dropped = df_dropped_columns - new_features_set

# Print the results
print("Features in new_features missing from df_dropped:", missing_in_df_dropped)
print("Columns in df_dropped not listed in new_features:", extra_in_df_dropped)

###########################################################################################

from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Variables to specify features for each encoding method
features_to_label_encode = ['addr_state','application_type', 'initial_list_status', 'purpose','home_ownership_grouped_kn']  # Columns to apply label encoding
features_to_one_hot_encode = ['grade', 'sub_grade','title','verification_status','hardship_status_kn']  # Columns to apply one-hot encoding

# Function to apply both label encoding and one-hot encoding
def apply_mixed_encoding(df, label_features, one_hot_features):
    df_encoded = df.copy()  # Copy the DataFrame to avoid modifying the original
    
    # Apply Label Encoding to specified features
    le = LabelEncoder()
    for feature in label_features:
        df_encoded[feature] = le.fit_transform(df_encoded[feature])
    
    # Apply One-Hot Encoding to specified features
    df_encoded = pd.get_dummies(df_encoded, columns=one_hot_features)
    
    return df_encoded

# Apply the mixed encoding to the specified features in df_dropped
df_encoded = apply_mixed_encoding(df_dropped, features_to_label_encode, features_to_one_hot_encode)

# Display the transformed DataFrame
df_encoded.head()

#### Run using this ####

# List of features to ignore
ignore_features = [
    'addr_state', 'application_type', 'earliest_cr_line', 'emp_length', 'emp_title', 
    'grade', 'home_ownership', 'initial_list_status', 'int_rate', 'issue_d', 
    'loan_status', 'purpose', 'revol_util', 'sub_grade', 'term', 'title', 
    'verification_status', 'zip_code', 'loan_status_grouped_kn'
]

# Filter each list to exclude the ignored features
filtered_boolean_list = [feature for feature in boolean_list if feature not in ignore_features]
filtered_numerical_list = [feature for feature in numerical_list if feature not in ignore_features]
filtered_categorical_list = [feature for feature in categorical_list if feature not in ignore_features]

# Now pass the filtered lists to the transform_features function
df_transformed = transform_features(df_dropped, filtered_boolean_list, filtered_numerical_list, filtered_categorical_list)

###########################################################################################

print(df_dropped.shape)
print(len(new_features))


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def transform_features(dataframe, bool_features, num_features, cat_features, prefix_suffix='_clean_kn'):
    """
    Transforms features in the dataframe based on their data type and specified feature lists.

    Parameters:
    ----------
    dataframe : pd.DataFrame
        The DataFrame containing the data to be transformed.
    bool_features : list
        A list of column names representing boolean features.
    num_features : list
        A list of column names representing numerical features.
    cat_features : list
        A list of column names representing categorical features.
    prefix_suffix : str
        The suffix to append to the prefix of each column during one-hot encoding.

    Returns:
    --------
    df_transformed : pd.DataFrame
        The DataFrame with transformed features.
    """
    # Copy the original DataFrame to avoid modifying it
    df_transformed = dataframe.copy()
    
    # Process boolean features
    for feature in bool_features:
        if feature in df_transformed.columns:
            print(f"Processing boolean feature: {feature}")
            # Ensure the feature is boolean or convert to boolean
            df_transformed[feature] = df_transformed[feature].astype(bool)
            
            # Convert boolean to integer (0 and 1)
            df_transformed[feature] = df_transformed[feature].astype(int)
            
            # Scale the feature using StandardScaler
            scaler = StandardScaler()
            df_transformed[feature] = scaler.fit_transform(df_transformed[[feature]])
        else:
            print(f"Boolean feature '{feature}' not found in DataFrame. Skipping...")

    # Process numerical features
    for feature in num_features:
        if feature in df_transformed.columns:
            print(f"Processing numerical feature: {feature}")
            # Handle missing values by imputing with 0
            df_transformed[feature] = df_transformed[feature].fillna(0)
            
            # Check for skewness and apply log transformation if necessary
            skewness = df_transformed[feature].skew()
            if skewness > 1 or skewness < -1:
                # Apply log transformation to reduce skewness
                feature_min = df_transformed[feature].min()
                if feature_min <= 0:
                    df_transformed[feature] = np.log1p(df_transformed[feature] - feature_min + 1)
                else:
                    df_transformed[feature] = np.log1p(df_transformed[feature])
            
            # Scale the feature using StandardScaler
            scaler = StandardScaler()
            df_transformed[feature] = scaler.fit_transform(df_transformed[[feature]])
        else:
            print(f"Numerical feature '{feature}' not found in DataFrame. Skipping...")

    # Process categorical features (One-Hot Encoding)
    if cat_features:
        print(f"Processing categorical features: {cat_features}")
        
        # Generate one-hot encoded columns for the specified categorical columns
        dummies = pd.get_dummies(
            df_transformed[cat_features],
            prefix=[f"{col}{prefix_suffix}" for col in cat_features]
        )
        
        # Use pd.concat to concatenate the new dummy columns with the original DataFrame
        df_transformed = pd.concat([df_transformed, dummies], axis=1)
        
        # Drop the original categorical columns from the DataFrame
        df_transformed.drop(columns=cat_features, inplace=True)

    print("Transformation complete")
    return df_transformed
