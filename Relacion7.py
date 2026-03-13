"""
Relacion7

Escribir un programa que realice la devolución de una cantidad dada por el usuario en monedas. 
El programa debe cumplir los siguientes requisitos: 
    ● Solo se disponen de tres tipos de monedas: 5, 2 y 1 €. 
    Crear una lista que contenga estos tres tipos de moneda y usar la lista en la solución. 
    ● El programa debe preguntar al usuario por una cantidad entera de euros. 

    ● El programa debe mostrar por pantalla el mínimo número de monedas necesarias para sumar la 
    cantidad introducida por el usuario y cuántas monedas de cada tipo se necesitan para ello. 

El número de monedas de cada tipo debe guardarse en otra lista. 
"""
lista_de_monedas = [5, 2, 1]
cantidad_monedas = [0, 0, 0]

cantidad = int(input("Cantidad de dinero a dividir: "))

resto = cantidad

for i in range(len(lista_de_monedas)):
    cantidad_monedas[i] = resto // lista_de_monedas[i]
    resto = resto % lista_de_monedas[i]

total_monedas = sum(cantidad_monedas)

print("Para devolver", cantidad, "€ se necesitan", total_monedas, "monedas")

for i in range(len(lista_de_monedas)):
    print("Monedas de", lista_de_monedas[i], "€:", cantidad_monedas[i])
