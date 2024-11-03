# 🔢 Key Lists for Data Processing

[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing) | [ELVTR Report](#-ELVTR-Data-Science-Main-Project-Report)

Throughout the analysis, several key lists are used to organise and manage specific groups of features. These lists help ensure a structured approach to feature transformation, selection, and analysis.

## Summary

The project utilises several organised lists to streamline the handling and transformation of specific feature types within the dataset. Each list—whether for Boolean, numerical, categorical, or newly engineered features—supports a structured approach to data preparation, ensuring that features are transformed, encoded, and scaled as needed. These lists facilitate targeted processing steps, such as encoding Boolean values, scaling numerical data, and handling categorical variables, thereby maintaining data integrity and consistency across modelling phases. This organised structure allows for efficient feature engineering and selection, ultimately enhancing the model's ability to accurately predict loan approval outcomes.

## 🔍 `boolean_list` - Boolean Variables
- **Creation and Identification**: The notebook creates the `boolean_list` by identifying binary or Boolean fields in the dataset. This is achieved by checking for columns with only `True/False` or `1/0` values, ensuring that these variables are correctly recognised.
- **Encoding and Cleaning**: The list is then used to apply uniform transformations, such as encoding Boolean variables as binary integers (if necessary), to prepare them for model input.
- **Date Exclusion**: Any datetime columns are removed from this list, ensuring they don’t interfere with the binary encoding process.
- **Final Checks**: The notebook performs checks to ensure the Boolean list doesn’t contain duplicates or irrelevant columns.

## 🔢 `numerical_list` - Numerical Variables
- **Identification and Selection**: `numerical_list` is created by selecting continuous and discrete numerical fields, such as loan amount and interest rates, from the dataset.
- **Standardisation and Scaling**: The list helps target numerical features for standardisation or normalisation, allowing them to be scaled appropriately before modelling. This step is essential to ensure models that are sensitive to scale (like neural networks) function optimally.
- **Data Preparation**: The notebook removes datetime columns from the list to avoid unintended conversions, and final checks ensure the numerical list is accurate and without duplicates.

## 📊 `categorical_list` - Categorical Variables
- **Creation and Encoding**: The `categorical_list` is created by selecting categorical features, such as `employment_title` and `home_ownership`, which require encoding.
- **Handling Missing Values**: The list is used to locate and handle missing values, either by imputing or dropping them as necessary.
- **Categorical Encoding**: This list is passed through encoding techniques like one-hot encoding or label encoding. This transformation is vital for converting non-numeric categorical values into a form suitable for machine learning models.
- **Date Exclusion and Cleaning**: The notebook excludes datetime fields from this list, ensuring that only true categorical variables remain, and duplicates are checked to maintain data integrity.


## ✨ `new_features` - Engineered and Derived Features
- **Feature Engineering**: `new_features` holds all engineered features created during the analysis. These features are derived from existing columns and may include transformations like extracting years from dates, creating ratios, and aggregating values.
- **Inclusion in Final Dataset**: The engineered features are added to the main dataset for further analysis and modelling, allowing the model to benefit from additional insights.
- **Refinement**: `new_features` is checked throughout the notebook to ensure no irrelevant columns are included. This list is refined by removing original columns that have been transformed or replaced with derived values.
- **Usage in Model Training**: The final set of features, including `new_features`, is split into training and test sets, enabling the model to utilise both raw and engineered variables for enhanced prediction accuracy.

---

These lists provide a structured approach to feature engineering, ensuring each variable type receives the appropriate transformations and treatments. This organisation facilitates efficient data processing, improves model interpretability, and supports more accurate predictive modelling.
