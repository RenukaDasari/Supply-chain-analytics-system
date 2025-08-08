from fastapi import FastAPI
from app.routers import data_routes, analytics_routes


app = FastAPI(title="AI Supply Chain System")

app.include_router(data_routes.router)
app.include_router(analytics_routes.router)

