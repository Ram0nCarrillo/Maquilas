from sqlalchemy import Column, Integer, String
from persistence.base import Base

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    telefono = Column(String)
    domicilio = Column(String)