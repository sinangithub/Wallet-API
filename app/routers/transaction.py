# app/routers/transaction.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, database, schemas

# Initialize router
router = APIRouter()

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Update wallet balance (adds a transaction automatically)
@router.put("/{wallet_id}/update", response_model=schemas.Wallet)
def update_wallet(wallet_id: int, amount: float, db: Session = Depends(get_db)):
    return crud.update_wallet(db=db, wallet_id=wallet_id, amount=amount)

# Fetch transactions for a user
@router.get("/user/{user_id}", response_model=list[schemas.Transaction])
def fetch_transactions(user_id: int, db: Session = Depends(get_db)):
    return crud.get_transactions_by_user(db, user_id)

