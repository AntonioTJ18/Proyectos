"""
Relaccion6

Escribir un programa que simule el famoso juego del ahorcado. 
El programa debe cumplir los siguientes requisitos: 
● El programa debe preguntar al usuario la palabra a adivinar.
 A partir de la palabra introducida debe crear una lista con los caracteres de la palabra. 

● Después debe ir preguntando al usuario por letras hasta un máximo de 5 fallos o hasta que no queden letras en la lista.
 En ambos casos el programa terminará pero mostrará el mensaje “Perdiste” si se cometen 5 fallos y el mensaje “Ganaste” 
si no quedan palabras en la lista.
 
● Cada vez que el usuario introduzca una nueva letra, si la letra está en la lista la eliminará y mostrará el mensaje
 “Acierto”, mientras que si la letra no está en la lista mostrará el mensaje “Fallo”. 

Si la letra está más de una vez en la lista, sólo se eliminará la primera instancia que aparezca. 
"""

palabra_secreta = input("Dime tu palabra secreta: ")
lista_secretas = list(palabra_secreta)
correcto = False
intentos = 5

while intentos > 0 and len(lista_secretas) != 0:
    
    letra = input("Dime una letra retrasado: ")

    for letras in lista_secretas:

        if letra == letras:
            lista_secretas.remove(letras)
            correcto = True

    if correcto == True:
         print("Letra acertada")
    else:
            intentos -= 1
            print("Intentos restantes: ", intentos)
        


if len(lista_secretas) == 0:
    print("Has ganado mamañema")
    print("Tienes un total de intentos: ",  intentos)
elif intentos == 0:
    print("Has perdido mamañema, mira que era dificil pero te has superado gilipollas")
    print("La palabra era: " + palabra_secreta)

