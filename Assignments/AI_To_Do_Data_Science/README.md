# Heart Attack Risk Prediction using Machine Learning

This repository showcases a machine learning project aimed at predicting the risk of heart attacks based on medical, lifestyle, and demographic features using a **Gradient Boosting Classifier**.

### Project Overview:
The dataset contains various health-related features such as age, cholesterol levels, blood pressure, exercise hours, and other demographic details. The goal is to create a predictive model to help healthcare professionals identify high-risk patients.

### Steps Involved:

1. **Data Loading**: Load the heart attack prediction dataset.
2. **Data Cleaning and Preprocessing**:
   - Split features like blood pressure into systolic and diastolic values.
   - Encode categorical variables such as gender, diet, and country.
   - Handle missing values and scale numerical data.
3. **Splitting the Data**: Split the dataset into training and testing sets to ensure robust evaluation.
4. **Standardization**: Standardize numerical features to bring them to the same scale for efficient model training.
5. **Model Training**: Train the **Gradient Boosting Classifier** using the training data.
6. **Model Evaluation**: Evaluate the model on the test set using classification metrics like precision, recall, and F1-score to measure its performance.
7. **Sample Prediction**: Perform a sample prediction to demonstrate how the trained model predicts heart attack risk for a single patient.

### Colab Notebook:
You can run the complete project using this [Colab notebook](https://colab.research.google.com/github/pruthvik-sheth/CMPE-255-Data-Mining/tree/main/Assignments/AI_To_Do_Data_Science).

### Medium Article:
A detailed explanation of the project can be found in this [Medium article](https://medium.com/@pns00911/predicting-heart-attack-risk-using-gradient-boosting-a-comprehensive-data-science-workflow-9b1068d66e1b).