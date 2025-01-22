example

Crear un archivo JSON para almacenar los datos.
Usar Python para manejar las operaciones de CRUD en ese archivo.
Crear un archivo JSON
Primero, crea un archivo data.json que se utilizará para almacenar los datos de las listas. Este archivo debería estar en el mismo directorio que el script de Python.

Crear el script en Python
import json

def cargar_datos():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  

def guardar_datos(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def crear_item(item):
    data = cargar_datos()
    data.append(item)
    guardar_datos(data)

def leer_items():
    data = cargar_datos()
    return data

def actualizar_item(indice, nuevo_item):
    data = cargar_datos()
    if 0 <= indice < len(data):
        data[indice] = nuevo_item
        guardar_datos(data)
    else:
        print("Índice fuera de rango.")

def eliminar_item(indice):
    data = cargar_datos()
    if 0 <= indice < len(data):
        data.pop(indice)
        guardar_datos(data)
    else:
        print("Índice fuera de rango.")




if __name__ == "__main__":

    crear_item({"nombre": "Juan", "edad": 30})
    crear_item({"nombre": "Ana", "edad": 25})

    items = leer_items()
    print("Elementos:", items)

    actualizar_item(1, {"nombre": "Ana", "edad": 26})

    eliminar_item(0)

    items = leer_items()
    print("Elementos después de actualización y eliminación:", items)



Ejemplo de contenido de data.json:

[
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Ana", "edad": 25}
]


Cómo usarlo:
Crear un nuevo elemento: Llama a crear_item({"nombre": "nombre", "edad": edad}).
Leer los elementos: Llama a leer_items(), lo cual devolverá la lista de datos.
Actualizar un elemento: Llama a actualizar_item(indice, {"nombre": "nuevo nombre", "edad": nueva edad}).
Eliminar un elemento: Llama a eliminar_item(indice).
Este es un ejemplo básico. Puedes adaptarlo para realizar validaciones adicionales o para manejar diferentes tipos de datos.


como listar mi json con indices de 1 a x numero, para poder agregarle un input y que al elegirlo se elimine

Para listar los elementos de tu archivo JSON con índices que van del 1 al número total de elementos (en lugar de usar los índices típicos que comienzan en 0), y luego permitir al usuario elegir uno para eliminarlo, puedes modificar el código para que al mostrar los elementos, los indices comiencen en 1. Luego, cuando el usuario elija el número correspondiente, el script eliminará ese elemento.

Paso 1: Modificar la función de lectura para mostrar índices de 1 a x
Primero, cambia la forma en que se muestran los elementos al usuario para que los índices empiecen en 1.

Paso 2: Usar input() para que el usuario elija un índice
Luego, puedes pedirle al usuario que ingrese un número de índice y eliminar el elemento correspondiente.

Aquí tienes el código modificado:


import json

def cargar_datos():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 

def guardar_datos(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def crear_item(item):
    data = cargar_datos()
    data.append(item)
    guardar_datos(data)

def leer_items():
    data = cargar_datos()
    for i, item in enumerate(data, 1):  
        print(f"{i}. {item}")
    return data


def eliminar_item(indice):
    data = cargar_datos()
    if 1 <= indice <= len(data): 
        data.pop(indice - 1)
        guardar_datos(data)
        print(f"Elemento en el índice {indice} ha sido eliminado.")
    else:
        print("Índice fuera de rango.")



if __name__ == "__main__":
    crear_item({"nombre": "Juan", "edad": 30})
    crear_item({"nombre": "Ana", "edad": 25})
    crear_item({"nombre": "Carlos", "edad": 35})

    print("Elementos actuales:")
    leer_items()

    try:
        indice_a_eliminar = int(input("Ingrese el número del elemento que desea eliminar: "))
        eliminar_item(indice_a_eliminar)

        # Mostrar los elementos después de la eliminación
        print("\nElementos después de la eliminación:")
        leer_items()
    except ValueError:
        print("Por favor ingrese un número válido.")
Explicación de los cambios:
enumerate(data, 1): En la función leer_items(), se usa enumerate con el segundo argumento 1 para que los índices comiencen desde 1 en lugar de 0. De esta manera, cuando el usuario vea la lista de elementos, verá algo como:

json
Copiar
1. {"nombre": "Juan", "edad": 30}
2. {"nombre": "Ana", "edad": 25}
3. {"nombre": "Carlos", "edad": 35}
eliminar_item(indice): La función eliminar_item ahora toma el índice proporcionado por el usuario (que es 1-based) y ajusta el índice internamente para eliminar el elemento correcto en la lista (por eso, indice - 1).

input(): Se usa input() para pedir al usuario el índice del elemento que desea eliminar. Luego, se convierte el valor ingresado a un entero con int().

Manejo de excepciones: Se agrega un bloque try-except alrededor del input() para asegurarse de que el usuario ingrese un número válido. Si el usuario ingresa algo que no es un número, se captura el error con ValueError.

Ejemplo de salida:
css
Copiar
Elementos actuales:
1. {'nombre': 'Juan', 'edad': 30}
2. {'nombre': 'Ana', 'edad': 25}
3. {'nombre': 'Carlos', 'edad': 35}

Ingrese el número del elemento que desea eliminar: 2
Elemento en el índice 2 ha sido eliminado.

Elementos después de la eliminación:
1. {'nombre': 'Juan', 'edad': 30}
2. {'nombre': 'Carlos', 'edad': 35}
Nota:
Modificación del archivo JSON: Después de eliminar un elemento, el archivo data.json se actualizará con los cambios.
Validación de índice: El código asegura que el índice ingresado esté dentro del rango de elementos disponibles, evitando errores al intentar acceder a un índice no válido.
