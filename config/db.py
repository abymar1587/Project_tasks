from pymongo import MongoClient

mongodb_url = "mongodb+srv://aumanuca:MongoDB123*@cluster0.ove6sx3.mongodb.net/?retryWrites=true&w=majority"
port = 8000

conn = MongoClient(mongodb_url, port)
db =conn["tasks"]  # la base de datos tasks tiene dos colecciones: tasks y users