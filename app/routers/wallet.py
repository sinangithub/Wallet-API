from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

router = APIRouter()   # 👈 this must be present

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Wallet
@router.post("/wallets/", response_model=schemas.Wallet)
def create_wallet(wallet: schemas.WalletCreate, db: Session = Depends(get_db)):
    return crud.create_wallet(db=db, wallet=wallet)

# Get Wallet by ID
@router.get("/wallets/{wallet_id}", response_model=schemas.Wallet)
def read_wallet(wallet_id: int, db: Session = Depends(get_db)):
    db_wallet = crud.get_wallet(db, wallet_id=wallet_id)
    if db_wallet is None:
        return {"error": "Wallet not found"}
    return db_wallet

