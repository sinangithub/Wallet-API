from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import user, wallet, transaction   # <-- include transaction router

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Wallet Management API")

# Routers
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(wallet.router, prefix="/wallets", tags=["Wallets"])
app.include_router(transaction.router, prefix="/transactions", tags=["Transactions"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, Wallet API is working!"}



