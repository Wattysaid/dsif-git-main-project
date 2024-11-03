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
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing) | [ELVTR Report](#-ELVTR-Data-Science-Main-Project-Report)

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
- **Exploratory Analysis**: Using visualisations to understand trends.
- **Predictive Modelling**: Application of machine learning algorithms for classification tasks.

## 📋 Requirements
[Home - ReadMe Overview](#-lending-club-loan-analysis---elvtr-data-science-course-project) | [Folder Structure](#-repository-structure---dsif-main-project) | [DataFrame Sequence and Processing Overview](#-lending-club-loan-analysis---dataframe-sequence-and-processing-overview) | [Key Lists for Data Processing](#key-lists-for-data-processing) | [ELVTR Report](#-ELVTR-Data-Science-Main-Project-Report)

- Python 3.12.6
- Key libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

Install dependencies with:
```bash
pip install -r requirements.txt
```

