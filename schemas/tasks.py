#schenas se utiliaza para poder mostrar la informacion en laruta 

def taskEntity(task) -> dict:  #task viene desde la base de datos
    return {
        "_id": str(task["_id"]),
        "tittle": task["tittle"],
        "description": task["description"],
        "important": task["important"],
    }

def tasksEntity(tasks) -> dict:
    resultado = []
    for task in tasks:
        resultado.append(taskEntity(task))
    return resultado