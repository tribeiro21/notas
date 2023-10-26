#Programa Básico (c) 2023 Tony Ribeiro

#Saludo inicial
print("Soy Tony Ribeiro")                                               #Autor
print("Estoy programando con Python")                                   #Descripción

nota = "Este es mi primer programa"                                     #Valor inicial de la variable
notas = []

print("Evalúa la calidad de mi primer programa del 1 al 10")            #Pido la evaluación del usuario
nota = input()                                                          #Introduce la puntuación
print("La puntuación que me has dado es: "+nota)                        #Mensaje final

print("Escribe una recomendación que le harías a mi programa")          #Le pido un comentario al usuario
notas.append(input())                                                   #Añado un comentario vacío
print("Tu comentario es: "+notas[0])                                    #Muestro el comentario

for i in range(0,10):
    print("Escribe una segunda recomendación que le harías a mi programa")  #Le pido un segundo comentario
    notas.append(input())                                                   #Añadp el segundo comentario
    print("Tu comentario es: ")                                             #Muestro el segundo comentario
    print(notas)
