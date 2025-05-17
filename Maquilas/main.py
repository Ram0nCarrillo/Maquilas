from entities.area import Area
from entities.operador import Operador
from entities.supervisor import Supervisor
from persistence.db import SessionLocal
import datetime

session = SessionLocal()

### Operador ###
def getOperador():
    operadores = SessionLocal().query(Operador).all()
    for o in operadores:
        print(f"\nId: {o.id}\nNombre: {o.nombre}\nSexo: {o.sexo}\nTurno: {o.turno}\nSalario: {o.salario}")
              
def saveOperador(nombre, sexo, turno, salario):
    SessionLocal().query(Operador).all()
    o = Operador(nombre = nombre, sexo = sexo, turno = turno, salario = salario)
    session.add(o)
    session.commit()
    print(f"\nSe agrego el registro {o.nombre}")
 
def updateOperador(id, nombre, sexo, turno, salario):
    operador = session.query(Operador).filter_by(id = id).first()
    if operador:
        operador.nombre = nombre
        operador.sexo = sexo
        operador.turno = turno
        operador.salario = salario
        session.commit()
    else:
        print("El cliente ingresado no existe")
 
def deleteOperador(id):
    operador = session.query(Operador).filter_by(id = id).first()
    if operador:
        session.delete(operador)
        session.commit
    else:
        print("El cliente ingresado no existe")
        
### Area ###
def getArea():
    areas = SessionLocal().query(Area).all()
    for a in areas:
        print(f"\nId: {a.id}\nDepartamento: {a.departamento}\nDescripcion: {a.descripcion}")
        
def saveArea(departamento, descripcion):
    
    SessionLocal().query(Area).all()
    
    a = Area(departamento = departamento, descripcion = descripcion)
    session.add(a)
    session.commit()
    print(f"\nSe creó un nuevo área de trabajo{a.departamento}")
 
def updateArea(id, departamento, descripcion):
    area = session.query(Area).filter_by(id = id).first()
    if area:
        area.departamento = departamento
        area.descripcion = descripcion
        session.commit()
    else:
        print("El cliente ingresado no existe")
 
def deleteArea(id):
    area = session.query(Area).filter_by(id = id).first()
    if area:
        session.delete(area)
        session.commit
    else:
        print("El Area ingresada no existe")

### Supervisor ###
def getSupervisor():
    supervisores = SessionLocal().query(Supervisor).all()
    for s in supervisores:
        print(f"\nId: {s.id}\nNombre: {s.nombre}\nSexo: {s.sexo}\nTurno: {s.turno}\nSalario: {s.salario}\nCorreo: {s.correo}\nTelefono: {s.telefono}")
              
def saveSupervisor(nombre, sexo, turno, salario, correo, telefono):
    SessionLocal().query(Supervisor).all()
    s = Supervisor(nombre = nombre, sexo = sexo, turno = turno, salario = salario, correo = correo, telefono = telefono)
    session.add(s)
    session.commit()
    print(f"\nSe agrego el registro {s.nombre}")
 
def updateSupervisor(id, nombre, sexo, turno, salario, correo, telefono):
    supervisor = session.query(Supervisor).filter_by(id = id).first()
    if supervisor:
        supervisor.nombre = nombre
        supervisor.sexo = sexo
        supervisor.turno = turno
        supervisor.salario = salario
        supervisor.correo = correo
        supervisor.telefono = telefono
        session.commit()
    else:
        print("El cliente ingresado no existe")
 
def deleteSupervisor(id):
    supervisor = session.query(Supervisor).filter_by(id = id).first()
    if supervisor:
        session.delete(supervisor)
        session.commit
    else:
        print("El cliente ingresado no existe")
        
        ### Menu Principal

### Menu principal ###
def menu_principal():
    print("Bienvenido Usuario")
    seleccion = input("\nIngrese la operación que desea realizar\nArea (1)\nOperador (2)\nSupervisor (3)\nCerrar (4)")
    if seleccion == ("1"):
        menu_Area()
    elif seleccion == ("2"):
        menu_Operador()
    elif seleccion == ("3"):
        menu_Supervisor
    elif seleccion == ("4"):
        print("\nGracias por usar el servicio de Ramón: Bases de datos y asociados")
        pass
    else:
        print("Ingresa una opcion valida")
        
### Menu Area ###
def menu_Area():
    seleccion = input("\nIngrese la operación que desea realizar\nConsultar Supervisores (1)\nRegresar a menu (2)\nCerrar (1)")
    if seleccion == ("1"):
        getArea()
    elif seleccion == ("2"):
        menu_principal()
    elif seleccion == ("3"):
        print("\nGracias por usar el servicio de Ramón: Bases de datos y asociados")
        pass
    else:
        print("Ingrese una opción valida")

### Menu Operador ###
def menu_Operador():
    seleccion = input("\nIngrese la operación que desea realizar\nConsultar Operadores (1)\nAgregar Operador (2)\nEditar Operador (3)\nEliminar Operador (4)\nRegresar al menu (5)\nCerrar (6)")
    if seleccion == ("1"):
        getOperador()
        
    elif seleccion == ("2"):
        nombre = input("Ingrese un nombre: ")
        sexo = input("Ingrese el sexo del operador: ")
        turno = input ("Ingrese el turno asignado: ")
        salario = input ("Ingrese el salario asignado: ")
        saveOperador(nombre, sexo, fecha_ingreso, turno, salario)
        
    elif seleccion == ("3"):
        getOperador()
        id = input("Selecciona un id")
        operador = session.query(Operador).filter_by(id = id).first()
        print(f"Está editando el registro: {operador.id} con nombre {operador.nombre}")
        nombre = input("Ingrese un nombre: ")
        sexo = input("Ingrese un número de telefono: ")
        domicilio = input("Ingrese un domicilio: ")
        fecha_ingreso = datetime.now()
        turno = input ("Ingrese el turno asignado: ")
        salario = input ("Ingrese el salario asignado: ")
        updateOperador(id, nombre, sexo, fecha_ingreso, turno, salario)
        
    elif seleccion == ("4"):
        getOperador()
        id = input("¿Cual desea eliminar?")
        deleteOperador(id)
        
    elif seleccion == ("5"):
        menu_principal()
        
    elif seleccion == ("6"):
        print("\nGracias por usar el servicio de Ramón: Bases de datos y asociados")
        pass
    else:
        print("Ingrese una opción valida")
        
### Menu Supervisor ###
def menu_Supervisor():
    seleccion = input("\nIngrese la operación que desea realizar\nConsultar Supervisores (1)\nAgregar Supervisor (2)\nEditar Supervisor (3)\nEliminar Supervisor (4)\nRegresar al menu (5)\nCerrar (6)")
    if seleccion == ("1"):
        getSupervisor()
        
    elif seleccion == ("2"):
        nombre = input("Ingrese un nombre: ")
        sexo = input("Ingrese el sexo del operador: ")
        turno = input("Ingrese el turno asignado: ")
        salario = input("Ingrese el salario asignado: ")
        correo = input("Ingresar el correo: ")
        telefono = input("Ingresar telefono: ")
        saveSupervisor(nombre, sexo, turno, salario, correo, telefono)
        
    elif seleccion == ("3"):
        getSupervisor()
        id = input("Selecciona un id")
        supervisor = session.query(Supervisor).filter_by(id = id).first()
        print(f"Está editando el registro: {supervisor.id} con nombre {supervisor.nombre}")
        nombre = input("Ingrese un nombre nuevo: ")
        sexo = input("Ingrese sexo nuevo: ")
        turno = input("Ingrese el turno nuevo: ")
        salario = input("Ingrese el salario nuevo: ")
        correo = input("Ingresar correo nuevo: ")
        telefono = input("Ingresar nuevo telefono: ")
        updateSupervisor(id, nombre, sexo, turno, salario, correo, telefono)
        
    elif seleccion == ("4"):
        getSupervisor()
        id = input("¿Cual desea eliminar?")
        deleteSupervisor(id)
        
    elif seleccion == ("5"):
        menu_principal()
        
    elif seleccion == ("6"):
        print("\nGracias por usar el servicio de Ramón: Bases de datos y asociados")
        pass
    else:
        print("Ingrese una opción valida")
        
menu_principal()