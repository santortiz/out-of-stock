from fastapi import APIRouter
from services.predict import predict_probabilities
from schemas.predict import PredictRequest

router = APIRouter()


@router.post("/predict")
async def predict(
    prediction_request: PredictRequest
) -> dict:
    prediction = predict_probabilities(prediction_request.dict())

    return {"prediction": prediction}