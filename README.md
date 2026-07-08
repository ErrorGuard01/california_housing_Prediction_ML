# 🏠 California Housing Price Prediction

A simple end-to-end Machine Learning project that predicts California housing prices based on various housing and location features. The project covers the complete ML workflow, from data preprocessing and model training to building and deploying a REST API using FastAPI.

## 📌 Project Overview

The objective of this project is to predict the median house value in California using historical housing data. It demonstrates a complete machine learning pipeline, including data preprocessing, feature engineering, model training, evaluation, and deployment.

## ✨ Features

* Data preprocessing and cleaning
* Feature engineering using Scikit-learn pipelines
* Model training and evaluation
* Saved trained model using Joblib
* REST API built with FastAPI
* Ready for cloud deployment

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* FastAPI
* Joblib
* Uvicorn


## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ErrorGuard01/california_housing_Prediction_ML.git
cd california_housing_Prediction_ML
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run the API

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

## 📊 Machine Learning Workflow

* Data Collection
* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Model Training
* Model Evaluation
* Model Serialization
* API Development
* Deployment

## 📈 Future Improvements

* Add Docker support
* Implement CI/CD pipeline
* Add model monitoring and logging
* Build a web interface for predictions

## 👨‍💻 Author

**Vijay Katiyar**

If you found this project helpful, feel free to give it a ⭐ on GitHub.
