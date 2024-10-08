""" 

Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total 
tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).

Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
Menú:

Cargar planilla. El chofer se debe identificar (el legajo debe existir 
dentro de una lista de legajos). Si el chofer existe cargará la recaudación 
del viaje indicando línea y coche (no necesariamente un chofer está 
asignado a una única línea y coche), estos datos deben estar validados. 
Un chofer puede cargar más de una recaudación por día (para distintas líneas 
y distintos coches). Cada coche de cada línea puede tener varias recaudaciones 
diarias.

Mostrar la recaudación de cada coche y línea (mostrar la matriz).

Calcular y mostrar recaudación por línea.

Calcular y mostrar recaudación por coche.

Calcular y mostrar la recaudación total.

Ordenar la matriz de vehiculos por recaudacion de forma descendente

Mostrar el vehiculo con mayor y menor recaudacion por cada linea

Calcular la recaudacion promedio por vehiculo de cada linea

De cada linea, mostrar los vehiculos que superen los 5000 de recaudacion

Salir.

Todo el desarrollo tiene que estar modularizado: ingreso de datos, 
validaciones de líneas y coches, generación y verificación de existencia de 
legajo, cálculos, etc.

"""
import funcionesAux
import funcionesBondis
import funcionesMatrices
legajosRegistrados = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115]
listaDeOpciones = [1,2,3,4,5,6,7,8,9]
opcion = 0

#crear matriz de líneas de bondi [i]=línea [j]= nro de coche dato = recaudación(expresado en miles)
matrizBondis = [[176,3,345,67,89,90],
                [146,34,35,29,49,340],
                [134,65,45,37,99,10]
                ]


def Main():
    def Menu():
    
        print("Bienvenido al sistema de gestión de COLECTIVOS SA")
        legajoValido = funcionesAux.validarLegajo(legajosRegistrados)
        if legajoValido :
            print(f"Ingreso de sesión exitoso. Bienvenido {legajoValido}\n  opciones del menú:")
            print("1. Cargar recaudación diaria")
            print("2. Mostrar la recaudación de cada coche y línea")
            print("3. Calcular y mostrar la recaudación total.")
            print("4. Ordenar la matriz de vehiculos por recaudacion de forma descendente.")
            print("5. Mostrar el vehiculo con mayor y menor recaudacion por cada linea")
            print("6.Calcular la recaudacion promedio por vehiculo de cada linea")
            print("7.De cada linea, mostrar los vehiculos que superen los 5000 de recaudacion")
            print("8. Salir")
            
            opcion = funcionesAux.validarOpciones(listaDeOpciones)
            return opcion

    opcionSeleccionada = Menu()

   
    if opcionSeleccionada == 1:
        print("Has seleccionado la opción 1: Cargar recaudación diaria.")
        funcionesBondis.cargarRecaudaciónDiaria(matrizBondis)
        
    elif opcionSeleccionada == 2:
        print("Has seleccionado la opción 2: Mostrar la recaudación de cada coche y línea.")
        print(funcionesBondis.mostrarRecaudacionPorVehiculo(matrizBondis))
        
    elif opcionSeleccionada == 3:
        print("Has seleccionado la opción 3: Calcular y mostrar la recaudación total.")
        print(funcionesBondis.mostrarRecaudacionTotal(matrizBondis))
        
    elif opcionSeleccionada == 4:
        print("Has seleccionado la opción 4: Ordenar la matriz de vehículos por recaudación de forma descendente.")
        
    elif opcionSeleccionada == 5:
        print("Has seleccionado la opción 5: Mostrar el vehículo con mayor y menor recaudación por cada línea.")
        
    elif opcionSeleccionada == 6:
        print("Has seleccionado la opción 6: Calcular la recaudación promedio por vehículo de cada línea.")
        print(funcionesBondis.mostrarPromedioPorLinea(matrizBondis))
        
    elif opcionSeleccionada == 7:
        print("Has seleccionado la opción 7: Mostrar los vehículos que superen los 5000 de recaudación por línea.")
        print(funcionesBondis.mostrarVehiculosMasCinco(matrizBondis))
        
    elif opcionSeleccionada == 8:
        print("Has seleccionado la opción 8: Salir.")
        
    else:
        print("Opción inválida. Inténtelo de nuevo.")
print(Main())

    







    

