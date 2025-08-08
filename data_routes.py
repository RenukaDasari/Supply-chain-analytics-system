from fastapi import APIRouter
from app.schemas import SalesData, InventaryData
from app.database import sales_collection, inventory_collection

router = APIRouter()

@router.post("/sales/")
def add_sales(data: SalesData):
    sales_collection.insert_one(data.dict())
    return {"msg": "Sales data inserted"}

@router.post("/inventory/")
def add_inventory(data: InventaryData):
    inventory_collection.insert_one(data.dict())
    return {"msg": "Inventory data inserted"}

@router.get("/")
def read_root():
    return {"message": "Welcome to the AI Supply Chain API"}
