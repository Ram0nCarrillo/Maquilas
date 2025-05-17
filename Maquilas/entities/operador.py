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

id_supervisor = Column(Integer, ForeignKey("supervisor.id"))
supervisores = relationship("Supervisor", back_populates="operadores")
id_area = Column(Integer, ForeignKey("area.id"))
area = relationship("Area", back_populates="operadores")    