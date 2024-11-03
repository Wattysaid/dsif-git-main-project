# 📊 Lending Club Loan Analysis - ELVTR Data Science Course Project

This project is part of the ELVTR Data Science course, designed to demonstrate the application of data science skills in a financial context. The primary goal is to analyse and model a dataset of loan applications to predict loan approval statuses.

## 🔗 Outline
- [📊 Lending Club Loan Analysis - ELVTR Data Science Course Project](#-lending-club-loan-analysis---elvtr-data-science-course-project)
- [🎯 Project Objectives](#-project-objectives)
- [🔄 Project Workflow](#-project-workflow)
- [🧠 Key Concepts Demonstrated](#-key-concepts-demonstrated)
- [📋 Requirements](#-requirements)
- [📊 DataFrames and Their Processing Sequence](#-dataframes-and-their-processing-sequence)
- [🔢 Key Lists for Data Processing](#-key-lists-for-data-processing)

  ---

# 📂 Repository Structure - DSIF Main Project
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing)

Welcome to the DSIF Main Project repository. This structure provides an organised overview of the folders and files within the project. Use the hyperlinks to quickly navigate to specific sections and access the corresponding resources.

## 🔗 Table of Contents
- [📁 Notebooks](#notebooks)
- [📁 Models](#models)
- [📁 Data](#data)
- [📁 Results](#results)
- [📁 Documentation](#documentation)
- [📁 Scripts](#scripts)

---

## 🎯 Project Objectives
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing)

1. **Data Cleaning and Preprocessing**: 
   - Handle missing values and inconsistent data types.
   - Remove duplicate entries, standardise, and normalise features.
2. **Feature Engineering and Selection**:
   - Categorise features into logical groups for better interpretability (e.g., credit history, employment information, loan performance).
   - Filter relevant features for modelling.
3. **Exploratory Data Analysis (EDA)**:
   - Perform statistical analysis and visualisation to uncover trends and insights.
4. **Predictive Modelling**:
   - Train and evaluate a predictive model for loan status classification.
   - Implement binary and multi-class classification using techniques like one-vs-one and one-vs-rest strategies.

## 🔄 Project Workflow
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing)

1. **Data Loading**:
   - Load the main loan dataset and data dictionary to understand feature meanings and relationships.

2. **Data Cleaning and Preparation**:
   - Ensure all columns are properly named and cleaned for consistency.
   - Address missing values and inconsistent data types to enhance data quality.
   - Calculate the Variance Inflation Factor (VIF) to detect multicollinearity, removing highly correlated variables that could affect model stability and interpretability.

3. **Exploratory Data Analysis (EDA)**:
   - Visualise data distributions and correlations to uncover patterns, trends, and relationships.
   - Identify key insights into loan performance and borrower profiles, which will guide feature selection and model design.

4. **Feature Engineering and Transformation**:
   - Group features into logical categories, such as `Credit History`, `Employment Information`, and `Loan Performance`, to aid interpretability.
   - Apply categorical encoding to convert categorical variables into numeric format suitable for modelling.
   - Standardise numerical features to ensure consistent scaling across variables, improving model performance for algorithms sensitive to feature scaling.
   - Implement Synthetic Minority Over-sampling Technique (SMOTE) to balance the target variable, addressing class imbalances and improving model robustness.

5. **Modelling**:
   - Split data into training and testing sets for model evaluation.
   - Train various machine learning models, including traditional algorithms and neural networks, to classify loan statuses.
   - Evaluate model performance using chosen metrics. Utilise SHAP (SHapley Additive exPlanations) values to interpret the impact of individual features on predictions, providing transparency and insights into model decisions.

## 🧠 Key Concepts Demonstrated
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing)

- **Data Cleaning**: Importance of preprocessing to ensure data quality.
- **Feature Selection**: Methods to retain meaningful variables for modelling.
- **Exploratory Analysis**: Using visualisations to understand trends.
- **Predictive Modelling**: Application of machine learning algorithms for classification tasks.

## 📋 Requirements
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing)

- Python 3.12.6
- Key libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

# 📊 Lending Club Loan Analysis - DataFrame Sequence and Processing Overview

[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing)

Here we'll explore at a high level the sequence of DataFrames used throughout the analysis and the key transformations applied to each. This high-level overview highlights the logical flow from raw data to final model preparation, showcasing data cleaning, feature engineering, and transformations.

## Summary

This project involves a series of transformations and analyses to prepare the loan data for predictive modelling. Each DataFrame builds on previous steps, ensuring a thorough and logical progression from raw data to fully prepared training and testing sets. These processing steps enable robust feature selection, handling of missing values, encoding, and scaling, laying the groundwork for a reliable model to predict loan approval statuses.

## DataFrames and Their Processing Sequence

### 1. `df` - Raw Loan Data 🗃️
The initial loan data is loaded into the `df` DataFrame. The raw data is cleaned by:
   - Standardising column names to lowercase and replacing spaces with underscores.
   - Handling missing values and inconsistent data types.
   - Removing duplicates to ensure data quality.

### 2. `df_data_dict` - Data Dictionary 📑
The `df_data_dict` DataFrame contains descriptions of each column in the main data. It serves as a reference to interpret variable meanings and structures, helping guide feature categorisation and selection.

### 3. `df_dropped` - Cleaned and Filtered Data 🧼
`df_dropped` is created by applying additional transformations to `df`, including:
   - Dropping unnecessary or highly null columns based on preliminary analysis.
   - Filtering records as needed for consistency with project goals.
   - Converting categorical variables to numerical representations where applicable, in preparation for modelling.

### 4. `df_emp_title` - Employment-Specific Data 💼
`df_emp_title` focuses on employment-related fields within the dataset, particularly useful for analysing employment length and titles. Additional cleaning may be applied, such as removing uncommon job titles or grouping similar roles for better interpretability.

### 5. `df_transformed` - Fully Transformed Data 🔄
The `df_transformed` DataFrame builds on `df_dropped` with a series of transformations to finalise the dataset for exploratory data analysis (EDA) and modelling:
   - Encoding categorical variables.
   - Normalising or scaling numerical features.
   - Creating logical groupings of variables based on the data dictionary, e.g., grouping by credit history, loan performance, or hardship-related features.
   - Extracting or engineering new features from existing ones, such as date-related fields.

### 6. `cross_tab_df` - Cross-Tabulation for Exploratory Analysis 🔍
`cross_tab_df` is used for exploring categorical variables, particularly for understanding distributions and relationships within the data. This DataFrame may also contribute to identifying key predictors of loan performance.

### 7. `defaulted_percentage_df` - Default Rate Analysis 📉
This DataFrame provides a breakdown of loan defaults by category, calculating default percentages across various segments. Insights from this analysis guide feature selection and model target definitions.

### 8. `freq_table` - Frequency Analysis of Categorical Variables 📊
The `freq_table` captures counts and frequencies of categorical values within selected columns. This analysis helps identify dominant categories or balance class distribution, particularly useful for features like loan purpose, home ownership, and employment length.

### 9. `missing_df` and `not_missing_df` - Missing Value Tracking 🕵️‍♀️
These DataFrames track missing values in `df`:
   - `missing_df` lists columns with null values, helping prioritise imputation or removal.
   - `not_missing_df` contains data without missing values, enabling comparisons to check if patterns in missingness impact the target variable.

### 10. `vif_data` - Variance Inflation Factor (VIF) Calculation 📐
`vif_data` is used to assess multicollinearity between features. This DataFrame calculates VIF scores, helping remove highly collinear features that may impact model stability and interpretability.

### 11. `uniqueness_df` - Unique Value Analysis 🔢
`uniqueness_df` provides insights into the number of unique values per column, highlighting fields with high cardinality or dominant categories that may require further processing, such as grouping or binning.

### 12. `X_train` and `X_test` - Training and Testing Sets 🏋️‍♂️
The final modelling datasets are split into `X_train` and `X_test`, with selected features and processed data:
   - `X_train`: Contains the feature set for training the model.
   - `X_test`: Holds the test data to evaluate model performance.
   - These datasets may be scaled and transformed for compatibility with machine learning models.

### 13. `Y` - Target Variable 🎯
The `Y` DataFrame holds the target variable for the model, representing the loan status or grouped loan outcome (e.g., default vs. non-default).

### Additional DataFrames for Analysis 🛠️
Throughout the notebook, various temporary DataFrames may be created for specific tasks such as feature selection (`selected_features`), visualisation, or detailed analysis (`datetime_headers`, `missing_cols`). These are utilised and refined as needed to finalise the data for modelling.

---

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

---

# 📊 ELVTR Data Science Main Project Report

## 🧠 Methodology, Approach, and Model Selection Rationale

This project aims to classify loan applications for Lending Club by analyzing historical data to predict loan repayment likelihood. The approach included these key stages:

1. **Data Cleaning and Preprocessing**: 🧹 Missing values were handled, categorical variables encoded, and numerical variables normalized. Columns with low variance were removed, and outliers adjusted to enhance model performance.
2. **Exploratory Data Analysis (EDA)**: 🔍 Analyzed feature correlations and distributions to gain insights into key factors influencing loan status.
3. **Feature Engineering**: 🛠 New features were derived based on domain knowledge, enriching the dataset to improve predictive accuracy.
4. **Model Selection**: 🎯 Various models, such as Logistic Regression, Decision Trees, and Random Forest, were evaluated. Random Forest was chosen for its balance of accuracy, interpretability, and robustness.

### 🔍 Rationale for Model Selection
Random Forest was selected due to its ability to handle complex relationships and reduce overfitting risks, as it combines the predictions of multiple decision trees.

## ✅ Advantages and ⚠️ Limitations of the Chosen Model

### ✅ Advantages
- **High Accuracy and Robustness**: 💪 Random Forest provides strong predictive power with a lower risk of overfitting.
- **Interpretability**: 🕵️ Feature importance scores allow insights into key factors affecting loan decisions.
- **Versatility**: 🌐 It handles both numerical and categorical data well, with less sensitivity to scaling or normalization.

### ⚠️ Limitations
- **Computational Cost**: 🖥️ Training and inference can be time-consuming, impacting scalability.
- **Complexity in Tuning**: 🔧 Optimal performance requires intensive hyperparameter tuning.
- **Real-Time Suitability**: ⏳ Random Forest may not be ideal for real-time applications without optimizations.

## 🏗️ Architecture of the Final Solution

The final solution consists of a multi-stage pipeline:

1. **Data Ingestion and Preprocessing**: 📥 Data is loaded, cleaned, and preprocessed with feature encoding, standardization, and normalization.
2. **Feature Engineering and Selection**: 🔨 Relevant features are selected and engineered to improve predictive accuracy.
3. **Model Training**: 🎓 The Random Forest classifier is trained with optimized hyperparameters through cross-validation.
4. **Prediction Pipeline**: 🔮 For new data, the model processes inputs and outputs the probability of loan default or approval.
5. **Optional Real-Time Scoring Component**: 🕰️ An API framework for batch scoring, with potential for real-time scoring through API endpoints.

## 🚀 Deployment and Scalability Considerations

For business-as-usual (BAU) use, the following deployment and scalability considerations were made:

- **Batch Prediction Pipeline**: 📦 Designed to handle high volumes efficiently in batch mode.
- **Cloud Hosting and Integration**: ☁️ Deployment options (e.g., AWS or GCP) to leverage scalable cloud resources.
- **Real-Time Extension**: ⏱️ API deployment for real-time scoring, optimized to reduce latency if needed.
- **Model Monitoring and Retraining**: 🔄 Regular monitoring and retraining scheduled to maintain accuracy as data distributions change.

## 📈 Estimated Impact and ROI

The deployment of this model is expected to bring significant benefits:

- **Reduce Loan Default Rates**: 🔒 Accurately identifies high-risk loan applications, reducing defaults and improving portfolio health.
- **Increase Operational Efficiency**: 🏃 Streamlines the decision-making process, reducing time and resources spent on manual evaluations.
- **Enhance Customer Experience**: 😊 Faster approvals for low-risk customers improve satisfaction and retention.
- **Expected ROI**: 💸 Improved loan performance is anticipated to lead to cost savings and reduced manual intervention. The exact ROI depends on improvements in Lending Club’s default rates and operational savings.

