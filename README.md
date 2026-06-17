# 🛒 E-Commerce Product Success AI Strategist

## 📌 Overview

E-Commerce Product Success AI Strategist is an AI-powered application that predicts the success probability of a product before launch. The system combines Machine Learning, Explainable AI, and Generative AI to help sellers make data-driven business decisions.

The application analyzes product attributes such as category, price, title length, description length, images, and physical dimensions to estimate product success and generate actionable business recommendations.

---

## 🚀 Features

* Predict product success probability using XGBoost
* Explain predictions using SHAP Explainable AI
* Generate AI-powered business recommendations using Gemini
* Interactive Streamlit dashboard
* Real-time product analysis
* Feature importance visualization
* Pricing strategy suggestions
* Product listing optimization recommendations

---

## 🏗️ System Architecture

```text
User Input
     │
     ▼
Feature Engineering
     │
     ▼
XGBoost Model
     │
     ▼
Success Probability
     │
     ├────────► SHAP Explainability
     │
     ▼
Gemini AI Recommendations
     │
     ▼
Streamlit Dashboard
```

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Scikit-Learn
* XGBoost

### Explainable AI

* SHAP

### Generative AI

* Google Gemini API

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Model Storage

* Joblib

---

## 📊 Dataset

The project uses an E-Commerce Product Dataset containing:

* Product Category
* Product Price
* Product Description
* Product Name
* Product Images Count
* Product Dimensions
* Product Ratings
* Product Reviews

---

## ⚙️ Feature Engineering

The following features are generated:

* avg_price
* category_avg_price
* category_avg_sales
* price_vs_category
* product_name_lenght
* product_description_lenght
* product_photos_qty
* product_weight_g
* product_length_cm
* product_height_cm
* product_width_cm
* category_encoded

---

## 🤖 Machine Learning Model

### XGBoost Classifier

The model was trained using engineered product features to classify products as successful or unsuccessful.

Benefits:

* Handles non-linear relationships
* High predictive performance
* Fast inference
* Robust feature importance analysis

---

## 🔍 Explainable AI

SHAP (SHapley Additive exPlanations) is used to explain model predictions.

Example Insights:

* Price increases success probability
* Description quality impacts performance
* Category competitiveness affects sales
* Product images influence conversions

---

## 🧠 Generative AI Integration

Google Gemini generates:

* Product launch recommendations
* Pricing strategies
* Listing optimization suggestions
* Marketing recommendations
* Risk assessment reports

---

## 💻 Streamlit Dashboard

Users can enter:

* Category
* Product Price
* Product Name
* Product Description
* Number of Images
* Weight
* Length
* Height
* Width

The application then provides:

* Success Probability
* Key Drivers
* AI Strategy Report

---

## 📈 Workflow

1. User enters product details.
2. Features are engineered.
3. XGBoost predicts success probability.
4. SHAP identifies key influencing factors.
5. Gemini generates business recommendations.
6. Results are displayed on Streamlit.

---

## 📂 Project Structure

```text
project/
│
├── app.py
├── xgb_model.pkl
├── shap_explainer.pkl
├── features.pkl
├── category_stats_india.csv
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone Repository

```bash
git clone <your-github-repo>
cd project
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Application

```bash
streamlit run app.py
```

---

## 📊 Business Impact

This solution helps:

* E-Commerce Sellers
* Product Managers
* Marketing Teams
* Marketplace Consultants

Benefits:

* Reduce product launch risk
* Improve pricing decisions
* Optimize product listings
* Increase conversion potential

---

## 🔮 Future Enhancements

* Product Image Analysis using Computer Vision
* Multimodal AI Models
* Real-time Amazon/Flipkart Integration
* Demand Forecasting
* Agentic AI Product Consultant
* Recommendation Engine Integration

---

## 👨‍💻 Author

Akash Singh

B.Tech (Data Science)

Machine Learning | Data Science | Generative AI | MLOps

GitHub: https://github.com/akashsingh62

LinkedIn: https://www.linkedin.com/in/akashsingh62/

---

## ⭐ If you found this project useful, please consider giving it a star.
