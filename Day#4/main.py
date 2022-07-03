from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:  # serialize our sql obj to json
        orm_mode = True

db=SessionLocal()

app = FastAPI()
