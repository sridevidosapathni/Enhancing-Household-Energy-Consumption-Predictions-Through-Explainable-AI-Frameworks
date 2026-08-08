# Enhancing-Household-Energy-Consumption-Predictions-Through-Explainable-AI-Frameworks
# Enhancing Household Energy Consumption Predictions Through Explainable AI Frameworks

## Overview

This project focuses on predicting household energy consumption using Machine Learning and Deep Learning techniques while improving model transparency through Explainable Artificial Intelligence (XAI).

The project compares multiple predictive models and uses **SHAP (SHapley Additive exPlanations)** and **LIME (Local Interpretable Model-Agnostic Explanations)** to understand the factors influencing energy consumption predictions.

The main goal is to build accurate energy consumption prediction models while making their decisions understandable and interpretable.

## Objectives

* Predict household energy consumption accurately.
* Perform data preprocessing and exploratory data analysis.
* Handle missing values and outliers.
* Perform feature engineering and feature selection.
* Create temporal and lag-based features.
* Train and compare multiple Machine Learning and Deep Learning models.
* Evaluate models using standard regression metrics.
* Identify important factors affecting energy consumption.
* Apply SHAP and LIME for model interpretability.
* Improve transparency and trust in energy prediction models.

##  Project Workflow

```text
Data Collection
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Feature Scaling
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Best Model Selection
      ↓
Explainable AI
   ↙       ↘
 SHAP     LIME
   ↘       ↙
Feature Importance
      ↓
Interpretable Energy Predictions
```

##  Data Preprocessing

The following preprocessing techniques are applied:

* Missing value handling
* Duplicate removal
* Outlier detection using the **Interquartile Range (IQR)** method
* **Min-Max normalization**
* Data transformation
* Temporal feature extraction

## Feature Engineering

Several features are created to improve prediction performance:

* Hour
* Day
* Month
* Day of the week
* Weekend/weekday indicators
* Lag features
* Historical energy consumption
* Cyclical encoding of temporal features

Cyclical encoding is used to represent periodic time-based features effectively.

## Machine Learning Models

The project explores and compares the following models:

* **Random Forest**
* **XGBoost**
* **LightGBM**
* **CatBoost**
* **LSTM**
* **BiLSTM**

These models are trained to predict household energy consumption and their performance is compared using different evaluation metrics.

##  Model Evaluation

The models are evaluated using the following regression metrics:

| Metric       | Description                  |
| ------------ | ---------------------------- |
| **MAE**      | Mean Absolute Error          |
| **MSE**      | Mean Squared Error           |
| **RMSE**     | Root Mean Squared Error      |
| **R² Score** | Coefficient of Determination |

These metrics are used to measure prediction accuracy and compare the performance of different models.

##  Explainable AI

Explainable AI is an important component of this project. Instead of treating Machine Learning models as black boxes, XAI techniques are used to understand how different features contribute to predictions.

###  SHAP

**SHAP (SHapley Additive exPlanations)** is used to determine the contribution of individual features to model predictions.

SHAP helps with:

* Global feature importance
* Local prediction explanations
* Positive and negative feature contributions
* Understanding model behavior

###  LIME

**LIME (Local Interpretable Model-Agnostic Explanations)** is used to explain individual predictions by approximating the complex model locally with an interpretable model.

Together, SHAP and LIME provide a better understanding of the factors influencing household energy consumption predictions.

##  Technologies Used

### Programming Language

* Python

### Libraries and Frameworks

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* LightGBM
* CatBoost
* TensorFlow
* Keras
* SHAP
* LIME

### Development Tools

* Jupyter Notebook
* Google Colab

##  Project Structure

```text
Enhancing-Household-Energy-Consumption-Predictions-Through-Explainable-AI-Frameworks/
│
├── Dataset/
├── Notebooks/
├── Models/
├── Results/
├── Images/
├── requirements.txt
└── README.md
```

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sridevidosapathni/Enhancing-Household-Energy-Consumption-Predictions-Through-Explainable-AI-Frameworks.git
```

### 2. Navigate to the Project Directory

```bash
cd Enhancing-Household-Energy-Consumption-Predictions-Through-Explainable-AI-Frameworks
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

##  Usage

1. Clone the repository.
2. Install the required dependencies.
3. Open the project notebook.
4. Load the household energy consumption dataset.
5. Perform data preprocessing.
6. Perform exploratory data analysis.
7. Generate engineered features.
8. Train the Machine Learning and Deep Learning models.
9. Evaluate and compare model performance.
10. Select the best-performing model.
11. Apply SHAP and LIME to explain the model predictions.
12. Analyze the feature contributions and prediction results.

##  Results

The project evaluates different Machine Learning and Deep Learning models for household energy consumption prediction.

The models are compared using **R², MAE, MSE, and RMSE** to identify the most effective predictive model.

SHAP and LIME are then used to explain the selected model and identify the features that have the greatest influence on energy consumption predictions.

##  Key Features

*  Household energy consumption prediction
*  Data preprocessing and cleaning
*  Exploratory data analysis
*  Temporal and lag-based feature engineering
*  Machine Learning model comparison
*  Deep Learning-based prediction
*  Model performance evaluation
*  SHAP-based explainability
*  LIME-based explainability
*  Feature importance analysis
*  Interpretable energy consumption predictions

##  Future Scope

* Real-time household energy consumption prediction
* Smart meter and IoT integration
* Weather data integration
* Energy-saving recommendations
* Real-time monitoring dashboards
* Web and mobile application development
* Deployment of the prediction model as an API
* Integration with renewable energy and solar generation data

##  Author

**Sridevi Dosapathni**

##  License

This project is developed for academic and educational purposes.

