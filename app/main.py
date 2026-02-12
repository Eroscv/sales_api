from fastapi import FastAPI
from core.database import Base, engine
from routes import sale_routes, analytics_routes, text_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sales API - SQLite + MongoDB")

app.include_router(sale_routes.router)
app.include_router(analytics_routes.router)
app.include_router(text_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",  # localhost
        port=8000,
        reload=True
    )
