## 🔍 SHAP Value Visualisation and Model Interpretability

To gain deeper insights into how each selected feature contributes to our model’s predictions, I used SHAP (SHapley Additive exPlanations) values. SHAP is a powerful tool for interpreting model outputs by showing the impact of each feature on individual predictions. This helps ensure that the model's decision-making aligns with our objectives and provides transparency in understanding the factors driving loan default predictions.

### 🧩 Understanding Feature Importance

I transformed the data into a NumPy array and used parallel processing to speed up SHAP calculations. Upon reviewing the feature importance values, I observed that there isn’t a single dominant feature driving the model's predictions. Instead, most feature importance scores range between 0.01 and 0.09. This suggests that the model depends on a variety of features, rather than focusing on a small subset, which is ideal for capturing nuanced patterns across different borrower profiles.

![image](https://github.com/user-attachments/assets/579685a3-4427-4530-9bac-30d72aa3bc63)


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


### 🔍 SHAP Analysis for Loan Default Predictions

#### Observation 128

In this SHAP force plot, the predicted value for the likelihood of default is **0.95**, which is significantly above the base value of **0.8658**. Key features influencing this high prediction include:

- **Debt-to-Income (DTI)**: With a positive SHAP value of **0.6154**, this feature strongly increases the likelihood of default, indicating that a high DTI ratio is a major risk factor.
- **`earliest_cr_line_year_kn`**: This feature contributes negatively to the prediction with a SHAP value of **-0.8838**, suggesting that an earlier credit line start date reduces the default risk.
- **`total_bal_ex_mort`** and **`mo_sin_rcnt_rev_tl_op`**: These features contribute positively, albeit to a lesser degree, to the prediction, indicating they add minor risks.
- **`mths_since_recent_bc`** and **`total_il_high_credit_limit`**: These features have negative contributions, helping to reduce the default likelihood but not enough to offset the higher-risk factors.

#### Observation 402

In this force plot, the predicted likelihood of default is **0.22**, which is well below the base value of **0.8658**. The primary factors reducing this prediction are:

- **`earliest_cr_line_year_kn`**: With a large negative contribution of **-0.8838**, an earlier credit line start date strongly reduces default risk for this observation.
- **`mo_sin_rcnt_rev_tl_op`**: This feature adds a positive contribution of **1.013**, which slightly increases the default risk but is outweighed by other factors.
- **`total_rec_late_fee`** and **`total_il_high_credit_limit`**: Both features contribute negatively, with **total_il_high_credit_limit** having the strongest impact here, indicating a high credit limit on installment loans reduces the default likelihood.

---

These SHAP plots highlight how features like `earliest_cr_line_year_kn` and `total_il_high_credit_limit` play significant roles in mitigating default risk, while a high DTI or recent revolving accounts (e.g., `mo_sin_rcnt_rev_tl_op`) can increase risk.

