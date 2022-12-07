from fastapi import FastAPI
from routes.users import users
from routes.tasks import tasks
from fastapi.middleware.cors import CORSMiddleware #conxion con vue

app = FastAPI(
    tittle="Aplicacion FastAPI con MongoDB - Lita de tareas",
    description="Esta es una aplicacion donde se va a hacer una API REST en la que se registren usuarios y cada usuario registrado puede ingresar una lista de tareas a realizar con su titulo descripcion y sies importante o no",
)

#conxion con vue
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(users)

app.include_router(tasks)



