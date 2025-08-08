from pydantic import BaseModel

class SalesData(BaseModel):
    product_id: str
    date: str  # YYYY-MM-DD
    units_sold: int
    market_trend_index: float
    price: float

class InventaryData(BaseModel):
    product_id: str
    current_stock: int
    warehouse: str

