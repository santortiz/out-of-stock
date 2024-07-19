from fastapi import APIRouter
from services.predict import GeneralModelPredictor
from schemas.predict import PredictRequest

#MODEL_PATH = "storage/models/logistic_regression_best_params.pkl"
#MODEL_PATH = "storage/models/rf_classifier_best_params.pkl"
MODEL_PATH = "storage/models/xgb_classifier_best_params.pkl"
MODEL = GeneralModelPredictor(MODEL_PATH)

router = APIRouter()


@router.post("/predict")
async def predict(
    prediction_request: PredictRequest
) -> dict:
    
    prediction = MODEL.predict_probabilities(prediction_request.dict())

    return {"prediction": prediction}