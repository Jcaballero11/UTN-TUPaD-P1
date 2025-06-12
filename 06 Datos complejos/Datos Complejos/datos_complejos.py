#1) Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código  / Banana = 1330 / Manzana = 1700 / melon = 2800
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
frutas_sin_precios = ["Banana", "Ananá", "Melón", "Uva", "Naranja", "Manzana", "Pera"]
print(frutas_sin_precios)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
contactos= {"Juan" : 123456789, "Mario": 172839, "Alberto" : 392817, "Luis" : 1234567, "Sergio": 789456}
#Luego, pedí un nombre y mostrale el número asociado, si existe.
print(contactos['Juan'])

#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.
palabras = input("Ingrese una frase: ")


#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.
alumnos = {
    "Juan": (10, 8, 9),
    "Mario": (7, 6, 8),
    "Alberto": (9, 7, 6)
}
promedio = sum(alumnos["Juan"]) / len(alumnos["Juan"])
promedio = sum(alumnos["Mario"]) / len(alumnos["Mario"])
promedio = sum(alumnos["Alberto"]) / len(alumnos["Alberto"])
print(promedio)

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial1 = {"Ana", "Juan", "Marcerlo"}
parcial2 = {"Mario", "Alberto", "Luis"}

ambos = parcial1 & parcial2
solo1 = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2
print(ambos)
print(solo1)
print(al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe.
stock = {"Manzana": 10, "Pera": 20, "Naranja": 15, "Uva": 30}
stock["Manzana"] = 18
stock["Melón"] = 25
producto = input("Ingresá el nombre del producto a consultar: ").capitalize()
if producto in stock:
    print(f"El stock de {producto} es: {stock[producto]} unidades.")
else:
    print(f"El producto '{producto}' no está registrado.")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#Permití consultar qué actividad hay en cierto día y hora.
agenda = {("Lunes", "10:00"):"Examen", 
          ("Martes", "15:00"):"Reunion", 
          ("Miércoles", "13:00"):"Taller", 
          ("Jueves", "09:00"):"Violin",
          ("Viernes", "22:00"):"Cine"}
dia = input("Ingrese el día: ").capitalize()
hora = input("Ingrese la hora: ")
if (dia, hora) in agenda:
    print(f"El evento del día {dia} a las {hora} es: {agenda [(dia, hora)]}")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores.
# Diccionario original: país -> capital
paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}
invertido = {capital: pais for pais, capital in paises_a_capitales.items()}
print(invertido)
