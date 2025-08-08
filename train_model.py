import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from app.database import sales_collection

def train_model():
    data = list(sales_collection.find({}, {'_id': 0}))
    df = pd.DataFrame(data)

    if df.empty:
        raise ValueError("No sales data available to train the model.")

    df['date'] = pd.to_datetime(df['date'])
    df['day'] = df['date'].dt.dayofyear

    X = df[['day', 'market_trend_index', 'price']]
    y = df['units_sold']

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "app/ml_model/demand_model.pkl")
