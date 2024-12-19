import json
import os


def guardarArchivo(Diccionario,archivo):
    with open (f"./data/{archivo}.json","w") as salida:
        json.dump(Diccionario, salida)
    return True 

def abrirArchivo(archivo):
    arcPath = f"./data/{archivo}.json"
    
    if not os.path.exists(arcPath):
        print(f"El archivo {arcPath} no existe.")
        return None
    
    with open(arcPath, "r") as entrada:
        nuevoDiccionario = json.load(entrada)
    return nuevoDiccionario


