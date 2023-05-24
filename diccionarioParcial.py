import json

diccionario = {
    'Raza': {
        'Humanos': {
            'Clases': {
                'Guerrero': {
                    'Vida': 100,
                    'Id': 'a',
                    'Ataque': 50,
                    'Defensa': 30,
                    'Poder mágico': 70
                },
                'Jinete': {
                    'Vida': 120,
                    'Id': 'b',
                    'Ataque': 70,
                    'Defensa': 20,
                    'Poder mágico': 40
                },
                'Mago': {
                    'Vida': 80,
                    'Id': 'c',
                    'Ataque': 20,
                    'Defensa': 40,
                    'Poder mágico': 90
                },
                'Recolector': {
                    'Vida': 90,
                    'Id': 'd',
                    'Ataque': 40,
                    'Defensa': 60,
                    'Poder mágico': 10
                },
                'Observador': {
                    'Vida': 70,
                    'Id': 'e',
                    'Ataque': 30,
                    'Defensa': 10,
                    'Poder mágico': 50
                }
            }
        },
        'Orcos': {
            'Clases': {
                'Guerrrero': {
                    'Vida': 80,
                    'Id': 'f',
                    'Ataque': 60,
                    'Defensa': 50,
                    'Poder mágico': 20
                },
                'Chaman': {
                    'Vida': 90,
                    'Id': 'g',
                    'Ataque': 40,
                    'Defensa': 30,
                    'Poder mágico': 60
                },
                'Jinete': {
                    'Vida': 100,
                    'Id': 'h',
                    'Ataque': 70,
                    'Defensa': 40,
                    'Poder mágico': 30
                }
            }
        }
    }
}

#Escribir

archivo = open("diccionario.json","w")

#Guardar Json

json.dump(diccionario,archivo)

#Cerrar el archivo

archivo.close()

# Guardar el diccionario como un archivo JSON
with open('informacion.json', 'w') as archivo:
    json.dump(diccionario, archivo)

# Imprimir el resultado
with open('informacion.json', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
