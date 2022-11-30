from fastapi import FastAPI
from routes.users import users
from routes.tasks import tasks

app = FastAPI(
    tittle="Aplicacion FastAPI con MongoDB - Lita de tareas",
    description="Esta es una aplicacion donde se va a hacer una API REST en la que se registren usuarios y cada usuario registrado puede ingresar una lista de tareas a realizar con su titulo descripcion y sies importante o no",
)

app.include_router(users)

app.include_router(tasks)



