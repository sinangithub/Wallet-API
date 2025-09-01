from pydantic import BaseModel
from typing import List, Optional

# User Schemas
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# Wallet Schemas
class WalletBase(BaseModel):
    balance: float = 0.0

class WalletCreate(WalletBase):
    pass

class Wallet(WalletBase):
    id: int
    user_id: int
    transactions: List["Transaction"] = []

    class Config:
        orm_mode = True


# Transaction Schemas
class TransactionBase(BaseModel):
    amount: float
    type: str   # e.g., "credit" or "debit"

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    wallet_id: int

    class Config:
        orm_mode = True







