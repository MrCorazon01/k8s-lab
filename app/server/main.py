from fastapi import FastAPI
from app.server.routers import health, items
from app.server.database import init_db

app = FastAPI()

# Initialize the database when the app starts
@app.on_event("startup")
async def startup():
    await init_db()

# Include routers
app.include_router(health.router)
app.include_router(items.router)

# Root endpoint
# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to my Python Kubernetes Lab API!"}
