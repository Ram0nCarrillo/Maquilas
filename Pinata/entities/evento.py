from sqlalchemy import Column, Integer, String, Date, ForeignKey
from persistence.base import Base
from sqlalchemy.orm import relationship

class Evento(Base):
    __tablename__ = "evento"
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    fecha = Column(Date)
    
    # llave foranea
    id_cliente = Column(Integer, ForeignKey("cliente.id"))
    cliente = relationship("Cliente", uselist=False)