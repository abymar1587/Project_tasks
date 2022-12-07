from pydantic import BaseModel

class User(BaseModel): #collection users
    user: str
    password: str
    confirmPassword: str

class Task(BaseModel): #coooection tasks
    tittle: str
    description: str
    important: bool #se quita esta instruccion para probar agregar datos con vue
    idUser: str
