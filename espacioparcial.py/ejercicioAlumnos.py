"""Cada estudiante tiene:

- Nombre 
- Apellido
- Legajo
- Division
- Notas (primer parcial y segundo parcial)

Asi mismo, contamos con una lista de divisiones a 
las que puede pertenecer un alumno: 
1A, 2B, 1C, 1D, 2A, 2B , 2C, 3A, 3B, 4A

Las consultas que se requieren realizar son:

- Nombre, division y nota del estudiante con mayor promedio.

- De cada division, mostrar los alumnos en condicion de 
aprobacion directa (se requiere nota 6 o mas en ambos 
parciales para esta condicion). 

- Ordenar los alumnos por legajo, nombre o apellido

- De cada division, el alumno con el menor promedio

- Seleccionar un alumno y modificar sus notas o su division.

"""

import os

ALUMNO = "Hola"

def menu(titulo : str , opciones : list):
    cantidad_opciones = len(opciones)
    
    print(titulo)
    for i in range(cantidad_opciones):
        print(f"{i+1} - {opciones[i]}")

    print("0 - Salir.")

    opcion = int(input("Ingrese una opcion: "))
    return opcion


def buscar_mayor_promedio(alumnos):
    indice_mayor_promedio = None
    mayor_promedio = 0
    for i in range(len(alumnos[0])):
        promedio = (alumnos[4][i] + alumnos[5][i]) / 2
        if i == 0 or mayor_promedio < promedio:
            mayor_promedio = promedio
            indice_mayor_promedio = i
    return indice_mayor_promedio

def mostrar_alumnos_con_aprobacion_directa(alumnos, divisiones):

    for division in divisiones:
        bandera = False
        print(f"Alumnos en condicion AD de la division {division}")
        for i in range(len(alumnos[0])):
            if alumnos[3][i] == division and alumnos[4][i] >= 6 and alumnos[5][i] >=6:
                aux = i
                print(f"Nombre completo: {alumnos[1][aux]},{alumnos[0][aux]}")
                bandera= True
        if bandera == False:
            print("No hay alumnos en condicion de AD")

def ordenar_matriz(alumnos, criterio):
    for i in range(len(alumnos[0])):
        for j in range(len(alumnos[0])):
            if alumnos[criterio][i] < alumnos[criterio][j]:
                for k in range(len(alumnos)):
                    aux = alumnos[k][i]
                    alumnos[k][i] = alumnos[k][j]
                    alumnos[k][j] = aux


def mostrar_alumnos_con_menor_promedio(alumnos, divisiones):

    for division in divisiones:
        menor_promedio = None
        indice_menor_promedio = None
        for i in range(len(alumnos[0])):
            if alumnos[3][i] == division:
                promedio = (alumnos[4][i] + alumnos[4][i]) / 2
                if menor_promedio == None or promedio < menor_promedio:
                    menor_promedio = promedio
                    indice_menor_promedio = i
        if indice_menor_promedio != None:
            print(f"El peor promedio de {division} lo tiene {alumnos[1][indice_menor_promedio]}, {alumnos[0][indice_menor_promedio]}")
        else:
            print(f"No hay alumnos en {division}")

def mostrar_alumnos(alumnos):
    for i in range(len(alumnos[0])):
        print(f"{i+1} - Nombre completo:{alumnos[1][i]},{alumnos[0][i]},Legajo:{alumnos[2][i]},Division:{alumnos[3][i]},Notas:{alumnos[4][i]},{alumnos[5][i]}")
    

def pedir_alumno(alumnos):
    mostrar_alumnos(alumnos)
    opcion = int(input("Ingresa el alumno a modificar: "))
    return opcion-1

def modificar_alumno(alumnos, indice, divisiones,modifica_notas : bool):
    if modifica_notas:
        #VALIDAR ANTES DE ASIGNAR
        alumnos[4][indice] = int(input("Ingresa la primer nota del alumno"))
        alumnos[5][indice] = int(input("Ingresa la segunda nota del alumno"))
    else:
        division = input("Ingresa la division del alumno")
        for d in divisiones:
            if division == d:
                alumnos[3] = division
                break
                
def main():
    alumnos = [
    ["Juan", "Martin", "Claudia", "Francisco", "Romina"], #nombres
    ["Martinez","Fernandez","Ferreira", "Casals", "Scarsi"], #apellidos
    [123456,234567,345567,456789,567890],#legajos
    ["2A", "2A", "1C", "1B" ,"1D"],#divisiones
    [5,8,2,9,10],#nota 1
    [9,8,5,7,10]#nota 2
    ]

    lista_divisiones = ["1A", "1B", "1C", "1D", "2A",
                        "2B" , "2C", "3A", "3B", "4A"]
    opciones = [ "Nombre, division y nota del estudiante con mayor promedio",
                "De cada division,alumnos en condicion de aprobacion directa",
                "Ordenar los alumnos por legajo, nombre o apellido",
                "De cada division, el alumno con el menor promedio",
                "Seleccionar un alumno y modificar sus notas o su division."]
    while True:
        opcion = menu("Menu principal\n", opciones)

        match(opcion):
            case 0: #Salir
                break
            case 1:#- Nombre, division y nota del estudiante con mayor promedio
                mayor_promedio = buscar_mayor_promedio(alumnos)
                print(f"Informacion del estudiante con mayor promedio: {alumnos[0][mayor_promedio]} {alumnos[3][mayor_promedio]} {(alumnos[4][mayor_promedio]+alumnos[5][mayor_promedio])/2}")
            case 2:#De cada division,alumnos en condicion de aprobacion directa
                mostrar_alumnos_con_aprobacion_directa(alumnos, lista_divisiones)
            case 3:#Ordenar los alumnos por legajo, nombre o apellido
                criterio = 0
                opcion = menu("Ordenar por:", ["Nombre", "Apellido", "Legajo"])
                if opcion >= 1 and opcion <=3:
                    ordenar_matriz(alumnos, opcion-1)  
                print(alumnos)              
            case 4:#De cada division, el alumno con el menor promedio
                mostrar_alumnos_con_menor_promedio(alumnos, lista_divisiones)
            case 5:#Seleccionar un alumno y modificar sus notas o su division.
                indice_alumno_a_modificar = pedir_alumno(alumnos)
                opcion = menu("Seleccione que desea modificar", ["Notas", "Division"])
                modificar_alumno(alumnos, indice_alumno_a_modificar,lista_divisiones, opcion == 1)
                mostrar_alumnos(alumnos)
            case _:
                pass
        input("Presione Enter para continuar...")
        os.system("cls")