# 🏠 California House Price Prediction API

A production-style **Machine Learning REST API** built using **FastAPI** that predicts California house prices using a trained **Random Forest Regressor** model.

The API supports both:

* 🏡 Single house price prediction
* 📂 Batch prediction using CSV upload

This project demonstrates how to train a machine learning model, save it using Joblib, and deploy it as a REST API with FastAPI.

---

# 🚀 Features

* ✅ FastAPI REST API
* ✅ Random Forest Regression Model
* ✅ Single House Price Prediction
* ✅ Batch Prediction using CSV Upload
* ✅ Input Validation using Pydantic
* ✅ Health Check Endpoint
* ✅ Automatic API Documentation (Swagger UI)
* ✅ CSV Prediction Download
* ✅ Model Serialization using Joblib
* ✅ Production-ready Project Structure

---

# 🛠️ Tech Stack

* Python 3.11+
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Joblib
* Uvicorn
* Pydantic
* Python Multipart

---

# 📂 Project Structure

```text
House_Prediction_API/
│
├── app/
│   └── main.py                 # FastAPI application
│
├── data/
│   └── housing.csv             # California Housing dataset
│
├── models/
│   ├── house_model.joblib      # Trained Random Forest model
│   └── house_features.joblib   # Feature names used during training
│
├── train.py                    # Train the model and generate model files
│
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

# 📊 Machine Learning Model

**Algorithm**

* Random Forest Regressor

**Dataset**

* California Housing Dataset

**Libraries**

* Scikit-learn
* Pandas
* NumPy

**Model Storage**

* Joblib

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/harshalk2022/House_Prediction_API.git
cd House_Prediction_API
```

---

## 2. Create a Virtual Environment

### Windows CMD

```cmd
python -m venv house_predict_env
house_predict_env\Scripts\activate
```

### Git Bash

```bash
python -m venv house_predict_env
source house_predict_env/Scripts/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Train the Machine Learning Model

Before starting the API, generate the trained model files.

Run:

```bash
python train.py
```

This script will:

* Load the California Housing dataset
* Train a Random Forest Regression model
* Save the trained model
* Save the feature names

Generated files:

```text
models/
├── house_model.joblib
└── house_features.joblib
```

> **Note:** If these files already exist inside the `models/` folder, you can skip this step.

---

# ▶️ Run the FastAPI Application

```bash
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

# 📖 API Documentation

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

## 🏠 Home

**GET /**

Returns the API status.

Example Response

```json
{
    "message": "California house prediction api",
    "status": "running",
    "endpoint": "send POST request to /predict"
}
```

---

## ❤️ Health Check

**GET /health**

Returns:

* API status
* Model name
* Model features
* Average prediction error

Example Response

```json
{
    "status": "running",
    "model": "RandomForestRegressor",
    "features": [
        "MedInc",
        "HouseAge",
        "AveRooms",
        "AveBedrms",
        "Population",
        "AveOccup",
        "Latitude",
        "Longitude"
    ],
    "avg_error": "$39,000"
}
```

---

## 🏡 Single House Prediction

**POST /predict**

Request Body

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

## 📂 Batch Prediction

**POST /predict-file**

Upload a CSV file containing multiple house records.

### Required Columns

| Column     |
| ---------- |
| MedInc     |
| HouseAge   |
| AveRooms   |
| AveBedrms  |
| Population |
| AveOccup   |
| Latitude   |
| Longitude  |

The API returns a downloadable CSV containing predicted house prices.

---

# ✅ Input Validation

The API validates:

* Positive Median Income
* Positive Average Rooms
* Positive Average Bedrooms
* Positive Population
* Positive Average Occupancy
* Latitude between **32 and 42**
* Longitude between **-125 and -114**
* CSV file format
* Required CSV columns
* Empty CSV file detection

---

# 📥 Example CSV Input

```csv
MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude
8.3252,41,6.984,1.024,322,2.555,37.88,-122.23
7.2574,21,6.238,0.971,2401,2.109,37.86,-122.22
5.6431,52,5.817,1.073,496,2.802,37.85,-122.24
```

---

# 📤 Example CSV Output

| MedInc | HouseAge | AveRooms | Prediction |
| ------ | -------: | -------: | ---------: |
| 8.3252 |       41 |    6.984 |   $452,000 |
| 7.2574 |       21 |    6.238 |   $389,000 |
| 5.6431 |       52 |    5.817 |   $311,000 |

---

# 📦 Install Individual Packages

```bash
pip install fastapi
pip install uvicorn
pip install pandas
pip install numpy
pip install scikit-learn
pip install joblib
pip install python-multipart
```

Or simply run:

```bash
pip install -r requirements.txt
```

---

# 🔍 Error Handling

The API returns meaningful HTTP status codes.

| Status Code | Meaning                     |
| ----------- | --------------------------- |
| 200         | Success                     |
| 400         | Invalid input or CSV format |
| 404         | Endpoint not found          |
| 422         | Validation Error            |
| 500         | Internal Server Error       |

---

# 🚀 Future Improvements

* Docker Support
* Unit Testing
* Logging
* Model Versioning
* Authentication
* Database Integration
* CI/CD using GitHub Actions
* Cloud Deployment (Render, AWS, Azure)

---

# 👨‍💻 Author

**Harshal Khandalkar**

**GitHub**

https://github.com/harshalk2022

**LinkedIn**

https://www.linkedin.com/in/harshal-khandalkar/

---

# ⭐ If you found this project useful

If you like this project, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports my work.

---

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
