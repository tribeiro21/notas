#Programa Básico (c) 2023 Tony Ribeiro

#Saludo inicial
print("Soy Tony Ribeiro")                                                   #Autor
print("Estoy programando con Python")                                       #Descripción

class Nota:                                                                 #Declaramos una clase
    def __init__(self,texto,color,fecha):                                   #Método constructor
        self.texto = texto                                                  #Propiedad texto
        self.color = color                                                  #Propiedad color
        self.fecha = fecha                                                  #Propiedad fecha

nota = "Este es mi primer programa"                                         #Valor inicial de la variable
notas = []                                                                  #Creamos una lista vacía

print("Evalúa la calidad de mi primer programa del 1 al 10")                #Pido la evaluación del usuario
nota = input()                                                              #Introduce la puntuación
print("La puntuación que me has dado es: "+nota)                            #Mensaje final

for i in range(0,10):                                                       #Permito al usuario varios comentarios                              
    print("Escribe una segunda recomendación que le harías a mi programa")  #Le pido un segundo comentario
    entrada = input()                                                       #Capturo la entrada del usuario
    print("Introduce el color del comentario")                              #Le pido el color al usuario
    color = input()                                                         #Capturo el color
    print("Introduce la fecha del comentario")                              #Le pido la fecha al usuario
    fecha = input()                                                         #Capturo la fecha
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
