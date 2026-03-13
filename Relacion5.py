"""
Relacion5

Escribe un programa en python que permita guardar las notas de un alumno conseguidas en un cuatrimestre.
Guarda la información en un diccionario cuyas claves sean las asignaturas y los valores de las notas de cada asignatura. 
El programa pedirá la asignatura y la nota para esa asignatura. Si se recibe un número negativo en la nota,
el programa termina y muestra las asignaturas suspensas. 

"""
asignaturas = {}
asignaturas_aprobadas = {}
asignaturas_suspensas = {}
nota_asignatura = 1.0

while nota_asignatura >= 0:

    nombre_asignatura = input("Dime tu asignatura: ")
    nota_asignatura = float(input("Dime tu nota: "))
    
    asignaturas[nombre_asignatura] = nota_asignatura

    for nombre, nota in asignaturas.items():

        if nota > 0:

            if nota >= 5:
                asignaturas_aprobadas[nombre] = nota

            if nota < 5:
                asignaturas_suspensas[nombre] = nota


print("Las notas aprobadas son: ", asignaturas_aprobadas)
print("Las notas suspensas son: ", asignaturas_suspensas)

