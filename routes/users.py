from fastapi import APIRouter
from config.db import db
from schemas.users import usersEntity
from bson import ObjectId
from models.models import User #se importa el modelo desde el archivo models.py

users = APIRouter()

@users.get("/users/{user}/{password}", tags=["Users"]) #se piden como parametros usuario y contraeña si ya se
                                                        # ha creado un ususario para el ingreso al CRUD de tareas
def log_in(user:str,password:str):
    if usersEntity(db.users.find({"user":user})):#si el "user" ingresado corresponde a algun "user" en la bae de datos     
        user=(usersEntity(db.users.find({"user":user}))[0]) #se saca el diccionario de la lista(eta lita solo tiene un valor que es el diccioario)
        if user["password"] == password: #se confirma si la contraseña ingresada es la misma de la bd
            return ("idUser: " + user["_id"]) #si es asi de devulv el id del usuario para usarlo en el CRUD de tast
        else:
            return("Contraseña errada") #de lo contrario sale el mensaje de contraseña errada
    else:
        return("Usted no se encuentra registrado")
    

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
    #print(dict(user))
    if usersEntity(db.users.find({"user":dict(user)["user"]})): #verifica si ya exite "user" en la bd
        return ("Ya se han regitrado con este nombre de usuario")
    elif dict(user)["password"] == dict(user)["confirmPassword"]: #confirmacion de la contraeña
        id = db.users.insert_one(dict(user)).inserted_id #instruccion para agregar a la base de datos
        #print(type(id))
        #print(type(ObjectId(id)))
        return usersEntity(db.users.find({"_id":id})) # se llama la funcion creada en schemas 
                                        #para que muestre en localhost:8000 el usuario que fue añadido
    else:
        return ("las contraseñas no concuerdan")   

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

    


