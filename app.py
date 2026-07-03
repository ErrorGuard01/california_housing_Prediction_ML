from fastapi import FastAPI,HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import logging

load_dotenv()

Model_Path = os.getenv("Model_Path")
API_Name = os.getenv("API_Name")
API_Version = os.getenv("API_Version")


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HouseData(BaseModel):
    MedInc: float = Field(gt=0)
    HouseAge: float = Field(ge=0)
    AveRooms: float = Field(gt=0)
    AveBedrms: float = Field(gt=0)
    Population: float = Field(ge=0)
    AveOccup: float = Field(gt=0)
    Latitude: float  
    Longitude: float 

app = FastAPI(title=API_Name, description="An API to predict California housing prices based on input features.", version=API_Version)
model = joblib.load(Model_Path)


@app.get("/")
def home():
    logger.info("API Status: Running")
    return {"message": "Welcome to the California Housing Price Prediction API!"}


@app.post("/predict")
def predict(data: HouseData):
    
    try:
        input_data = pd.DataFrame([data.model_dump()])
        prediction = model.predict(input_data)
        logger.info(f"Prediction successful")
        return {"predicted_house_price": float(prediction[0])}
    except Exception as e:
        logger.error(f"Error occurred while making prediction: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")