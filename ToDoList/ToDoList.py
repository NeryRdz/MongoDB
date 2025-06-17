from pymongo import MongoClient         #Install pymongo in terminal
from datetime import datetime

class ToDoList():

    def CrearTarea(self,titulo: str,descripcion: str):
        if coltarea.find_one({'titulo':{'$eq':titulo}}):
                    print("No puedes repetir los titulos de las tareas")
                    return
        
        tarea = {
            'titulo' : titulo,
            'descripcion': descripcion,
            'completada': "Pendiente",
            'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'fecha_completada': 'No completada'
        }

        coltarea.insert_one(tarea)
        print("Tarea Creada")

    def VerTareas(self):
        if  coltarea.count_documents({}) == 0:
            print("No hay tareas actualmente")
            return

        tareas = coltarea.find({})

        opcion = int(input("Selecciona una opcion:\n1. Ver todas la tareas\n2. Buscar una tarea por su titulo\nTu opcion: "))

        if opcion == 1:
            for index, tarea in enumerate(tareas,1):
                print(f"""
-------- Tarea {index} --------
Titulo: {tarea['titulo']}
Descripcion: {tarea['descripcion']}
Completada: {tarea['completada']}
Fecha de creacion: {tarea['fecha_creacion']}
Fecha completada: {tarea['fecha_completada']}
--------------------------------""")
                
        elif opcion == 2:
            titulo = input("Selecciona por titulo la tarea que quieras buscar: ")

            tarea = coltarea.find_one({'titulo':titulo})

            if not tarea:
                print("Tarea no encontrada")
                return

            print(f"""
-------- Tarea Encontrada --------
Titulo: {tarea['titulo']}
Descripcion: {tarea['descripcion']}
Completada: {tarea['completada']}
Fecha de creacion: {tarea['fecha_creacion']}
Fecha completada: {tarea['fecha_completada']}
--------------------------------""")

        else:
            print("Escoge una opcion valida")

        
            
    def ActualizarTareas(self):
        titulo = input("Selecciona por titulo la tarea que quieras actualizar: ")

        if not coltarea.find_one({'titulo':titulo}):
            print("Tarea no encontrada")
            return
        
        opcion = int(input("¿Que deseas realizar?\n1. Marcar como completada\n2. Editar titulo\n3. Editar descripcion\n4. Salir\nTu opcion: "))
        if opcion == 1:
            if coltarea.find_one({'$and':[{'titulo':titulo},{'completada':{'$eq':"Completo"}}]}):
                print("Esta tarea ya esta marcada como completada. No se han realizado cambios")
                return

            coltarea.update_one({'titulo':titulo},{'$set':{'completada':"Completo",'fecha_completada':datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})
            print("Tarea marcada como completada.\n")

        elif opcion == 2:
            nuevoti = input("Ingresa el nuevo titulo de la tarea: ")
            coltarea.update_one({'titulo':titulo},{'$set':{'titulo':nuevoti}})
            print("Titulo cambiado exitosamente\n")

        elif opcion == 3:
            nuevadesc = input("Ingresa la nueva descripcion de la tarea: ")
            coltarea.update_one({'titulo':titulo},{'$set':{'descripcion':nuevadesc}})
            print("Descripcion cambiada exitosamente\n")

        elif opcion == 4:
            return
        else:
            print("Escoge una opcion valida\n")

        
    def EliminarTareas(self):
        titulo = input("Selecciona por titulo la tarea que quieras eliminar: ")
        if not coltarea.find_one({'titulo':titulo}):
            print("Tarea no encontrada")
            return
        
        coltarea.delete_one({'titulo':titulo})
        print("Tarea eliminada exitosamente\n")

    def terminal(self):
        while True:
            print("------------------------ Gestor de Tareas ------------------------")
            opcion = int(input("Selecciona una opcion: \n1. Crear tarea\n2. Ver Tareas\n3. Actualizar tarea\n4. Eliminar tarea\n5. Salir\nTu opcion: "))
            if opcion == 1:
                print("------------------------ Crear Tarea ------------------------")
                titulo = input("Ingresa el titulo de tu tarea: ")
                descripcion = input("Ingresa una descripcion a la tarea: ")
                tdl.CrearTarea(titulo,descripcion)

            elif opcion == 2:
                print("------------------------ Ver Tareas ------------------------")
                tdl.VerTareas()
                

            elif opcion == 3:
                print("------------------------ Actualizar Tarea ------------------------")
                tdl.ActualizarTareas()
                

            elif opcion == 4:
                print("------------------------ Eliminar Tarea ------------------------")
                tdl.EliminarTareas()
                
            elif opcion == 5:
                break
            else:
                print("\nIngresa una opcion valida\n")

try:
    client = MongoClient('mongodb://localhost:27017/')          

    db = client['ToDoList2']                               

    coltarea = db['Tarea']                              

    tdl = ToDoList()

    tdl.terminal()

except Exception as ex:
    print("Error: {}".format(ex))
finally:
    client.close()
    print("Gracias por usar el programa.")
    print("Conexion finalizada")