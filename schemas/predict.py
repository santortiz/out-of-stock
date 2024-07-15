from pydantic import BaseModel

class PredictRequest(BaseModel):
    sold_quantity: int
    current_price: float
    currency: str
    listing_type: str
    shipping_logistic_type: str
    shipping_payment: str
    cluster: int