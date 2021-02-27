from sqlalchemy import Column, Integer, String
from app.database import Base


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    content = Column(String, nullable=False)
