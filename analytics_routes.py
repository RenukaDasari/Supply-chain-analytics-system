from fastapi import APIRouter
from datetime import datetime
from app.ml_model.predictor import predict_demand  # or correct import

router = APIRouter()

@router.get("/forecast")
def forecast(product_id: str, date: str, market_trend_index: float, price: float):
    day_of_year = datetime.strptime(date, "%Y-%m-%d").timetuple().tm_yday
    forecast = predict_demand(day_of_year, market_trend_index, price)
    optimized_inventory = round(forecast * 1.1)

    return {
        "product_id": product_id,
        "forecasted_demand": round(forecast),
        "optimized_inventory": optimized_inventory
    }

