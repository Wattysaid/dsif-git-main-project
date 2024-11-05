![image](https://github.com/user-attachments/assets/b42449a1-a52e-4efb-8343-3688d0b158b0)

#📊 Lending Club Loan Analysis

![image](https://github.com/user-attachments/assets/31891671-e12d-44b6-a156-18d28dbe8672)

This project is part of the ELVTR Data Science course, designed to demonstrate the application of data science skills in a financial context. The primary goal is to analyse and model a dataset of loan applications to predict loan approval statuses.

## 🔗 Outline
- [📊 Lending Club Loan Analysis - ELVTR Data Science Course Project](#-lending-club-loan-analysis---elvtr-data-science-course-project)
- [🎯 Project Objectives](#-project-objectives)
- [🔄 Project Workflow](#-project-workflow)
- [🧠 Key Concepts Demonstrated](#-key-concepts-demonstrated)
- [📋 Requirements](#-requirements)

## 🔗 Page Menu

Use this as a quick reference guide to navigate the project's main documents!

- 📄 [Overview of DataFrame Sequence and Processing](https://github.com/Wattysaid/dsif-git-main-project/blob/main/DataFrame_Sequence_and_Processing_Overview.md)
- 📊 [ELVTR Report](https://github.com/Wattysaid/dsif-git-main-project/blob/main/ELVTR_report.md)
- 🔍 [Feature Selection and Challenges](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Feature_selection_and_challenges.md)
- 📑 [Key Lists for Data Processing](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Key_Lists_for_Data_Processing.md)
- 🤖 [ML Models and Results](https://github.com/Wattysaid/dsif-git-main-project/blob/main/ML_models_and_results.md)
- 🧠 [Neural Network Selection](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Neural_Network_selection.md)
- 📘 [README](https://github.com/Wattysaid/dsif-git-main-project/blob/main/README.md)
- ⚙️ [Understanding Feature Impact](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Understanding_feature_impact.md)
- 📈 [Visual Analysis](https://github.com/Wattysaid/dsif-git-main-project/blob/main/Visual_Analysis.md)


  ---

# 📂 Repository Structure - DSIF Main Project
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing) | [ELVTR Report](#-ELVTR-Data-Science-Main-Project-Report)

Welcome to the DSIF Main Project repository. This structure provides an organised overview of the folders and files within the project. Use the hyperlinks to quickly navigate to specific sections and access the corresponding resources.

## 🔗 Table of Contents
- [📁 Notebooks](https://github.com/Wattysaid/dsif-git-main-project/tree/main/elvtr_main_project/notebooks)
- [📁 Models & Results](https://github.com/Wattysaid/dsif-git-main-project/tree/main/elvtr_main_project/models)
- [📁 Documentation](https://github.com/Wattysaid/dsif-git-main-project/tree/main/elvtr_main_project/docs)
- [📁 Reports](https://github.com/Wattysaid/dsif-git-main-project/tree/main/elvtr_main_project/reports)


![image](https://github.com/user-attachments/assets/5642d472-eb07-43b5-a586-6900a9448795)


## 🎯 Project Objectives
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing) | [ELVTR Report](#-ELVTR-Data-Science-Main-Project-Report)

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
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing) | [ELVTR Report](#-ELVTR-Data-Science-Main-Project-Report)

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
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing) | [ELVTR Report](#-ELVTR-Data-Science-Main-Project-Report)

- **Data Cleaning**: Importance of preprocessing to ensure data quality.
- **Feature Selection**: Methods to retain meaningful variables for modelling.
- **Exploratory Analysis**: Using visualisations to understand the data.
- **Predictive Modelling**: Application of machine learning algorithms for classification tasks.

## 📋 Requirements
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing) | [ELVTR Report](#-ELVTR-Data-Science-Main-Project-Report)

- Python 3.12.6
- Key libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

Install dependencies with:
```bash
pip install -r requirements.txt # updated with all package dependancies 4th Nov. 2024
```

