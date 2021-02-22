from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    parent_id = Column(Integer)
    destination_id = Column(Integer)
    is_container = Column(Boolean)
