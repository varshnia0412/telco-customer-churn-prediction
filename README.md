# 📊 Telco Customer Churn Prediction & Deployment

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/varshnia0412/telco-customer-churn-prediction/blob/main/notebooks/churn_analysis.ipynb)

## 🎯 Project Overview
This project provides an end-to-end Machine Learning solution to predict customer churn in the telecommunications industry. By identifying at-risk customers, businesses can take proactive measures to improve retention and reduce revenue loss.

## 🚀 Live App Preview
![App Screenshot](https://github.com/varshnia0412/telco-customer-churn-prediction/blob/main/screenshots/preview.png?raw=true)
*Interactive Dashboard built with Streamlit.*

## 🧠 Model Performance
I implemented a **Random Forest Classifier** which achieved:
- **Accuracy:** 81.41%
- **Key Predictors:** Contract Type, Tenure, and Internet Service Type.

## 📂 Project Structure
```text
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Dataset
├── models/
│   ├── churn_model.pkl                        # Trained Model
│   └── columns.pkl                            # Feature Metadata
├── notebooks/
│   └── Telco_Churn_Analysis.ipynb             # Full EDA & Training
├── app.py                                     # Streamlit Web App
├── requirements.txt                           # Dependencies
└── README.md

📈 Business Insights
- Month-to-month contracts are the strongest indicator of churn.
- Customers using Fiber Optic internet show higher churn rates, suggesting a need for service quality investigation.
- Long-term tenure (over 2 years) significantly reduces the probability of a customer leaving.
