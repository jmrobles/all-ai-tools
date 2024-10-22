from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pgvector.sqlalchemy import Vector
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define PostgreSQL model
class ToolVector(Base):
    __tablename__ = 'tool_vectors'

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    metadata = Column(Text)
    vector = Column(Vector(1536))

Base.metadata.create_all(engine)
