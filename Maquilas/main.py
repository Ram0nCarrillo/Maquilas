from entities.area import Area
from entities.operador import Operador
from entities.supervisor import Supervisor
from persistence.db import SessionLocal
from datetime import datetime

session = SessionLocal()

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
    print(f"\nSe creó una nueva área de trabajo: {a.departamento}")
 
def updateArea(id, departamento, descripcion):
    area = session.query(Area).filter_by(id = id).first()
    if area:
        area.departamento = departamento
        area.descripcion = descripcion
        session.commit()
    else:
        print("El área ingresada no existe")
 
def deleteArea(id):
    area = session.query(Area).filter_by(id = id).first()
    if area:
        session.delete(area)
        session.commit()
        print(f"\nSe eliminó el registro: {area.departamento}")
    else:
        print("El Área ingresada no existe")

### Operador ###
def obtener_operador_por_id(id_operador):
    operador = session.query(Operador).filter_by(id=id_operador).first()
    return operador

def listarAreas():
    areas = session.query(Area).all()
    print("\nÁreas disponibles:")
    for a in areas:
        print(f"ID: {a.id} - Departamento: {a.departamento}")

def listarSupervisores():
    supervisores = session.query(Supervisor).all()
    print("\nSupervisores disponibles:")
    for s in supervisores:
        print(f"ID: {s.id} - Nombre: {s.nombre}")

def getOperador():
    operadores = SessionLocal().query(Operador).all()
    for o in operadores:
        area = o.area.departamento if o.area else "Sin área"
        supervisor = o.supervisor.nombre if o.supervisor else "Sin supervisor"
        print(f"\nId: {o.id}\nNombre: {o.nombre}\nSexo: {o.sexo}\nFecha de ingreso: {o.fecha_ingreso}\nTurno: {o.turno}\nSalario: {o.salario}\nÁrea: {area}\nSupervisor: {supervisor}")
              
def saveOperador(nombre, sexo, fecha_ingreso, turno, salario, id_area, id_supervisor):
    SessionLocal().query(Operador).all()
    o = Operador(nombre = nombre, sexo = sexo,fecha_ingreso = fecha_ingreso, turno = turno, salario = salario,  id_area=int(id_area), id_supervisor=int(id_supervisor))
    session.add(o)
    session.commit()
    print(f"\nSe agregó el operador: {o.nombre}")
 
def updateOperador(id, nombre, sexo, fecha_ingreso, turno, salario, id_area=None, id_supervisor=None):
    operador = session.query(Operador).filter_by(id=id).first()
    if operador:
        operador.nombre = nombre
        operador.sexo = sexo
        operador.fecha_ingreso = fecha_ingreso
        operador.turno = turno
        operador.salario = salario
        if id_area is not None:
            operador.id_area = id_area
        if id_supervisor is not None:
            operador.id_supervisor = id_supervisor
        session.commit()
    else:
        print("El operador ingresado no existe")
 
def deleteOperador(id):
    operador = session.query(Operador).filter_by(id = id).first()
    if operador:
        session.delete(operador)
        session.commit()
        print(f"\nSe eliminó el operador: {operador.nombre}")
    else:
        print("El operador ingresado no existe")

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
    print(f"\nSe agregó el supervisor: {s.nombre}")
 
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
        print("El supervisor ingresado no existe")
 
def deleteSupervisor(id):
    supervisor = session.query(Supervisor).filter_by(id = id).first()
    if supervisor:
        session.delete(supervisor)
        session.commit()
        print(f"\nSe eliminó el supervisor: {supervisor.nombre}")
    else:
        print("El supervisor ingresado no existe")

### Menu principal ###
def menu_principal():
    while True:
        print("\n--------MENÚ PRINCIPAL----------")
        print("\nBIENVENIDO :)")

        print("\n1. Área")
        print("2. Operador")
        print("3. Supervisor")
        print("4. Cerrar") 

        seleccion = input("\nIngrese la operación que desea realizar: ")
        if seleccion == ("1"):
            menu_Area()
        elif seleccion == ("2"):
            menu_Operador()
        elif seleccion == ("3"):
            menu_Supervisor()
        elif seleccion == ("4"):
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Ingrese una opcion valida")
        
### Menu Area ###
def menu_Area():
    while True:
        
        print("\n--------MENÚ DE ÁREAS----------")
        print("\n1. Consultar Áreas")
        print("2. Agregar Área")
        print("3. Editar Área")
        print("4. Eliminar Área") 
        print("5. Regresar al menú principal") 
        print("6. Cerrar")

        seleccion = input("\nIngrese la operación que desea realizar: ")

        if seleccion == "1":
            getArea()
        elif seleccion == "2":
            departamento = input("\nIngrese el nombre del departamento: ")
            descripcion = input("Ingrese una descripción para el área: ")
            saveArea(departamento, descripcion)

        elif seleccion == ("3"):
            getArea()
            try:
                id_area = int(input("\nIngrese el ID del área que desea editar: "))
                area = session.query(Area).filter_by(id=id_area).first()

                if not area:
                    print("No se encontró esa área.")
                    continue

                print("\nDeje en blanco si no desea cambiar un dato.\n")
                nuevo_departamento = input(f"Departamento [{area.departamento}]: ") or area.departamento
                nueva_descripcion = input(f"Descripción [{area.descripcion}]: ") or area.descripcion

                updateArea(id_area, nuevo_departamento, nueva_descripcion)
                print("Área actualizada con éxito.")

            except ValueError:
                print("ID inválido. Intente de nuevo.")

        elif seleccion == ("4"):
            getArea()
            try:
                id_area = int(input("\nIngrese el ID del área que desea eliminar: "))
                area = session.query(Area).filter_by(id=id_area).first()

                if not area:
                    print("No se encontró esa área.")
                    continue

                deleteArea(id_area)
                print("Área eliminada con éxito.")

            except ValueError:
                print("ID inválido. Intente de nuevo.")

        elif seleccion == "5":
            break

        elif seleccion == "6":
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            exit()

        else:
            print("Ingrese una opción válida")

### Menu Operador ###
def menu_Operador():
    while True:

        print("\n--------MENÚ DE OPERADORES----------")
        print("\n1. Consultar Operadores")
        print("2. Agregar Operador")
        print("3. Editar Operador")
        print("4. Eliminar Operador") 
        print("5. Regresar al menú principal") 
        print("6. Cerrar")
        seleccion = input("\nIngrese la operación que desea realizar: ")
    
    
        if seleccion == ("1"):
            getOperador()
        
        elif seleccion == ("2"):
            nombre = input("\nIngrese el nombre: ")
            sexo = input("Ingrese el sexo del operador(M/F): ")
            fecha_input = input("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
            try:
                fecha_ingreso = datetime.strptime(fecha_input, "%Y-%m-%d").date()
            except ValueError:
                print("Fecha inválida. Use el formato YYYY-MM-DD.")
                return
        
            turno = input ("Ingrese el turno asignado: ")
            salario = input ("Ingrese el salario asignado: ")
            listarAreas()
            id_area = input("Ingrese el id del área a la que pertenece: ")
            listarSupervisores()
            id_supervisor = input("Ingrese el id del supervisor: ")

        
            saveOperador(nombre, sexo, fecha_ingreso, turno, salario, id_area, id_supervisor)
        
        elif seleccion == ("3"):
            operadores = session.query(Operador).all()

            print("\nLista de operadores:")
            for op in operadores:
                print(f"{op.id}: {op.nombre}")

            try:
                id_op = int(input("\nIngrese el ID del operador que desea editar: "))
                operador = session.query(Operador).filter_by(id=id_op).first()

                if not operador:
                    print("No se encontró ese operador.")
                    return

                print("\nDeje en blanco si no deseas cambiar un dato.\n")

                nuevo_nombre = input(f"Nombre [{operador.nombre}]: ") or operador.nombre
                nuevo_sexo = input(f"Sexo [{operador.sexo}]: ") or operador.sexo
                nueva_fecha = input(f"Fecha de ingreso (YYYY-MM-DD) [{operador.fecha_ingreso}]: ") or str(operador.fecha_ingreso)
                nuevo_turno = input(f"Turno [{operador.turno}]: ") or operador.turno
                nuevo_salario = input(f"Salario [{operador.salario}]: ") or str(operador.salario)

                listarAreas()
                id_area_input = input(f"ID Área [{operador.id_area}]: ")

                listarSupervisores()
                id_supervisor_input = input(f"ID Supervisor [{operador.id_supervisor}]: ")

                fecha_dt = datetime.strptime(nueva_fecha, "%Y-%m-%d").date()
                salario_float = float(nuevo_salario)

                id_area = int(id_area_input) if id_area_input.strip() else None
                id_supervisor = int(id_supervisor_input) if id_supervisor_input.strip() else None

                updateOperador(id_op, nuevo_nombre, nuevo_sexo, fecha_dt, nuevo_turno, salario_float, id_area, id_supervisor)
                print("Operador actualizado con éxito.")

            except ValueError as e:
                print("Entrada no válida. Asegúrese de ingresar valores correctos.")
                print(f"Detalles del error: {e}")
            
        elif seleccion == ("4"):
            getOperador()
            try:
                id_op = int(input("\nIngrese el ID del operador que desea eliminar: "))
                operador = session.query(Operador).filter_by(id=id_op).first()

                if not operador:
                    print("No se encontró ese operador.")
                    continue

                deleteOperador(id_op)
                print("Operador eliminado con éxito.")

            except ValueError:
                print("ID inválido. Intente de nuevo.")
        
        elif seleccion == ("5"):
            menu_principal()
        
        elif seleccion == "6":
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            exit()

        else:
            print("Ingrese una opción valida")

### Menu Supervisor ###
def menu_Supervisor():
    while True:

        print("\n--------MENÚ DE SUPERVISORES----------")
        print("\n1. Consultar Supervisores")
        print("2. Agregar Supervisores")
        print("3. Editar Supervisores")
        print("4. Eliminar Supervisores") 
        print("5. Regresar al menú principal") 
        print("6. Cerrar")
        seleccion = input("\nIngrese la operación que desea realizar: ")
    
        if seleccion == ("1"):
            getSupervisor()
        
        elif seleccion == ("2"):
            nombre = input("\nIngrese un nombre: ")
            sexo = input("Ingrese el sexo del supervidor(M/F): ")
            turno = input("Ingrese el turno asignado: ")
            salario = input("Ingrese el salario asignado: ")
            correo = input("Ingrese el correo: ")
            telefono = input("Ingrese el telefono: ")
            saveSupervisor(nombre, sexo, turno, salario, correo, telefono)
        
        elif seleccion == ("3"):
            getSupervisor()
            try:
                id_sup = int(input("\nIngrese el ID del supervisor que desea editar: "))
                supervisor = session.query(Supervisor).filter_by(id=id_sup).first()

                if not supervisor:
                    print("No se encontró ese supervisor.")
                    continue

                print("\nDeje en blanco si no deseas cambiar un dato.\n")
                nuevo_nombre = input(f"Nombre [{supervisor.nombre}]: ") or supervisor.nombre
                nuevo_sexo = input(f"Sexo [{supervisor.sexo}]: ") or supervisor.sexo
                nuevo_turno = input(f"Turno [{supervisor.turno}]: ") or supervisor.turno

                nuevo_salario_input = input(f"Salario [{supervisor.salario}]: ")
                nuevo_salario = float(nuevo_salario_input) if nuevo_salario_input.strip() else supervisor.salario

                nuevo_correo = input(f"Correo [{supervisor.correo}]: ") or supervisor.correo
                nuevo_telefono = input(f"Teléfono [{supervisor.telefono}]: ") or supervisor.telefono

                updateSupervisor(id_sup, nuevo_nombre, nuevo_sexo, nuevo_turno, nuevo_salario, nuevo_correo, nuevo_telefono)
                print("Supervisor actualizado con éxito.")

            except ValueError:
                print("Entrada inválida. Intente de nuevo.")
        
        elif seleccion == ("4"):
            getSupervisor()
            try:
                id_sup = int(input("\nIngrese el ID del supervisor que desea eliminar: "))
                supervisor = session.query(Supervisor).filter_by(id=id_sup).first()

                if not supervisor:
                    print("No se encontró ese supervisor.")
                    continue

                deleteSupervisor(id_sup)
                print("Supervisor eliminado con éxito.")

            except ValueError:
                print("ID inválido. Intente de nuevo.")
        
        elif seleccion == ("5"):
            menu_principal()
        
        elif seleccion == ("6"):
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            exit()
        else:
            print("Ingrese una opción valida")
        
menu_principal()