from .preprocess import preprocess, load_model

MODEL = load_model("storage/models/logistic_regression_best_params.pkl")

def predict_probabilities(sku_data: dict) -> list:

    preprocessed_data = preprocess(sku_data)
    prediction = MODEL.predict_proba(preprocessed_data)

    return prediction.tolist()