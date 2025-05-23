# -*- coding: utf-8 -*-
"""U5_listas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qHV0w3awcJBC07WnrRBre0Euismo1Rjb

***
## **LISTAS**
***

Las listas son secuencias mutables ya que permiten modificar los valores de sus elementos, eliminar o añadir elementos.

En ellas se pueden almacenar tantos elementos como se desee, incluso pueden existir listas vacías (sin elementos). Para definirlas se utilizan corchetes y se separan los elementos mediante comas :

`nombre_lista = [valor1, valor2, ...]`.
"""

notas = [9.1, 8.5, 7.3]

print(notas)
print(type(notas))

"""No es necesario que una lista contenga el mismo tipo de datos. Por ejemplo, podemos tener la siguiente lista:"""

lista = ["UTN", 2, 3.5, True]

print(lista)
print(type(lista))

"""#### **MÉTODOS CON LISTAS**

**range**

Se puede crear una lista de números automáticamente utilizando `range(inicio, fin)`.
"""

lista_range = list(range(1,10))

print(lista_range)

"""Por default toma intervalos de 1 en 1. Para modificar esto basta con agregar un argumento a `range(inicio, fin, intervalo)`."""

lista_range = list(range(1,10,2))

print(lista_range)

"""**split**

Permite crear una lista a partir de un string, utilizando un caracter específico como separador. Por defecto, utiliza los espacios para separar el string en distintos elementos de la lista.
"""

hello_world_string = 'Hello world!'
lista_separada = hello_world_string.split()

print(lista_separada)

"""***Slicing***

Es posible acceder a los distintos elementos de una lista utilizando el índice del mismo, de manera análoga a como se realiza con los strings `nombre_lista[índice_elemento]`.
"""

lista = ["UTN", 2, 3.5, True]

posicion_1_lista = lista[0]

print(posicion_1_lista)
print(type(posicion_1_lista))

rango_lista = lista[0:3]
print(rango_lista)

"""***Añadir elementos***

Se usa la sentencia `nombreLista.append(elementoAAñadir)`.

Notar que no es necesario sobreescribir la variable, las sentencia `append()` modifica la lista sin necesidad de sobreescribirla.
"""

print(notas)

notas.append(9.2)
notas.append(False)
print(notas)

"""***Eliminar elementos***

Se usa la sentencia `nombreLista.remove(elementoAEliminar)`.

"""

notas.remove(9.2)
notas.remove(False)
print(notas)

"""***Actualizar elementos***

Para esto se hace uso del slicing. Esta operación diferencia una lista de un string, ya que no puede ser efectuada en el segundo tipo de dato. <Por ejemplo, si queremos actualizar el tercer elemento:
"""

notas[2] = "Hola mundo"

print(notas)

"""***Concatenación***

Se pueden concatenar dos listas usando el operador de la suma (**+**).
"""

notas_2 = notas + ["UTN", True]

print(notas_2)

"""***Comprobar si un valor existe dentro de la lista***

Se usa el término `in`.
"""

print(8 in notas_2)

print('UTN' in notas_2)

"""#### **LISTAS ANIDADAS**

Pueden haber listas adentro de otras listas, por ejemplo:
"""

lista_anidada = [1, 1.3, ["UTN", "Mendoza"]]

print(lista_anidada)

posicion_2_lista = lista_anidada[2]
print(posicion_2_lista)

posicion_2_1_lista = lista_anidada[2][1]

print(posicion_2_1_lista)