#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
mult_4= list(range(4,101,4))
print(mult_4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
#¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
lista_elem = ["violin", "viola", "violonchelo", "guitarra", "bajo"]
print(lista_elem[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
instrumentos = []
instrumentos.append("violin")
instrumentos.append("piano")
instrumentos.append("bateria")
print(instrumentos)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
#Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien
#investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = ["loro"]
animales[-1]= ["oso"]
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
#1-define una lista de variables llamada numero
#2-utlizamos remove para eliminar el numero maximo que es 22
#3-imprime la lista de numeros sin el 22

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5
#y mostrar por pantalla los dos primeros.
numeros=list(range(10,31,5))
print(numeros)
print(numeros[:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3]= ["hermoso", "grande"]
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
#Imprimir la lista resultante por pantalla.
dobles=[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras(2).append("jugo")
compras[0].remove("pan")
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. FALTA HACER

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
lista_anidada=[15,True,[25.5,57.9,30.6],False]