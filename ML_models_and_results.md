# 📊 ELVTR Data Science Main Project Report

## 🧠 Methodology, Approach, and Model Selection Rationale

### Model Selection Process
To predict loan default probability effectively, several classification models were evaluated as baselines, including Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, K-Nearest Neighbors (KNN), and Naive Bayes. Each model was tested on various performance metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC, and Cross-Validation Mean Accuracy, as well as evaluated for potential issues like overfitting and data leakage.

### Baseline Model Performance Summary

1. **Logistic Regression**
   - **Accuracy**: 95.17%
   - **Precision**: 95.68%
   - **Recall**: 98.90%
   - **F1-Score**: 97.26%
   - **ROC-AUC**: 96.30%
   - **Cross-Validation Mean Accuracy**: 95.04%
   - **Confusion Matrix**: Significant false positives, suggesting potential areas for improvement in feature handling.

  ![image](https://github.com/user-attachments/assets/841f6e24-2e42-4708-b484-05d4adbefe86) ![image](https://github.com/user-attachments/assets/e8e4fe41-0521-402f-89d3-b97ce9d6da90)
  [image](https://github.com/user-attachments/assets/a524526d-4950-4d8f-bbc6-e29c062a88a1)

2. **Decision Tree**
   - **Accuracy**: 95.34%
   - **Precision**: 97.60%
   - **Recall**: 97.01%
   - **F1-Score**: 97.31%
   - **ROC-AUC**: 90.70%
   - **Cross-Validation Mean Accuracy**: 95.12%
   - **Confusion Matrix**: High recall but lower ROC-AUC, indicating overfitting on the training data and possible limitations in generalizing to new data.

3. **Random Forest**
   - **Accuracy**: 93.13%
   - **Precision**: 92.76%
   - **Recall**: 99.88%
   - **F1-Score**: 96.19%
   - **ROC-AUC**: 94.29%
   - **Cross-Validation Mean Accuracy**: 92.73%
   - **Confusion Matrix**: Very high recall, showing strength in capturing true positives but also suggesting some overfitting due to lower cross-validation accuracy.

4. **Gradient Boosting**
   - **Accuracy**: 96.07%
   - **Precision**: 95.92%
   - **Recall**: 99.72%
   - **F1-Score**: 97.78%
   - **ROC-AUC**: 97.80%
   - **Cross-Validation Mean Accuracy**: 96.04%
   - **Confusion Matrix**: Strong performance across metrics, providing balanced precision and recall. Potential to serve as a robust baseline for further tuning.

5. **K-Nearest Neighbors (KNN)**
   - **Accuracy**: 87.39%
   - **Precision**: 88.61%
   - **Recall**: 98.07%
   - **F1-Score**: 93.10%
   - **ROC-AUC**: 69.74%
   - **Cross-Validation Mean Accuracy**: 87.17%
   - **Confusion Matrix**: Lower overall accuracy and ROC-AUC, indicating KNN may not be well-suited for this dataset’s scale and complexity.

6. **Naive Bayes**
   - **Accuracy**: 81.24%
   - **Precision**: 89.47%
   - **Recall**: 88.84%
   - **F1-Score**: 89.15%
   - **ROC-AUC**: 74.10%
   - **Cross-Validation Mean Accuracy**: 81.32%
   - **Confusion Matrix**: High recall but lower precision, with a considerable trade-off that might not be viable in a production setting due to high false positives.

## 📝 Model Evaluation and Challenges

### Observations on Model Performance
The **Gradient Boosting** model emerged as the top performer with a balanced F1-Score, high ROC-AUC, and strong cross-validation accuracy, indicating robustness across metrics. Logistic Regression and Decision Tree models also showed competitive performance, but the Decision Tree presented potential overfitting issues, evident from the lower ROC-AUC compared to other metrics.

### Challenges Encountered
1. **Data Leakage**: During feature engineering, care was taken to avoid including features that could directly reveal loan status. However, given the high recall scores in models like Random Forest, there is a risk of subtle data leakage from correlated variables. Addressing this may involve regular feature audits or further cross-validation techniques to assess model generalization.

2. **Overfitting**: The Decision Tree model exhibited classic signs of overfitting, achieving high recall but comparatively lower ROC-AUC. Overfitting can often result from deep trees or excessive reliance on granular splits. To counter this, techniques like pruning or using ensemble methods like Gradient Boosting and Random Forest (with optimized depth) were explored, with Gradient Boosting showing better performance.

3. **Model Complexity**: KNN and Naive Bayes models underperformed, suggesting that simpler models struggle with the dataset’s complexity. High-dimensional data and the nuances of loan risk assessment may require more sophisticated algorithms to capture intricate patterns.

## 🚀 Next Steps
Based on this evaluation, the **Gradient Boosting** model will be further refined and tested as a primary candidate for deployment. Logistic Regression and Random Forest will be retained as simpler alternatives for comparison. Future work will involve hyperparameter tuning for Gradient Boosting, along with feature importance analysis to ensure interpretability and reduce potential data leakage.

The model’s architecture will also consider deployment strategies, emphasizing scalability and robustness to maintain consistency in predictive accuracy.
