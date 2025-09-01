# crud.py
from sqlalchemy.orm import Session
from app import models

def update_wallet(db: Session, wallet_id: int, amount: float):
    wallet = db.query(models.Wallet).filter(models.Wallet.id == wallet_id).first()
    if not wallet:
        return None

    # Update balance
    wallet.balance += amount

    # Decide transaction type
    txn_type = "credit" if amount > 0 else "debit"

    # Create and link transaction
    transaction = models.Transaction(
        wallet_id=wallet.id,
        amount=amount,
        type=txn_type
    )

    db.add(transaction)
    db.commit()
    db.refresh(wallet)
    return wallet


# ✅ New function to get transactions by user_id
def get_transactions_by_user(db: Session, user_id: int):
    return (
        db.query(models.Transaction)
        .join(models.Wallet)
        .filter(models.Wallet.user_id == user_id)
        .all()
    )


# ✅ Optional: get all transactions of a single wallet
def get_transactions(db: Session, wallet_id: int):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.wallet_id == wallet_id)
        .all()
    )

