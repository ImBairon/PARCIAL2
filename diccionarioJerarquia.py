import json

diccionario1 = {
    "House Stark": {
        "Ricckard": {
            "Benjen": {},
            "brandon": {},
            "lyanna": {},
            "wylla": {},
            "Eddard & Catelyn": {
                "robb": {
                    "animal": "Grey Wind"
                },
                "sansa": {
                    "animal": "Lady"
                },
                "arya": {
                    "animal": "Nymeria"
                },
                "bran": {
                    "animal": "Summer"
                },
                "rickon": {
                    "animal": "Shaggydog"
                }
            }
        }
    },
    "House Tully": {
        "Hoster": {
            "relacion": "Robin",
            "catelyn": {},
            "lysa": {},
            "edmure": {}
        }
    }
}

#Escribir

archivo = open("diccionario.json","w")

#Guardar Json

json.dump(diccionario1,archivo)

#Cerrar el archivo

archivo.close()

# Guardar el diccionario como un archivo JSON
with open('informacion.json', 'w') as archivo:
    json.dump(diccionario1, archivo)

# Imprimir el resultado
with open('informacion.json', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)



#Obtener descendencia House Stark


def obtener_descendencia(diccionario, casa, nivel=0):
    if casa in diccionario:
        descendencia = diccionario1[casa]
        print("  " * nivel + "- " + casa)
        mostrar_descendencia(descendencia, nivel + 1)

def mostrar_descendencia(diccionario1, nivel):
    for nombre, descendencia in diccionario1.items():
        if isinstance(descendencia, dict) and descendencia:
            print("  " * nivel + "- " + nombre)
            mostrar_descendencia(descendencia, nivel + 1)
        else:
            print("  " * nivel + "- " + nombre)

obtener_descendencia(diccionario1, "House Stark")

#Listar Personajes


def listar_personajes(diccionario1, familia):
    if familia in diccionario1:
        personajes = obtener_personajes(diccionario1[familia])
        if personajes:
            print(f"Personajes de la familia {familia}:")
            for personaje in personajes:
                print("- " + personaje)

def obtener_personajes(diccionario1):
    personajes = []
    for nombre, descendencia in diccionario1.items():
        if descendencia:
            personajes.append(nombre)
            if isinstance(descendencia, dict):
                personajes.extend(obtener_personajes(descendencia))
    return personajes

listar_personajes(diccionario1, "House Stark")


#Agregar CasaNueva

diccionario1["CasaNueva1"] = "TYRELL"
diccionario1["CasaNueva2"] = "UNISANGIL"

#Agregar personaje 
diccionario1["PersonajeNuevo"] = "Bairon Diaz"
diccionario1["PersonajeNuevo"] = "Brandon Gomez"
diccionario1["PersonajeNuevo"] = "TYRION"

#Cambiar de TYRIOS A TYRION KING
diccionario1["Tyron"] = None
print(diccionario1)

diccionario1["Tyron"] = "Tyron King"
print(diccionario1)
#Eliminar Casa TYRELL

del diccionario1["CasaNueva1"]
print(diccionario1)
