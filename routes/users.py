from fastapi import APIRouter
from config.db import db
from schemas.users import usersEntity
from bson import ObjectId
from models.models import User #se importa el modelo desde el archivo models.py

users = APIRouter()

@users.get("/users", tags=["Users"])
def all_users():  
    return usersEntity(db.users.find()) # se llama la funcion creada en schemas para que muestra en 
                                        #localhost:8000 todos los usuarios dque tenga bd 

@users.get("/users/{id}", tags=["Users"])
def an_user(id: str):
    return usersEntity(db.users.find({"_id":ObjectId(id)}))# se llama la funcion creada en schemas 
                                        #para que muestra en localhost:8000 el usuario que corresponda 
                                        # a un determinado id
      
@users.post("/users", tags=["Users"])
def add_user(user: User):
    id = db.users.insert_one(dict(user)).inserted_id #instruccion para agregar a la base de datos
    return usersEntity(db.users.find({"_id":ObjectId(id)})) # se llama la funcion creada en schemas 
                                        #para que muestre en localhost:8000 el usuario que fue añadido

@users.put("/users/{id}", tags=["Users"])
def update_user(id: str, user:User):
    db.users.find_one_and_update(
        {"_id":ObjectId(id)},
        {"$set": dict(user)}
    ) #instruccion para actualizar un registro de collection tasks
    return usersEntity(db.users.find({"_id":ObjectId(id)})) # se llama la funcion creada en schemas 
                                        #para que muestre en localhost:8000 el usuario que fue modificado

@users.delete("/users/{id}", tags=["Users"])
def delete_user(id: str):
    db.users.find_one_and_delete({"_id":ObjectId(id)}) #instruccion para borrar un registro de collection userx
    return{"Se ha eliminado correctamente"}

    


