## 🧠 Neural Network Challenger Model: Simple Architecture

## 🌟 Best Performing Neural Network Model: Intermediate Architecture

After testing multiple neural network architectures, the intermediate model emerged as the best performer, balancing high accuracy and efficient computational cost. Here’s a summary of its results:

### Key Metrics

- **Training Accuracy**: 98.62%
- **Validation Accuracy**: 98.72%
- **Training Loss**: 0.0478
- **Validation Loss**: 0.0505

### Model Insights

This intermediate architecture, with three hidden layers (32, 16, and 8 neurons), effectively captured the patterns in the data while avoiding overfitting. The training and validation accuracy curves converged closely, indicating that the model generalises well to unseen data. 

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


