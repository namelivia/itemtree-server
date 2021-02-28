from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, nullable=False)
    user_id = Column(String, nullable=False)
    user_name = Column(String)
    content = Column(String, nullable=False)
    date = Column(DateTime, nullable=False, server_default=func.now())
