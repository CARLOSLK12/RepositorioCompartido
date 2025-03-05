'''
    1. Tabla de Multiplicar del 1 al 10


    for x in range(1, 11):
        print(x, " x ", 10, " = ", x*10)
'''



'''
    ----------------------
    EJERCICIOS INTERMEDIOS
    ----------------------

    1. Suma de números del 1 al N: Pide un número N al usuario y calcula la suma de los números del 1 al N.

    
numero = int(input("ingresar un numero: "))
contador = 0
for x in range(1, numero+1):
    contador = contador + x
    print(f"la suma de los numeros del 1 al {numero} es: {contador}")
'''

"""
#conatar cuantas letras tiene un texto.

texto = "Este es un texto en el que se puede descubrir todos los demas temas de conversacion de el bucle for"
contador_palabras = 0
letter = input("Ingresar letra: ")
for x in texto:
    if x != " ":
        if x == letter:
            contador_palabras += 1
print(f"Se ha encontrado {contador_palabras} veces la letra {letter}")

"""
"""
# Dada una lista de números, usa un bucle for para sumar todos sus elementos.

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
suma = 0
for x in lista_numeros: 
    suma = suma + x
    print(f"la suma es: {suma}")

"""

"""
# verificar si un numero se encuentra en una lista

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
buscarNumero = int(input("ingrese numero: "))
for x in lista_numeros:
    if buscarNumero == x:
        print("El numero se encuentra en la lista")
    else:
        continue
    
"""

# Dada una lista de palabras y un número 𝑁, usa un bucle for para mostrar solo las palabras cuya longitud sea mayor o igual a N.

lista_palabras = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
n = int(input("Ingresa el numero N: "))

for x in lista_palabras:    
    if len(x) >= n:
        print(f"las palabras son: {x}")
