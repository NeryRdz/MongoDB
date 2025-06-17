from pymongo import MongoClient
from pymongo import ASCENDING,DESCENDING
from datetime import datetime

# Requires the PyMongo package.
# https://api.mongodb.com/python/current
try:
    client = MongoClient('mongodb://localhost:27017/')          #Conexion a mongodb

    db = client['PruebaDeConexion']                               #Sentencia para crear la base de datos

    collection = db['Tarea']                              #Crear una coleccion

    documents = collection.find()                         #Recuperar los documentos

    
    #Insertar documento a una coleccion
    collection.insert_one({
        'titulo': 'Matematicas',
        'descripcion': 'Ecuaciones',
        'completada': True,
        'fecha_creacion': datetime.now(),
        'fecha_completada': '22/22/2222',
        'prueba': 10
    })

    #Ver todas las bases de datos
    print("Bases de datos:")
    print(client.list_database_names())

    #Ver las colecciones de la base de datos
    print(f"Coleccion(es) de la base de datos {db.name}:")
    print(db.list_collection_names())                       

    #Contar los documentos
    print(f"Cantidad de documento(s) de la coleccion {collection.name}:")
    print(collection.count_documents({}))             

    #Mostrar todos los documentos      
    print(f"Documentos de la coleccion {collection.name}:")
    for documento in collection.find({}):                   
        print (documento)   

    #Borrar documento
    collection.delete_one({                                 
        "completada":False              
    })

    #Actualizar documento
    collection.update_one({                                 
        "completada":True
    },{
        "$set":{
            "completada":False
        }
    })

    #Indice
    collection.create_index([{'prueba',ASCENDING}])

    #Borrar coleccion
    #db.drop_collection('Tarea')

    #Borrar Base de Datos
    #client.drop_database('ToDoList')

except Exception as ex:
    print("Error durante la conexion: {}".format(ex))
finally:
    client.close()
    print("Conexion finalizada")