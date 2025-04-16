#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101):
    print(str(i) + " ", end="")

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un número entero: "))
print("El numero ingresado tiene " + str(len(str(num))) + " digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

inicio = min(num1, num2) +1
fin = max(num1, num2)

suma = 0
for i in range(inicio, fin):
    suma += i

print(f"La suma de los numeros {num1} y {num2}, es {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

numero = int(input("Ingrese un numero entero (0 para terminar): " ))
suma = 0

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un numero entero (0 para terminar): " ))

print(f"La suma de los numero es: {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

num_escondido = random.randint(1,10) #Devuelve un número entero aleatorio entre a y b (ambos inclusive).

intentos = 0
adivinar = 0

print("Juego: Adivinar el numero escondido")

while adivinar != num_escondido:
    adivinar = int(input("Ingrese un numero entre el 0 y el 10: "))
    intentos += 1

print(f"Adivinaste! El numero secreto era {num_escondido}")
print(f"Los intentos fueron {intentos}")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 

#ESTO  NOOOOOOOOOOO
# for numero in range(101,0, -1):
#    if numero > 0:
#       if numero % 2 != 0:
#            numero = numero - 1
#        cont = numero
#        while cont >= 0:
#            print(str(cont) + " ", end="")
#            cont = cont - 2

for numero in range(100, -1, -2):
    print(numero, end=" ")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

numero = int(input("Ingrese un numero positivo: "))

if numero < 0:
    print("El numero debe ser positivo")
else:
    suma = 0
    cont = 0

    while cont <= numero:
        suma += cont
        cont += 1
    print(f"La suma de los numeros entre 0 y {numero} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cant_numeros = 10
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {cant_numeros} numeros enteros: ")
for i in range(cant_numeros):
    numero= int(input(f"Numero {i+1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero >0:
        positivos +=1
    elif numero <0:
        negativos +=1

print("Los numeros pares: {pares}")
print("Los numeros impares: {impares}")
print("Los numeros positivos: {positivos}")
print("Los numeros negativos: {negativos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

cant_numeros = 10
suma_total = 0

print(f"Ingrese {cant_numeros} numeros enteros: ")
for i in range(cant_numeros):
    numero = int(input(f"Numero {i+1}: "))
    suma_total += numero

media = suma_total / cant_numeros
print(f"La media de los {cant_numeros} numeros ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = ("Ingrese un numero de 3 digitos: ")
numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10

print(f"El numero invertido es: {numero_invertido}")