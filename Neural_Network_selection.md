## 🧠 Neural Network Challenger Model: Simple Architecture

## 🧠 Neural Network Model Summary

### Objective
The goal of this neural network exercise was to test various architectures and regularisation techniques to identify an optimal model for predicting loan defaults. I experimented with three primary configurations: basic neural networks, dropout with early stopping, and L2 regularisation. 

### Model Configurations Tested

1. **Basic Neural Networks (Model1a, Model1b, Model1c)**:
   - These models had straightforward architectures with layers and neurons but without additional regularisation.
   - Achieved high accuracy and AUC, performing well across metrics.

2. **Dropout with Early Stopping (Model2a - Model2e)**:
   - Dropout layers were used to prevent overfitting by randomly deactivating neurons during training.
   - Early stopping was implemented to halt training when validation performance plateaued.
   - This configuration consistently achieved high performance, with an AUC of 0.99 across all dropout models.

3. **L2 Regularisation (Model3a, Model3b)**:
   - L2 regularisation penalised large weights, further controlling overfitting.
   - This approach demonstrated strong generalisation, achieving an AUC of 0.98-0.99.

### Performance Overview

- **Accuracy**: All models, including those with dropout and L2 regularisation, maintained high accuracy scores around 0.98-0.99.
- **Precision**: Models consistently achieved precision of 0.97-0.99, indicating high accuracy in correctly predicting defaults.
- **Recall**: All models had a recall of 1.00, ensuring that they effectively captured all positive (default) cases.
- **AUC**: Most models achieved an AUC of 0.99, with only a slight decrease in the L2 regularisation models, which maintained an AUC of 0.98-0.99.

### ROC Curve Analysis

The ROC curve plot shows near-perfect separation, with all models achieving a high true positive rate across a low false positive rate. This curve underscores the models' strong performance in distinguishing between loan default and non-default cases. Each model's AUC score reinforces this, as most hover at 0.99, demonstrating excellent predictive capability.

### Conclusion

The neural network exercise successfully identified several high-performing configurations. Both dropout with early stopping and L2 regularisation effectively controlled overfitting, with dropout models slightly outperforming in terms of AUC. Given their robust performance, any of these configurations could be considered for deployment, with the final choice potentially depending on computational efficiency and specific deployment needs.


For this neural network experiment, I opted for a simpler model architecture to evaluate whether a more streamlined network could achieve comparable performance. This model acts as a challenger by testing if fewer layers and neurons can still capture the predictive patterns in our data with high accuracy.

### Model Architecture

- **Layer 1**: Dense layer with 16 neurons and ReLU activation. This layer takes the scaled input features and applies non-linear transformations to capture underlying patterns.
- **Layer 2**: Dense layer with 8 neurons and ReLU activation, refining the representations learned in the first layer.
- **Output Layer**: Dense layer with 1 neuron and sigmoid activation to output a probability score, indicating the likelihood of default.

### Training and Validation Results

- **Training Accuracy**: The model achieved a final training accuracy of **98.56%** with a low loss of **0.0538**.
- **Validation Accuracy**: The validation accuracy reached **98.51%** by the end of training, with a similarly low validation loss of **0.0566**.

### Training Curve Analysis

The training and validation accuracy curves indicate strong model performance with minimal signs of overfitting. Both curves converge closely, suggesting that the model generalises well to unseen data. The validation accuracy improves rapidly in the first few epochs, plateauing around epoch 4 as it nears maximum performance.

This experiment shows that even a relatively simple neural network architecture can achieve impressive predictive accuracy on this dataset. However, further testing and comparison with more complex models are necessary to confirm if this simpler model maintains robust performance across different data splits.

![image](https://github.com/user-attachments/assets/496b07dd-ce9f-4874-a844-e0a492a56809)

## 🧠 Neural Network Challenger Model: Intermediate Architecture

In this iteration, I tested a slightly more complex architecture to evaluate whether additional layers and neurons could enhance performance. This model serves as an intermediate challenger to both simpler and more complex architectures.

### Model Architecture

- **Layer 1**: Dense layer with 32 neurons and ReLU activation, providing a solid foundation for capturing non-linear relationships in the input data.
- **Layer 2**: Dense layer with 16 neurons and ReLU activation, narrowing down feature representations for more focused learning.
- **Layer 3**: Dense layer with 8 neurons and ReLU activation, further refining the learned representations.
- **Output Layer**: Dense layer with 1 neuron and sigmoid activation, providing a probability score for loan default likelihood.

### Training and Validation Results

- **Training Accuracy**: The model achieved a final training accuracy of **98.62%** with a minimal loss of **0.0478**.
- **Validation Accuracy**: The validation accuracy reached **98.72%** by the end of training, with a validation loss of **0.0505**.

### Training Curve Analysis

The training and validation curves show strong convergence, with both accuracy and loss stabilising at high performance levels. The validation accuracy closely follows the training accuracy, indicating a well-generalised model with minimal overfitting. The rapid improvement in the first few epochs followed by gradual convergence suggests the model quickly captured the main patterns and then fine-tuned these as training progressed.

This intermediate architecture demonstrates robust performance, achieving both high accuracy and low loss. It provides a balance between model complexity and generalisability, serving as a strong candidate for deployment while remaining efficient in terms of computation.

![image](https://github.com/user-attachments/assets/bae6ee03-e7e9-4569-8149-e385d15ffc16)

## 🧠 Neural Network Challenger Model: Complex Architecture

For this experiment, I implemented a deeper neural network with multiple layers and neurons to test the effectiveness of a more complex architecture on our loan default prediction task. This model aims to capture more intricate patterns within the data by utilising increased capacity and depth.

### Model Architecture

- **Layer 1**: Dense layer with 64 neurons and ReLU activation, allowing the model to capture complex, high-dimensional relationships from the input features.
- **Layer 2**: Dense layer with 32 neurons and ReLU activation, reducing dimensionality while retaining important information.
- **Layer 3**: Dense layer with 16 neurons and ReLU activation, refining feature interactions learned in previous layers.
- **Layer 4**: Dense layer with 8 neurons and ReLU activation, focusing on high-level abstractions.
- **Output Layer**: Dense layer with 1 neuron and sigmoid activation to output a probability score, indicating the likelihood of loan default.

### Training and Validation Results

- **Training Accuracy**: The model reached a final training accuracy of **98.68%** with a low loss of **0.0452**.
- **Validation Accuracy**: The validation accuracy achieved **98.66%** by the end of training, with a validation loss of **0.0490**.

### Training Curve Analysis

The training and validation accuracy curves show close convergence, suggesting that the model is generalising well without significant overfitting. Both training and validation accuracies increase steadily and then stabilise, indicating that the model is efficiently learning the key patterns within the data.

The complex architecture demonstrates high accuracy and low loss, supporting its capability to handle complex, non-linear relationships in the data. However, considering the minimal performance difference compared to simpler architectures, this model's added complexity may not provide substantial gains in accuracy, warranting further evaluation based on computational efficiency and deployment requirements.

![image](https://github.com/user-attachments/assets/d368756f-15ea-479a-9e0e-96603c1765e0)

## Regularisation Techniques to Improve Results

## 🧠 Neural Network Challenger Model with Dropout Layers

To address potential overfitting and improve generalisation, I introduced Dropout layers into the neural network. This model includes regularisation through dropout, which randomly deactivates neurons during training, helping the model learn more robust features.

### Model Architecture

- **Layer 1**: Dense layer with 32 neurons and ReLU activation.
  - **Dropout**: 50% dropout rate to prevent over-reliance on specific neurons.
- **Layer 2**: Dense layer with 16 neurons and ReLU activation.
  - **Dropout**: 50% dropout rate for regularisation.
- **Layer 3**: Dense layer with 8 neurons and ReLU activation.
  - **Dropout**: 50% dropout rate to encourage diversity in feature learning.
- **Output Layer**: Dense layer with 1 neuron and sigmoid activation, producing a probability score for default prediction.

### Training and Validation Results

- **AUC**: Reached a final AUC score of **0.9693**, indicating strong classification performance.
- **Precision**: Achieved a precision of **0.9796**, reflecting the model’s accuracy in predicting defaults.
- **Recall**: High recall at **0.9777**, ensuring that the model captures most positive instances (defaults).
- **Validation Accuracy**: Stabilised around **97.94%** with a low validation loss of **0.0959**.

### Training Curve Analysis

The training and validation curves show consistent performance, with validation accuracy stabilising early, thanks to the early stopping mechanism. The dropout layers appear effective in mitigating overfitting, as seen in the close alignment of training and validation accuracies. By epoch 15, the model demonstrates solid generalisation with minimal validation loss.

### Conclusion

The addition of Dropout layers allowed the model to achieve high accuracy and generalise well on unseen data, with strong AUC, precision, and recall metrics. This model is a promising candidate for production, as the dropout regularisation helps maintain accuracy without overfitting.

![image](https://github.com/user-attachments/assets/7bb6b05d-32a5-41d9-a194-bcf632ae0804)

## 🧠 Neural Network Challenger Model with Reduced Dropout

In this model, I applied a lighter regularisation approach by lowering the dropout rate to 20%, allowing more neurons to remain active during training. This was done to assess if a smaller dropout rate could maintain high generalisation while improving training performance.

### Model Architecture

- **Layer 1**: Dense layer with 32 neurons and ReLU activation.
  - **Dropout**: 20% dropout rate for mild regularisation.
- **Layer 2**: Dense layer with 16 neurons and ReLU activation.
  - **Dropout**: 20% dropout rate for reduced regularisation.
- **Layer 3**: Dense layer with 8 neurons and ReLU activation.
  - **Dropout**: 20% dropout rate to prevent overfitting.
- **Output Layer**: Dense layer with 1 neuron and sigmoid activation, producing a probability score for loan default prediction.

### Training and Validation Results

- **AUC**: The model reached an AUC score of **0.9854**, indicating strong separation between classes.
- **Precision**: High precision of **0.9810**, showing the model’s reliability in predicting defaults.
- **Recall**: Maintained a recall of **0.9965**, ensuring most positive instances were captured.
- **Validation Accuracy**: Stabilised around **98.31%** with a low validation loss of **0.0579**.

### Training Curve Analysis

The training and validation accuracy curves show close alignment, with validation accuracy converging early due to early stopping. The reduced dropout rate allowed for faster learning and a slightly higher training accuracy, while still preventing overfitting. This balance of dropout regularisation appears to be effective, as seen in the model's high precision and recall.

### Conclusion

With a lighter dropout rate, this model achieved a high AUC and balanced precision and recall. It is a strong candidate for deployment, as it combines efficient learning with robust generalisation.

![image](https://github.com/user-attachments/assets/885fcca4-73be-4c88-a04a-0318e33fbe16)

## 🧠 Neural Network Challenger Model with Increased Dropout

In this version, I applied a higher dropout rate of 50% across all layers to test its impact on model generalisation. The goal was to mitigate overfitting further and evaluate if a stronger regularisation effect would improve the model’s performance on validation data.

### Model Architecture

- **Layer 1**: Dense layer with 32 neurons and ReLU activation.
  - **Dropout**: 50% dropout rate for robust regularisation.
- **Layer 2**: Dense layer with 16 neurons and ReLU activation.
  - **Dropout**: 50% dropout rate to further reduce overfitting.
- **Layer 3**: Dense layer with 8 neurons and ReLU activation.
  - **Dropout**: 50% dropout rate to maintain regularisation consistency.
- **Output Layer**: Dense layer with 1 neuron and sigmoid activation, producing a probability score for loan default likelihood.

### Training and Validation Results

- **AUC**: Reached a final AUC score of **0.9686**, showing strong classification capability.
- **Precision**: Achieved a precision of **0.9768**, indicating accuracy in default predictions.
- **Recall**: High recall at **0.9800**, ensuring the model effectively captures most positive instances (defaults).
- **Validation Accuracy**: Stabilised at **98.01%** with a validation loss of **0.0815**.

### Training Curve Analysis

The training and validation accuracy curves reveal that the increased dropout helped maintain alignment between training and validation accuracies, effectively controlling overfitting. Both metrics stabilised by around epoch 8, suggesting early convergence with the assistance of early stopping. However, the higher dropout rate also slightly reduced the training accuracy, which is expected due to the aggressive regularisation.

### Conclusion

The model with a 50% dropout rate achieved strong validation metrics, balancing high precision and recall with effective overfitting control. This architecture is robust, making it suitable for deployment in scenarios where overfitting poses a significant risk.

![image](https://github.com/user-attachments/assets/02ea78f4-2b03-40e9-a34e-37b9d6c5f9ed)

## 🧠 Neural Network Challenger Model with Batch Normalisation and Dropout

In this model, I combined Batch Normalisation and Dropout layers to improve both model stability and generalisation. Batch Normalisation helps in accelerating training and stabilising learning, while Dropout reduces overfitting by randomly deactivating neurons during training.

### Model Architecture

- **Layer 1**: Dense layer with 64 neurons and ReLU activation.
  - **Batch Normalisation**: Normalises activations to stabilise training.
  - **Dropout**: 50% dropout rate for robust regularisation.
- **Layer 2**: Dense layer with 32 neurons and ReLU activation.
  - **Batch Normalisation**: Further normalises intermediate activations.
  - **Dropout**: 50% dropout rate to control overfitting.
- **Layer 3**: Dense layer with 16 neurons and ReLU activation.
  - **Batch Normalisation**: Ensures stable learning.
  - **Dropout**: 50% dropout rate for consistent regularisation.
- **Output Layer**: Dense layer with 1 neuron and sigmoid activation, providing a probability for loan default prediction.

### Training and Validation Results

- **AUC**: Achieved a final AUC of **0.9710**, indicating strong model performance in class separation.
- **Precision**: Reached a precision of **0.9764**, reflecting accuracy in default predictions.
- **Recall**: High recall of **0.9932**, ensuring the model captures most defaults.
- **Validation Accuracy**: Stabilised at **98.04%** with a validation loss of **0.066**.

### Training Curve Analysis

The training and validation accuracy curves show close convergence, indicating that the model generalises well on the validation set. The combination of Batch Normalisation and Dropout contributed to stable training and effective overfitting control, with the validation accuracy reaching a plateau after a few epochs. This balance allowed the model to learn efficiently without significant performance degradation on unseen data.

### Conclusion

The inclusion of Batch Normalisation with Dropout resulted in a well-performing model with high accuracy, precision, and recall. This model is a strong candidate for deployment due to its robustness and improved generalisation capabilities.

![image](https://github.com/user-attachments/assets/584bb647-ccc5-48e9-9935-6e9cc050ab91)

## 🧠 Neural Network Challenger Model with Light Dropout

In this model, I applied a lighter dropout rate of 20% to evaluate whether reduced regularisation could still provide strong generalisation while allowing for faster convergence. This model aims to maintain a balance between performance and efficiency, with fewer dropout layers than previous models.

### Model Architecture

- **Layer 1**: Dense layer with 32 neurons and ReLU activation.
  - **Dropout**: 20% dropout rate for moderate regularisation.
- **Layer 2**: Dense layer with 16 neurons and ReLU activation.
  - **Dropout**: 20% dropout rate to control overfitting.
- **Layer 3**: Dense layer with 8 neurons and ReLU activation, without additional dropout to allow full activation.
- **Output Layer**: Dense layer with 1 neuron and sigmoid activation, producing a probability for loan default prediction.

### Training and Validation Results

- **Training Accuracy**: The model reached a final training accuracy of **98.25%**.
- **Validation Accuracy**: The validation accuracy stabilised around **98.30%** with minimal signs of overfitting.
- **Validation Loss**: Low validation loss indicates that the model generalises well without substantial degradation.

### Training Curve Analysis

The training and validation accuracy curves are closely aligned, showing minimal divergence throughout the epochs, which suggests that the light dropout rate successfully controlled overfitting. Both metrics converged early due to the early stopping mechanism, highlighting stable performance across epochs.

### Conclusion

With a 20% dropout rate, this model achieved high accuracy and maintained effective generalisation. The lighter dropout rate balanced regularisation with efficient learning, making this model a practical choice for deployment scenarios where computational efficiency is important.

![image](https://github.com/user-attachments/assets/f9dfd2b4-7565-44cf-8f00-6df03000175b)

## 🧠 Neural Network Challenger Model with L2 Regularisation

This model applies L2 regularisation to each dense layer to penalise large weights and improve generalisation. L2 regularisation helps reduce overfitting by keeping the model parameters in check, leading to better stability in performance.

### Model Architecture

- **Layer 1**: Dense layer with 16 neurons and ReLU activation.
  - **L2 Regularisation**: Applied with a regularisation factor of 0.01.
- **Layer 2**: Dense layer with 8 neurons and ReLU activation.
  - **L2 Regularisation**: Also applied with a factor of 0.01.
- **Output Layer**: Dense layer with 1 neuron and sigmoid activation, outputting a probability score for loan default prediction.

### Training and Validation Results

- **Training Accuracy**: Reached **97.39%** by the final epoch.
- **Validation Accuracy**: Stabilised at **97.55%**, closely tracking the training accuracy.
- **AUC**: Achieved an AUC of **0.9833**, indicating strong capability in distinguishing between classes.
- **Precision**: High precision at **0.9737**, ensuring accurate identification of defaults.
- **Recall**: Very high recall of **0.9986**, capturing nearly all default cases.
- **Validation Loss**: Final validation loss of **0.1217**, indicating good model fit with minimal overfitting.

### Training Curve Analysis

The training and validation accuracy curves are well-aligned, showing that the L2 regularisation was effective in controlling overfitting. Both accuracies improved steadily and converged smoothly, indicating that the model learned effectively without memorising the training data.

### Conclusion

This model with L2 regularisation demonstrated high accuracy, AUC, precision, and recall, making it a strong candidate for production use. The close alignment of training and validation performance underscores its generalisation ability, providing reliable predictions on unseen data.

![image](https://github.com/user-attachments/assets/c0bd0481-f8e8-47b1-b314-a7bf6eaeb983)

## 🧠 Neural Network Challenger Model with L2 Regularisation and Dropout

In this model, I combined L2 regularisation with dropout to control overfitting and improve generalisation. L2 regularisation penalises large weights, while dropout randomly deactivates neurons during training to prevent the model from relying too heavily on any single neuron.

### Model Architecture

- **Layer 1**: Dense layer with 64 neurons and ReLU activation.
  - **L2 Regularisation**: Applied with a regularisation factor of 0.001.
  - **Dropout**: 30% dropout rate to prevent overfitting.
- **Layer 2**: Dense layer with 32 neurons and ReLU activation.
  - **L2 Regularisation**: Applied with a regularisation factor of 0.001.
  - **Dropout**: 30% dropout rate to maintain regularisation.
- **Layer 3**: Dense layer with 16 neurons and ReLU activation.
  - **L2 Regularisation**: Applied with a regularisation factor of 0.001.
  - **Dropout**: 30% dropout rate to ensure robustness.
- **Output Layer**: Dense layer with 1 neuron and sigmoid activation, producing a probability score for loan default prediction.

### Training and Validation Results

- **Training Accuracy**: Reached **97.52%** by the final epoch.
- **Validation Accuracy**: Stabilised at **98.08%**, demonstrating strong generalisation.
- **AUC**: Achieved an AUC of **0.9783**, showing effective class separation.
- **Precision**: High precision at **0.9786**, indicating accurate identification of defaults.
- **Recall**: High recall at **0.9935**, ensuring most default cases were captured.
- **Validation Loss**: Final validation loss of **0.0956**, indicating a good fit with minimal overfitting.

### Training Curve Analysis

The training and validation curves display a stable progression, with minimal divergence. The combination of L2 regularisation and dropout was effective in controlling overfitting, as evidenced by the close alignment of training and validation accuracy. Both accuracies converged early, with the validation curve slightly outperforming the training curve, highlighting the model’s strong generalisation.

### Conclusion

The combination of L2 regularisation and dropout allowed this model to achieve high accuracy, AUC, precision, and recall. The stability and strong performance on validation data make it a robust candidate for deployment, especially in scenarios where overfitting control is critical.

![image](https://github.com/user-attachments/assets/b56241f4-7161-4cff-a0af-b5da7df728cd)
