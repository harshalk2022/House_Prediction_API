# 🏠 California House Price Prediction API

A production-style Machine Learning REST API built with **FastAPI** for predicting California house prices using a trained **Random Forest Regressor** model.

This project demonstrates how to deploy a machine learning model as a REST API with support for both:

- Single house prediction
- Batch prediction using CSV upload

---

# 🚀 Features

- FastAPI REST API
- Random Forest Regression model
- Single prediction endpoint
- Batch CSV prediction
- Pydantic request validation
- Input validation
- Health check endpoint
- Download prediction results as CSV
- Interactive Swagger UI
- Automatic OpenAPI documentation

---

# 🛠 Tech Stack

- Python 3.11+
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Uvicorn
- Pydantic

---

# 📂 Project Structure

```
House_Prediction_API/
│
├── app/
│   └── main.py
│
├── models/
│   ├── house_model.joblib
│   └── house_features.joblib
│
├── data/
│   └── housing.csv
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/harshalk2022/House_Prediction_API.git
```

Go to the project directory

```bash
cd House_Prediction_API
```

Create Virtual Environment

Windows

```bash
python -m venv house_predict_env
```

Activate

CMD

```cmd
house_predict_env\Scripts\activate
```

Git Bash

```bash
source house_predict_env/Scripts/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run the API

```bash
uvicorn app.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📌 API Endpoints

## Home

```
GET /
```

Returns API status.

---

## Health Check

```
GET /health
```

Returns

- Model name
- Features used
- Average model error

---

## Predict House Price

```
POST /predict
```

Example Request

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41,
  "AveRooms": 6.984,
  "AveBedrms": 1.024,
  "Population": 322,
  "AveOccup": 2.555,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

Example Response

```json
{
  "predicted_price": "$452,000",
  "predicted_price_short": "$4.52 hundred thousands",
  "confidence_range": "$413,000 to $491,000"
}
```

---

## Batch Prediction

```
POST /predict-file
```

Upload a CSV file containing multiple houses.

Required Columns

| Column |
|---------|
| MedInc |
| HouseAge |
| AveRooms |
| AveBedrms |
| Population |
| AveOccup |
| Latitude |
| Longitude |

Returns a downloadable CSV containing predicted prices.

---

# 📊 Machine Learning Model

Model

- Random Forest Regressor

Dataset

- California Housing Dataset

Framework

- Scikit-learn

Model Serialization

- Joblib

---

# 📖 Input Validation

The API validates:

- Positive income
- Valid latitude range
- Valid longitude range
- Positive room counts
- Population > 0
- CSV format
- Required columns
- Empty file detection

---

# 🧪 Testing

Interactive API documentation

```
http://127.0.0.1:8000/docs
```

---

# 📦 Dependencies

Install

```bash
pip install -r requirements.txt
```

or

```bash
pip install fastapi uvicorn pandas scikit-learn joblib python-multipart
```

---

# 👨‍💻 Author

**Harshal Khandalkar**

GitHub

https://github.com/harshalk2022

LinkedIn

https://www.linkedin.com/in/harshal-khandalkar/

---

# ⭐ Future Improvements

- Docker support
- Logging
- Authentication
- Model versioning
- Unit testing
- CI/CD with GitHub Actions
- Cloud deployment (Render/AWS/Azure)
- Database integration

---

If you found this project useful, consider giving it a ⭐ on GitHub.