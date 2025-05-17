from sqlalchemy import Column, Integer, String, TEXT
from persistence.base import Base
from sqlalchemy.orm import relationship

class Area(Base):
    __tablename__ = 'area'
    id = Column(Integer, primary_key = True)
    departamento = Column(String, nullable=False)
    descripcion = Column(TEXT)
    
supervisores = relationship("Supervisor", back_populates="area")
operadores = relationship("Operador", back_populates="area")