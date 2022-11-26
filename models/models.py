from pydantic import BaseModel

class User(BaseModel): #collection users
    user: str
    password: str

class Task(BaseModel): #coooection tasks
    tittle: str
    description: str
    important: bool
