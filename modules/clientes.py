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
    doc = int(input('Ingrese el Número de Documento: '))
    docStr = str(doc) 

    if docStr in clienteData:
        print(f"El número de documento {doc} ya se encuentra registrado.")
        input('Presione Enter para continuar...')
        os.system('clear')
        return 

    name = input('Ingrese nombre: ')
    direccion = input('Ingrese dirección: ')
    telefono = int(input('Ingrese teléfono: '))

    planes_list = [
        {"id": int(id_plan), "nombre": plan['nombre']}
        for id_plan, plan in planesInfo.items()
    ]
    print('Lista de planes:')
    for index, plan in enumerate(planes_list):
        print(f"{index+1}. Nombre: {plan['nombre']}")

    while True:
        try:
            seleccion = int(input('Seleccione el índice del plan para el usuario: '))
            if 1 <= seleccion <= len(planes_list):
                planElegido = planes_list[seleccion - 1]
                break
            else:
                print('Índice fuera de rango, elija nuevamente...')
        except ValueError:
            print('Por favor, ingrese un número válido.')

    clienteData[docStr] = {
        "nombre": name,
        "direccion": direccion,
        "telefono": telefono,
        "plan": planElegido
    }

    guardarArchivo(clienteData, "clientesData")
    print(f"El usuario con documento {doc} ha sido creado exitosamente.")
    input('Presione Enter para continuar...')
    os.system('clear')



def listarClientes(clienteData: dict) -> list:
    clientes_list = [
        {"id": int(id_cli), "nombre": cliente['nombre']}
        for id_cli, cliente in clienteData.items()
    ]
    
    print("Lista de clientes:")
    for index, cliente in enumerate(clientes_list):
        print(f"{index+1}. Nombre: {cliente['nombre']} (ID: {cliente['id']})")
    
    return clientes_list


def eliminarCliente(clienteData: dict):
    clientes_list = listarClientes(clienteData)
    
    while True:
        try:
            seleccion = int(input('Seleccione el índice del usuario a eliminar: '))
            if 1 <= seleccion <= len(clientes_list):
                clienteElegido = clientes_list[seleccion - 1]
                cliente_id = str(clienteElegido['id'])
                
                if cliente_id in clienteData:
                    clienteData.pop(cliente_id)
                    guardarArchivo(clienteData, "clientesData")
                    print(f"Cliente {clienteElegido['nombre']} eliminado correctamente.")
                    break
                else:
                    print("El cliente seleccionado no existe en los datos.")
            else:
                print("Índice fuera de rango, elija nuevamente...")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")


def editarCliente(clienteData: dict):
    clientes_list = listarClientes(clienteData)
    
    while True:
        try:
            seleccion = int(input('Seleccione el índice del usuario a editar: '))
            if 1 <= seleccion <= len(clientes_list):
                clienteElegido = clientes_list[seleccion - 1]
                cliente_id = str(clienteElegido['id'])
                cliente_actual = clienteData[cliente_id]

                print(f"Seleccionaste al cliente: {cliente_actual['nombre']}")
                print("Campos disponibles para editar: ")
                print("1. Nombre")
                print("2. Dirección")
                print("3. Teléfono")
                print("4. Plan")

                campo = int(input("Seleccione el campo que desea editar: "))
                if campo == 1:
                    nuevo_valor = input("Ingrese el nuevo nombre: ")
                    cliente_actual['nombre'] = nuevo_valor
                elif campo == 2:
                    nuevo_valor = input("Ingrese la nueva dirección: ")
                    cliente_actual['direccion'] = nuevo_valor
                elif campo == 3:
                    nuevo_valor = input("Ingrese el nuevo teléfono: ")
                    cliente_actual['telefono'] = int(nuevo_valor)
                elif campo == 4:
                    nuevo_nombre_plan = input("Ingrese el nuevo nombre del plan: ")
                    nuevo_id_plan = int(input("Ingrese el nuevo ID del plan: "))
                    cliente_actual['plan']['nombre'] = nuevo_nombre_plan
                    cliente_actual['plan']['id'] = nuevo_id_plan
                else:
                    print("Campo no válido.")
                    continue

                # Guardar los cambios en el archivo
                guardarArchivo(clienteData, "clientesData")
                print(f"Cliente actualizado: {cliente_actual}")
                break
            else:
                print("Índice fuera de rango, elija nuevamente...")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
