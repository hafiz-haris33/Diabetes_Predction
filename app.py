from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load("diabetes_model.pkl")
training_columns = joblib.load("training_columns.pkl")

app = FastAPI()

class PatientData(BaseModel):
    age: float
    urea: float
    cr: float
    hba1c: float
    chol: float
    tg: float
    hdl: float
    ldl: float
    vldl: float
    bmi: float
    gender: str


@app.get("/")
def home():
    return {"status": "API is running"}

@app.post("/predict")
def predict(data: PatientData):

    # Step 1: convert input to dict
    input_data = data.model_dump()  # Convert Pydantic model to dict

    # Step 2: convert to DataFrame
    df = pd.DataFrame([input_data])

    # Step 3: one-hot encoding on gender
    df = pd.get_dummies(df, columns=["gender"])

    # Step 4: align with training columns
    df = df.reindex(columns=training_columns, fill_value=0)

    # Step 5: prediction
    prediction = model.predict(df)

    # Step 6: return result
    return {
        "prediction": int(prediction[0])
    }