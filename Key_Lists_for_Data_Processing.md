# 🔢 Key Lists for Data Processing

## 🔗 Navigation Menu

- 📘 [README](https://github.com/Wattysaid/dsif-git-main-project/blob/main/README.md)
- 📄 [Overview of DataFrame Sequence and Processing](https://github.com/Wattysaid/dsif-git-main-project/blob/main/DataFrame_Sequence_and_Processing_Overview.md)
- 📊 [ELVTR Report](https://github.com/Wattysaid/dsif-git-main-project/blob/main/ELVTR_report.md)
- 🔍 [Feature Selection and Challenges](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Feature_selection_and_challenges.md)
- 📑 [Key Lists for Data Processing](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Key_Lists_for_Data_Processing.md)
- 🤖 [ML Models and Results](https://github.com/Wattysaid/dsif-git-main-project/blob/main/ML_models_and_results.md)
- 🧠 [Neural Network Selection](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Neural_Network_selection.md)
- ⚙️ [Understanding Feature Impact](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Understanding_feature_impact.md)
- 📈 [Visual Analysis](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Visual_Analysis.md)

## Summary

I tried to brak the data down into 3 distinct categories for easier processing and to save time during the EDA. As a result the project utilises boolean, numerical, and categorical lists. Each list—whether for Boolean, numerical, categorical, or newly engineered features—supports a structured approach (I think...) to data preparation, to facilitate the identification of features that require transforming, encoding, and/or scaling.

![image](https://github.com/user-attachments/assets/41be1f7e-1e19-4b90-925b-645a19816601)


## 🔍 `boolean_list` - Boolean Variables
- **Creation and Identification**: The notebook code creates the `boolean_list` by identifying binary or Boolean fields in the dataset. This is achieved by checking for columns with only `True/False` or `1/0` values, ensuring that these variables are correctly recognised.
- **Encoding and Cleaning**: This list is then used to apply uniform transformations, such as encoding Boolean variables as binary integers (if necessary), to prepare them for model input.
- **Final Checks**: The notebook code performs checks to ensure the Boolean list doesn’t contain duplicates or irrelevant columns.

## 🔢 `numerical_list` - Numerical Variables
- **Identification and Selection**: The notebook code creates the `numerical_list` by selecting continuous and discrete numerical fields, such as `loan_amount` and `interest_rates`, from the dataset.
- **Standardisation and Scaling**: The list helps target numerical features for standardisation or normalisation, allowing them to be scaled appropriately before modelling. This step is essential and probably the most tedious of all lists. Given the type of data we used in this assignment there is no need to exclude data (prays to the greek gods).
- **Data Preparation**: The notebook removes datetime columns from the list to avoid unintended conversions, and final checks ensure the numerical list is accurate and without duplicates.

## 📊 `categorical_list` - Categorical Variables
- **Creation and Encoding**: The notebook code creates the `categorical_list` by selecting categorical features, such as `employment_title` and `home_ownership`, which require encoding ore removal.
- **Handling Missing Values**: The list is used to locate and handle missing values, either by imputing or dropping them as necessary. I didn simplify some into small logical groupings but dropped most of the categorical features either at the beginning or towards the end after the VIF, and RFE analysis.
- **Categorical Encoding**: This list is passed through encoding techniques like one-hot encoding (which was a mistake... creating over a data fram of over 3k features) or binary. This transformation converted the non-numeric categorical values into a form suitable for machine learning models. However, I might run the entire notebook using one hot again now that the end to end python code is working as intended.
- **Date Exclusion and Cleaning**: I've excluded datetime fields from this list, ensuring that only true categorical variables remain, and duplicates are checked to maintain data integrity. The intention of the date time conversion was to plot a timeline considering most defaults are across specific years. **Note**: this might be in place by the time you get to review this assignment.

## ✨ `new_features` - Engineered and Derived Features
- **Feature Engineering**: The notebook code cretes the `new_features` list whcih holds all pre-hardship features created during the initial/basic analysis. These features are derived from existing columns and include transformations like extracting years from dates, creating ratios, and aggregating values after the processing of the 3 lists we touched on above.
- **Inclusion in Final Dataset**: The engineered features are added to the main dataset and result in the data frame `df_transformed`
- **Refinement**: The `new_features` list is checked throughout the notebook refined by removing columns that have been transformed or replaced with derived values.
- **Usage in Model Training**: The final set of features, including `new_features`, is split into training and test sets.

