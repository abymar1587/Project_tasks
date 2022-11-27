#schenas se utiliaza para poder mostrar la informacion en laruta 

def userEntity(user) -> dict:  #user viene desde la base de datos
    return {
        "_id": str(user["_id"]),
        "user": user["user"],
        "password": user["password"],
       # "confirmPassword": user["confirmPassword"],
    }

def usersEntity(users) -> dict:
    resultado = []
    for user in users:
        resultado.append(userEntity(user))
    return resultado