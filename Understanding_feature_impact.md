## 🔍 SHAP Value Visualisation and Model Interpretability

To gain deeper insights into how each selected feature contributes to our model’s predictions, I used SHAP (SHapley Additive exPlanations) values. SHAP is a powerful tool for interpreting model outputs by showing the impact of each feature on individual predictions. This helps ensure that the model's decision-making aligns with our objectives and provides transparency in understanding the factors driving loan default predictions.

### 🧩 Understanding Feature Importance

I transformed the data into a NumPy array and used parallel processing to speed up SHAP calculations. Upon reviewing the feature importance values, I observed that there isn’t a single dominant feature driving the model's predictions. Instead, most feature importance scores range between 0.01 and 0.09. This suggests that the model depends on a variety of features, rather than focusing on a small subset, which is ideal for capturing nuanced patterns across different borrower profiles.

### 📊 SHAP Analysis and Visualisation

After training the model, I generated SHAP values to visualise how each feature pushes the prediction up or down. Here’s how to interpret the SHAP force plot:

- **Red arrows** indicate features that increase the likelihood of default (higher prediction values).
- **Blue arrows** indicate features that decrease the likelihood of default.
- The **length of each arrow** represents the relative importance of each feature in driving that specific prediction.

In the example SHAP plot:
- Features like `dti` and `total_il_high_credit_limit` push the prediction upwards, indicating a higher risk of default.
- Conversely, `il_util` and `total_rec_late_fee` push the prediction downwards, reducing the risk score.
  
The **base value** represents the average prediction for a positive class, while the final output value for each observation reflects its individual likelihood of default.

### 🎛️ Interactive SHAP Force Plot

![image](https://github.com/user-attachments/assets/ff1c4d45-3a69-4ba0-ab29-410e581dafe4)

![image](https://github.com/user-attachments/assets/53c7f5a6-5ea0-4cd9-be8b-bc2a6294abcf)


To make this analysis more user-friendly, I added a slider that lets us view the SHAP force plot for different observations. By moving the slider, we can see how each feature impacts the likelihood of default for individual loan applicants. For example:

- Observations with predictions above the base value (e.g., 0.23) indicate a higher likelihood of default.
- Observations with predictions below the base value (e.g., 0.07) indicate a lower likelihood of default.

This interactive approach allows us to explore how our selected features influence predictions at an individual level, enhancing our understanding of the model’s behaviour across various borrower profiles. This transparency is key to building trust in the model and ensuring it provides actionable insights.
