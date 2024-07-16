from abc import ABC, abstractmethod
from .preprocess import preprocess
import joblib

class ModelPredictor(ABC):
    
    def __init__(self, model_path: str):
        self.model = self.load_model(model_path)
    
    @staticmethod
    def load_model(model_path: str):
        return joblib.load(model_path)
    
    @abstractmethod
    def predict_probabilities(self, sku_data: dict) -> list:
        pass

class GeneralModelPredictor(ModelPredictor):
    
    def predict_probabilities(self, sku_data: dict) -> list:
        preprocessed_data = preprocess(sku_data)
        prediction = self.model.predict_proba(preprocessed_data)
        return prediction.tolist()