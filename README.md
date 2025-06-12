# 🧠 Health Prediction Dashboard for Somalia

This is a Streamlit-based interactive web application that predicts **Measles**, **Malaria**, and **SAM (Severe Acute Malnutrition)** cases in Somalia based on environmental and health-related factors.

🌐 **Live App:**  
👉 [Launch Dashboard](https://health-dashboard0.streamlit.app/)

---

## 📊 Features

- Predicts health outcomes using trained machine learning models.
- Inputs include: vaccination rates, rainfall, temperature, mosquito density, and more.
- Stylish, mobile-friendly dashboard using **Streamlit** and **custom CSS**.
- Supports predictions across multiple Somali regions (Banadir, Hargeisa, Kismayo, etc.)

---

## 🧮 Prediction Models

Trained using `scikit-learn` and exported with `joblib`:

- `measles_model.joblib`
- `malaria_model.joblib`
- `sam_model.joblib`

---

## 📥 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/Mezoutsena77/health-dashboard.git
cd health-dashboard
pip install -r requirements.txt
