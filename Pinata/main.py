from entities.cliente import Cliente
from persistence.db import SessionLocal
from entities.evento import Evento

session = SessionLocal()

def get():
    clientes = SessionLocal().query(Cliente).all()
    for c in clientes:
        print(f"\nId: {c.id}\nNombre: {c.nombre}\nTelefono: {c.telefono}\nDomicilio: {c.domicilio}")
        
        
def save(nombre, telefono, domicilio):
    SessionLocal().query(Cliente).all()
    c = Cliente(nombre = nombre, telefono = telefono, domicilio = domicilio)
    session.add(c)
    session.commit()
    print(f"\nSe agrego el registro {c.nombre}")
 
def update(id, nombre, telefono, domicilio):
    cliente = session.query(Cliente).filter_by(id = id).first()
    if cliente:
        cliente.nombre = nombre
        cliente.telefono = telefono
        cliente.domicilio = domicilio
        session.commit()
    else:
        print("El cliente ingresado no existe")
 
def delete(id):
    cliente = session.query(Cliente).filter_by(id = id).first()
    if cliente:
        session.delete(cliente)
        session.commit
    else:
        print("El cliente ingresado no existe")
        
### Evento ###
def getEvento():
    eventos = SessionLocal().query(Evento).all()
    for e in eventos:
        print(f"\nId: {e.id}\nDescripcion: {e.descripcion}\nFecha y Hora: {e.fecha}\nCliente: {e.cliente.nombre}")
        
def save(nombre, telefono, domicilio):
    SessionLocal().query(Cliente).all()
    c = Cliente(nombre = nombre, telefono = telefono, domicilio = domicilio)
    session.add(c)
    session.commit()
    print(f"\nSe agrego el registro {c.nombre}")
 
def update(id, nombre, telefono, domicilio):
    cliente = session.query(Cliente).filter_by(id = id).first()
    if cliente:
        cliente.nombre = nombre
        cliente.telefono = telefono
        cliente.domicilio = domicilio
        session.commit()
    else:
        print("El cliente ingresado no existe")
 
def delete(id):
    cliente = session.query(Cliente).filter_by(id = id).first()
    if cliente:
        session.delete(cliente)
        session.commit
    else:
        print("El cliente ingresado no existe")

def menu_cliente():
    seleccion = input("\nIngrese la operación que desea realizar\nConsultar (1)\nAgregar (2)\nEditar (3)\nEliminar (4)\nTerminar operaciones (5)\n")

    if seleccion == ("1"):
        get()
        getEvento()
    elif seleccion == ("2"):
        nombre = input("Ingrese un nombre: ")
        telefono = input("Ingrese un número de telefono: ")
        domicilio = input("Ingrese un domicilio: ")
        save(nombre, telefono, domicilio)
    elif seleccion == ("3"):
        get()
        id = input("Selecciona un id")
        cliente = session.query(Cliente).filter_by(id = id).first()
        print(f"Está editando el registro: {cliente.id} con nombre {cliente.nombre}")
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        domicilio = input("Domicilio: ")
        update(id, nombre, telefono, domicilio)
    elif seleccion == ("4"):
        get()
        id = input("¿Cual desea eliminar?")
        delete(id)
    elif seleccion == ("5"):
        print("\nGracias por usar el servicio de Ramón: Bases de datos y asociados")
        pass
    else:
        print("Ingrese una opción valida")
        
print("Bienvenido Usuario")



while True:
   menu_cliente()