from sqlalchemy import Column, Integer, String, DECIMAL, Date, CHAR, ForeignKey
from sqlalchemy.orm import relationship
from persistence.base import Base


class Operador(Base):
    __tablename__ = 'operador'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    sexo = Column(CHAR)
    fecha_ingreso = Column(Date)
    turno = Column(String)
    salario = Column(DECIMAL)  

    # Claves foraneas 
    id_supervisor = Column(Integer, ForeignKey("supervisor.id"))
    id_area = Column(Integer, ForeignKey("area.id"))

    # Relaciones
    supervisor = relationship("Supervisor", back_populates="operadores")
    area = relationship("Area", back_populates="operadores")