#schenas se utiliaza para poder mostrar la informacion en laruta 

def taskEntity(task) -> dict:  #task viene desde la base de datos
    return {
        "_id": str(task["_id"]),
        "tittle": task["tittle"],
        "description": task["description"],
        "important": task["important"], # se quito apra robar si funciona agregar datos con vue
        "idUser": task["idUser"], #se quito apra robar si funciona agregar datos con vue
    }

def tasksEntity(tasks) -> dict:
    resultado = []
    for task in tasks:                    
        resultado.append(taskEntity(task))
    return resultado
    
    #codigo para que no se visualice el id de usuario
    #result=[] 
    #for item in resultado:
    #    del item["idUser"]
    #    result.append(item)      
    #return result
    