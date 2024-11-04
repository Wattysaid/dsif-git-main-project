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

The aim of this project was to create a loan application scoreing model leveraging predictive modelling for the Lending Club. To do this I analysed a data set of 100k client loans covering Active, In Progress, Defaulted and late loans. This resulted in a trained ML model that predicted with over 87% accuracy.

1. **Data Cleaning and Preprocessing**: Missing values were handled, categorical variables encoded, and numerical variables normalised. Columns with low variance were removed, and outliers adjusted to enhance model performance. This proved to be the most time consuming part of the assignment with a lot of reasearch and additional reading to make the most out of our data.
2. **Exploratory Data Analysis (EDA)**: Here I analysed feature correlations and distributions to gain insights into key factors that could possible predict or influence a postive or negative loan status outcome. Features were filtered following a pre hardship grouping (this was also, very time consuming as the data dictionary didn't always make sense. In a real life scenario I'd reach out to SMEs.). The entire pre hardship feature list was split into three seperate lists for a deeper analysis. This led to several changes i.e. simplifying categorical data into new groupings, removal of data with no variation i.e. unique columns (`id`), etc. I faced several challenges during this phase in particular handling the outliers. Some values were capped, some retained the outliers e.g. `total_pymnt`, some were transformed using square root transformation. I avoided removing any outliers given the nature of the data.
3. **Feature Engineering**: New features were introduced to simplify the collected data. This was completed either via grouping or the combination of multiple data points, this enriched the dataset and improved the ML models predictive accuracy albeit we still have data leakage and overfitted outputs. The main difference between this assignement and the previous one is that the categorical encoding works in this assignement allowing for more accurate results. Nevertheless, our data needs a bit more tuning. I can see that I've removed columns from the second ML run but not from later code as a result we're still running 103 features in SHAP although the RFE selected 23. I did however catch this when running the NN Models and reduced the selection to the RFE selected values.
4. **Model Selection**: I ran various models (out of curiosity and based on the mind maps shared by Adrian), Logistic Regression, Decision Trees, and Random Forest, were all evaluated. Random Forest was chosen for its balance of accuracy, and interpretabiliyt. I shuffled model parameters to determine their impact on the final scores. Balancing accuracty, precision and recall proved to be tricky with initial models scoring above a realistic value i.e. 99%. ***!! The notebook in this GitHub is more recent than the one submitted !!***

### 🔍 Rationale for Model Selection of our baseline model
I decided to proceed with two models (Gradient Boosting and Logistic Regression). Both performed well when ran against our transformed data.

was selected due to its ability to handle complex relationships and reduce overfitting risks, as it combines the predictions of multiple decision trees.

## ✅ Advantages and ⚠️ Limitations of our baseline model 

(a lot of the model comparaison is from O'Reilly books or shamlessly googled)

#### 1. Gradient Boosting

**✅ Advantages**:
   - **High Accuracy**: Gradient Boosting achieves high accuracy and ROC-AUC, suggesting strong overall predictive capability.
   - **Effective at Capturing Defaults**: The model has a high recall (0.9972), meaning it successfully identifies most default cases. Not blind to these results they change later after fine tuning.
   - **Handles Complex Patterns**: Gradient Boosting is effective at learning complex relationships, which can improve prediction performance in cases with intricate data patterns this seemed to be the appropriate choice given the results but also the volume of data I passed through the model.

**⚠️ Limitations**:
   - **Computationally Intensive**: Training Gradient Boosting models can be time-consuming and requires more computational resources, especially on large datasets. (MSFT surface...)
   - **Overfitting**: Our Gradient Boosting is overfit and something we'll fine tune in the second run (e.g., too many trees or too high learning rate).
   - **Less Interpretable**: The model’s complexity can make it challenging to interpret results, which might be a limitation when explaining predictions to stakeholders. (shamlessly googled)

#### 2. Logistic Regression

**✅ Advantages**:
   - **Interpretable**: Logistic Regression is easier to interpret, with coefficients directly indicating feature importance, which can help explain default risk factors. (shamlessly googled)
   - **Computationally Efficient**: Logistic Regression is relatively fast to train and requires fewer resources, making it suitable for large datasets and real-time applications.
   - **High Recall**: The model has a high recall (0.9890), indicating effective identification of defaults and a reliable capture of risk cases.

**⚠️ Limitations**:
   - **Limited to Linear Relationships**: Logistic Regression may struggle with complex patterns if the data relationships are highly nonlinear.
   - **Lower Flexibility**: Compared to models like Gradient Boosting, Logistic Regression is less flexible and may not perform as well on datasets with complex, nonlinear relationships. (shamlessly googled)
   - **Lower Recall and F1-Score than Gradient Boosting**: Although the recall and F1-score are high, they’re slightly lower than Gradient Boosting, meaning it may miss a few more default cases.

### 🔍 Rationale for Model Selection of our baseline model



## 🏗️ Architecture of the Final Solution

The final solution consists of a multi-stage pipeline (I sacrificed the application building to focus on the 40pts project, but might have this in place by the time you guys get to reviewing the assignment):

1. **Data Ingestion and Preprocessing**: Data is loaded, cleaned, and an initial selection list created `new_features`.
2. **Feature Engineering and Selection**: Relevant `new_features`, new features created, removed, and grouped.
3. **Model Training**: The Random Forest (second ML run after SMOTE) classifier is trained with optimized hyperparameters through cross-validation.
4. **Prediction Pipeline**: For new data, the model processes inputs and outputs the probability of loan default or approval.
5. **Optional Real-Time Scoring Component**: An API framework for batch scoring, with potential for real-time scoring through API endpoints.

## 🚀 Deployment and Scalability Considerations

For business-as-usual (BAU) use, I've looked at the deployment and scalability (theory):

- **Batch Prediction Pipeline**: Designed to handle high volumes efficiently in batch mode.
- **Cloud Hosting and Integration**: Deployment options (e.g., AWS or GCP) to leverage scalable cloud resources.
- **Real-Time Extension**: API deployment for real-time scoring, optimized to reduce latency using fastAPI.
- **Model Monitoring and Retraining**: Regular Dashboard monitoring and retraining scheduled to maintain accuracy as data distributions changes

## 📈 Estimated Impact and ROI

The deployment of this model is expected to bring significant benefits:

- **Reduce Loan Default Rates**: 🔒 Accurately identifies high-risk loan applications, reducing defaults and improving portfolio health.
- **Increase Operational Efficiency**: 🏃 Streamlines the decision-making process, reducing time and resources spent on manual evaluations.
- **Enhance Customer Experience**: 😊 Faster approvals for low-risk customers improve satisfaction and retention.
- **Expected ROI**: 💸 Improved loan performance is anticipated to lead to cost savings and reduced manual intervention. The exact ROI depends on improvements in Lending Club’s default rates and operational savings.

## Impact of being wrong (detailed analysis)

### The cost of being wrong

In attempt to understand the cost of error I've used a sample number of 1000 predictions. The question I'm asking myself is the following:

How much is the cost of the time spent researching, execution, and closing false negatives, and false positives?

I'll use Precision and Recall to calculate this. We'll also substitue a few numbers to simulate cost in minutes.

We have the following information:

- **Gradient Boosting:**
    - Precsion (after SMOTE) 0.5523
    - Recall (after SMOTE) 0.4991

- **Random Forest:**
    - Precsion (after SMOTE) 0.6833
    - Recall (after SMOTE) 0.4325

Expected number of defaults = Sum of defaults / Total data set =  12431 / 63689 = 0.1951 * 100 = 20%

Using 1000 applicants or current loans as a base figure.

1000 * 0.20 = 800 estimated non defaults, leaving us with 200 actual defaults estimated.

- **Gradient Boosting:**
    - False Positives = Precsion (after SMOTE) = (1 - 0.5523) * 800 =  358
    - False Negatives = Recall (after SMOTE) = (1 - 0.4991) * 200 = 100
    - Total of incorrect predictions 458

- **Random Forest:**
    - False Positives = Precsion (after SMOTE) = (1 - 0.6833) * 800 =  253
    - False Negatives = Recall (after SMOTE) = (1 - 0.4325) * 200 = 114
    - Total of incorrect predictions 367

The cost of for each approach can be calculated by multiplying our results against the cost of a False Positive, and the cost of a False Negative.

Let's assume the cost of a False Positive (revenue loss maybe denying a loan) equates to 2500, and the cost of a False Negtive (loss from a customer defaulting) equates to 5600.

**Gradient Boosting** = (358 * 2500) + (100 * 5600) = 1,455,000
**Random Forest** = (253 * 2500) + (114 * 5600) = 1,270,900

In the above scenario with these very subjective numbers we'd be best opting for the Random Forest which has a lower cost of being wrong.
