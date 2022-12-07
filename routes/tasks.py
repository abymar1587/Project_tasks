from fastapi import APIRouter
from config.db import db
from schemas.tasks import tasksEntity
from bson import ObjectId
from models.models import Task #se importa el modelo desde el archivo models.py



tasks = APIRouter()

@tasks.get("/tasks", tags=["Tasks"]) #solo si se tiene un id de usuatio se puden listar
def all_tasks():  
    return tasksEntity(db.tasks.find()) # se llama la funcion creada en schemas para que muestre en 
                                        #localhost:8000 todos los usuarios dque tenga bd 

@tasks.get("/tasks/{idUser}", tags=["Tasks"]) #solo si se tiene un id de usuatio se puden listar
def all_tasks(idUser: str):  
    return tasksEntity(db.tasks.find({"idUser":idUser})) # se llama la funcion creada en schemas para que muestre en 
                                        #localhost:8000 todos los usuarios dque tenga bd 

@tasks.get("/tasks/{id}", tags=["Tasks"])
def an_task(id: str):
    return tasksEntity(db.tasks.find({"_id":ObjectId(id)}))# se llama la funcion creada en schemas 
                                        #para que muestre en localhost:8000 la tarea que corresponda 
                                        # a un determinado id
@tasks.post("/tasks", tags=["Tasks"])  
def add_task(task: Task):
#### se quita las siguientes 2 lineas y se cambian por las dos de arriba para probar agregar datos con vua   
#@tasks.post("/tasks/{idUser}", tags=["Tasks"]) #solo si se tiene un id de usuatio se puden crear taras
#def add_task(idUser: str, task: Task):
    task=dict(task) #convierte task en un diccionario
    ##### se quita la siguiente linea para probar agregar datos con vue
    #task["idUser"] = idUser #agrega el id del usuario a la tarea para que e guarde en la base de dato
    id = db.tasks.insert_one(task).inserted_id #instruccion para agregar a la base de datos
    return tasksEntity(db.tasks.find({"_id":ObjectId(id)}))# se llama la funcion creada en schemas 
                                        #para que muestre en localhost:8000 la tarea que fue añadida

@tasks.put("/tasks/{id}", tags=["Tasks"])
def update_task(id: str, task:Task):
    db.tasks.find_one_and_update(
        {"_id":ObjectId(id)},
        {"$set": dict(task)}
    ) #instruccion para actualizar un registro de collection tasks
    return tasksEntity(db.tasks.find({"_id":ObjectId(id)}))# se llama la funcion creada en schemas 
                                        #para que muestre en localhost:8000 la tarea que fue modificada

@tasks.delete("/tasks/{id}", tags=["Tasks"])
def delete_task(id: str):
    db.tasks.find_one_and_delete({"_id":ObjectId(id)})#instruccion para borrar un registro de collection tasks
    return{"Se ha eliminado correctamente"}

    


