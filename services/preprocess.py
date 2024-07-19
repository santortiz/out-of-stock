from pandas import DataFrame, get_dummies
from numpy import array
from pickle import load

CORE_SKUS_COLUMNS = [
    'sold_quantity',
    'current_price',
    'currency_ARG',
    'currency_MEX',
    'currency_REA',
    'listing_type_premium',
    'shipping_logistic_type_cross_docking',
    'shipping_logistic_type_drop_off',
    'shipping_logistic_type_fulfillment',
    'shipping_payment_paid_shipping',
    'cluster_0',
    'cluster_1',
    'cluster_2',
    'cluster_3',
    'cluster_4',
]

def load_model(path_to_model):
    with open(path_to_model, "rb") as file:
        model = load(file)
    return model

def scale(sku_data: dict) -> dict:
    currency = sku_data["currency"]
    scaler = load_model(f"storage/models/{currency}_scaler.pkl")

    scaled_values = scaler.transform(
        array([sku_data["sold_quantity"], sku_data["current_price"]]).reshape(1, -1)
    )

    sku_data["sold_quantity"] = scaled_values[0][0]
    sku_data["current_price"] = scaled_values[0][1]

    return sku_data

def dummy_encode(sku_data: dict) -> DataFrame:
    new_entry_df = DataFrame().from_dict(sku_data, orient="index").T
    new_entry_encoded = get_dummies(
        new_entry_df,
        columns=["currency", "listing_type", "shipping_logistic_type", "shipping_payment", "cluster"]
    )

    new_entry_aligned = new_entry_encoded.reindex(columns=CORE_SKUS_COLUMNS, fill_value=0)

    return new_entry_aligned.astype(float)


def preprocess(sku_data: dict) -> DataFrame:
    scaled_data = scale(sku_data)
    preprocessed_data = dummy_encode(scaled_data)
    return preprocessed_data