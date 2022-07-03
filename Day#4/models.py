from database import Base
from sqlalchemy import String, Float, Integer, Column, Text

class Item(Base): # inherets from Base class
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    price = Column(Float, nullable=False)
    tax = Column(Float)

    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"
