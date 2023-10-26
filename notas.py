#Programa Básico (c) 2023 Tony Ribeiro

import sqlite3 as db                                                        #Importo la librería de sqlite
import time                                                                 #Importo la librería de tratamiento de fechas

conexion = db.connect("comentarios.sqlite")                                 #Indico el nombre de la base de datos a la que me quiero conectar
cursor = conexion.cursor()                                                  #Creo un cursor
#Sobre el cursor ejecuto una petición para crear una tabla en la base de datos en el caso de que no exista anteriormente
cursor.execute("""
    CREATE TABLE IF NOT EXISTS 'comentarios'(
        'id' INTEGER,
        'texto' TEXT,
        'color' TEXT,
        'fecha' TEXT,
        PRIMARY KEY('id' AUTOINCREMENT)
    );
""")
#Sobre el cursor ejecuto una petición para crear una tabla de usuarios si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS 'usuarios'(
        'id' INTEGER,
        'usuario' TEXT,
        'password' TEXT,
        'email' TEXT,
        PRIMARY KEY('id' AUTOINCREMENT)
    );
""")

#Saludo inicial
print("Soy Tony Ribeiro")                                                   #Autor
print("Estoy programando con Python")                                       #Descripción

class Nota:                                                                 #Declaramos una clase
    def __init__(self,texto,color,fecha):                                   #Método constructor
        self.texto = texto                                                  #Propiedad texto
        self.color = color                                                  #Propiedad color
        self.fecha = fecha                                                  #Propiedad fecha

usuario = "Este es mi primer programa"                                      #Valor inicial de la variable
notas = []                                                                  #Creamos una lista vacía

print("Introduce el usuario")                                               #Pido la evaluación del usuario
usuario = input()                                                           #Introduce la puntuación
print("El usuario es: "+usuario)                                            #Mensaje final

for i in range(0,10):                                                       #Permito al usuario varios comentarios                              
    print("Escribe una recomendación que le harías a mi programa")          #Le pido un segundo comentario
    entrada = input()                                                       #Capturo la entrada del usuario
    print("Introduce el color del comentario")                              #Le pido el color al usuario
    color = input()                                                         #Capturo el color
    #print("Introduce la fecha del comentario")                             #Le pido la fecha al usuario
    fecha = str(int(time.time()))                                           #Capturo la fecha
    if entrada == "finalizar":                                              #Si el usuario escribe "finalizar"
        break                                                               #Salfo del bucle
    else:                                                                   #En caso contrario
        notas.append(Nota(entrada,color,fecha))                             #Añado el segundo comentario
        print("Tu comentario es: ")                                         #Muestro el segundo comentario0

print("Muestro el contenido de todos los cometarios")                       #Muestro los comentarios
for i in notas:                                                             #Para cada una de los comentarios
    print(i.texto)                                                          #Imprimo el comentario
    print(i.color)                                                          #Imprimo el color
    print(i.fecha)                                                          #Imprimo la fecha
    cursor.execute("INSERT INTO comentarios VALUES(NULL,'"+i.texto+"','"+i.color+"','"+i.fecha+"');")#Inserto uno a una las notas en la base de datos
    conexion.commit()                                                       #Ejecuto la inserción
