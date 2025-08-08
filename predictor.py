import joblib
import numpy as np

# Load the trained model
model = joblib.load("app/ml_model/demand_model.pkl")

def predict_demand(day_of_year, market_trend_index, price):
    features = np.array([[day_of_year, market_trend_index, price]])
    prediction = model.predict(features)
    return round(prediction[0], 2)


