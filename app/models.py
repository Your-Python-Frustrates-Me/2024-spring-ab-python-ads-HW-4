from sqlalchemy import Column, Integer, DateTime, String
from .database import Base


class RequestLog(Base):
    __tablename__ = "requests_log"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    country = Column(String, index=True)
    year = Column(Integer, index=True)
    trees = Column(Integer, index=True)
