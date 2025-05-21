from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Date
from sqlalchemy.orm import relationship
from persistence.base import Base

class Supervisor(Base):
    __tablename__ = 'supervisor'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    sexo = Column(String)
    fecha_ingreso = Column(Date)
    salario = Column(DECIMAL)
    telefono = Column(String)
    correo = Column(String)
    turno = Column(String)
    
    # Clave foranea hacia el area que supervisa 
    id_area = Column(Integer, ForeignKey("area.id"))
    
    # Relaciones
    area = relationship("Area", back_populates="supervisores")
    operadores = relationship("Operador", back_populates="supervisor")