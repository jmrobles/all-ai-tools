from sqlalchemy import Column, Integer, String
from app.db.base import Base  

class DataAITools(Base):
    __tablename__ = "data_ai_tools"

    id = Column(Integer, primary_key=True, index=True)
