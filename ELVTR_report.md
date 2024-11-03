# 📊 ELVTR Data Science Main Project Report

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

## 🧠 Methodology, Approach, and Model Selection Rationale

The aim of this project was to a loan application predictive model for Lending Club by analysing 100k client loan data to predict loan repayment likelyhood of loan defaults.

The approach included these key stages:

1. **Data Cleaning and Preprocessing**: 🧹 Missing values were handled, categorical variables encoded, and numerical variables normalized. Columns with low variance were removed, and outliers adjusted to enhance model performance.
2. **Exploratory Data Analysis (EDA)**: 🔍 Analyzed feature correlations and distributions to gain insights into key factors influencing loan status. Filtered features and identified meaningful trends.
3. **Feature Engineering**: 🛠 New features were derived either via grouping or the combination of multiple data points, this enriched the dataset and improved the ML models predictive accuracy albeit.
4. **Model Selection**: 🎯 Various models, such as Logistic Regression, Decision Trees, and Random Forest, were evaluated. Random Forest was chosen for its balance of accuracy, interpretability, and robustness.

### 🔍 Rationale for Model Selection
Random Forest was selected due to its ability to handle complex relationships and reduce overfitting risks, as it combines the predictions of multiple decision trees.

## ✅ Advantages and ⚠️ Limitations of the Chosen Model

### ✅ Advantages
- **High Accuracy and Robustness**: 💪 Random Forest provideded strong predictive power with a lower risk of overfitting. Yet we still have some work ahead of us to remove overfitting entirely.
- **Interpretability**: 🕵️ Feature importance scores allow insights into key factors affecting loan decisions.
- **Versatility**: 🌐 It handles both numerical and categorical data well, with less sensitivity to scaling or normalization.

### ⚠️ Limitations
- **Computational Cost**: 🖥️ Training and inference was time consuming, neural networks feature reduction excercises along with SHAP tested my laptop. SHAP was executed with 1000 features only.
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

