from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from persistence.base import Base

class Supervisor(Base):
    __tablename__ = 'supervisor'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    sexo = Column(String)
    salario = Column(DECIMAL)
    telefono = Column(String)
    correo = Column(String)
    turno = Column(String)
    
    id_area = Column(Integer, ForeignKey("area.id"))
    area = relationship("Area", back_populates="supervisores")

    # Relación con operadores
    operadores = relationship("Operador", back_populates="supervisor")