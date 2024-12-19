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

planesInfo = abrirArchivo("planesData")
clientesInfo = abrirArchivo("clientesData")

def crearCliente(clienteData: dict):
    doc = int(input('Ingrese el Numero de Documento: '))
    docStr = str(doc)
    if docStr not in clienteData["clientes"]:
        name = input('Ingrese nombre: ')
        direccion = input('Ingrese direccion: ')
        telefono = int(input('Ingrese telefono: '))
        planes_list = [
            {"id": int(id_plan), "nombre": plan['nombre']}
            for id_plan, plan in planesInfo.items()
        ]
        print('Lista de planes:')
        for index, plan in enumerate(planes_list):
            print(f"{index+1}. Nombre: {plan['nombre']}")

        while True:
            seleccion = int(input('Seleccione el indice del plan para el Usuario'))
            if 0 <= (seleccion-1) < len(planes_list):
                planElegido = planes_list[seleccion-1]
                break
            else:
                input('Indice fuera de rango, elija nuevamente...')
                os.system('clear')

        clientesInfo["clientes"][doc] = {
            "nombre": name,
            "direccion": direccion,
            "telefono": telefono,
            "plan": planElegido
        }

        guardarArchivo(clientesInfo, "clientesData")
        abrirArchivo("clientesData")
        print(f"El usuario con documento {doc} ha sido creado...")
        input('')
        os.system('clear')
    else:
        print(f"El número de documento {doc} ya se encuentra registrado.")
        input('')
        os.system('clear')


def eliminarCliente(clienteData: dict):

    clientes_list =[
        {"id": int(id_cli), "nombre": cliente['nombre']}
        for id_cli, cliente in clientesInfo.items()
    ]
    
    print("Lista de clientes: ")
    for index, cliente in enumerate(clientes_list):
        print(f"{index+1}. Nombre: {cliente['nombre']}")
    
    while True:
        seleccion = int(input('Seleccione el indice del usuario a eliminar'))
        if 0 <= (seleccion-1) < len(clientes_list):
            clienteElegido = clientes_list[seleccion-1]
            if (str(clienteElegido['id']) in clienteData):
                clienteData.pop(clienteElegido)
                guardarArchivo(clientesInfo, "clientesData")
                abrirArchivo("clientesData")
                break
        else:
            input('Indice fuera de rango, elija nuevamente...')
            os.system('clear')


def editarCliente(clienteData: dict):
    clientes_list =[
        {"id": int(id_cli), "nombre": cliente['nombre']}
        for id_cli, cliente in clientesInfo.items()
    ]
    
    print("Lista de clientes: ")
    for index, cliente in enumerate(clientes_list):
        print(f"{index+1}. Nombre: {cliente['nombre']}")
    
    while True:
        seleccion = int(input('Seleccione el indice del usuario a eliminar'))
        if 0 <= (seleccion-1) < len(clientes_list):
            clienteElegido = clientes_list[seleccion-1]