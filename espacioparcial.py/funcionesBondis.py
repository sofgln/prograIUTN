#mostrar coordenadas de donde se encuentra cada dato en una matriz
def mostrarCoordenadasMatriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            dato = matriz[fila][columna]
            print(f'Linea: {fila} | nro de Vehículo: {columna} | recaudación: {dato}')


#cargar recaudación diario 
def modificarDato(matriz, linea: int, nrovehiculo: int, recaudacionDiaria: int) -> str:
    """Esta función permite modificar un dato pasando su ubicación y el dato a ingresar."""
    matriz[linea][nrovehiculo] = recaudacionDiaria
    recaudacionmsg = f"La recaudación diaria del coche {nrovehiculo} de la línea {linea} es: ${recaudacionDiaria} mil pesos."
    return recaudacionmsg

def cargarRecaudaciónDiaria(matriz):
   
    linea = int(input("Ingrese la línea del vehículo a cargar: "))
    nrovehiculo = int(input("Ingrese el número de vehículo: "))
    recaudacionDiaria = float(input("Ingrese la recaudación diaria: "))
    recaudacionmsg = modificarDato(matriz, linea, nrovehiculo, recaudacionDiaria)


    print(recaudacionmsg)



#mostrar recaudación de cada vehiculo de cada linea
#mostrar coordenadas de donde se encuentra cada dato en una matriz
def mostrarRecaudacionPorVehiculo(matriz):
    for linea in range(len(matriz)):
        for vehiculo in range(len(matriz[linea])):
            recaudacion = matriz[linea][vehiculo]
            print(f'Linea: {linea} | Nro Vehículo: {vehiculo} | recaudación del día: ${recaudacion} mil pesos')



#mostrar la recaudacion total
def mostrarRecaudacionTotal(matriz):
    recaudacionTotal = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            recaudacionTotal += matriz[fila][columna]
    recaudacionmsg = f"la recaudacion total del día es de ${recaudacionTotal} mil pesos"
    return recaudacionmsg


#funciones punto 7 De cada linea, mostrar los vehiculos que superen los 5000 de recaudacion"

def mostrarVehiculosMasCinco(matriz):
    linea0Vehiculos=[]
    linea1Vehiculos = []
    linea2Vehiculos =[]

    for i in range(len(matriz[0])):
        if matriz[0][i]  > 5:
            linea0Vehiculos.append(matriz[0][i])
    for i in range(len(matriz[1])):
        if matriz[1][i]  > 5:
            linea1Vehiculos.append(matriz[1][i])
            
    for i in range(len(matriz[2])):
        if matriz[2][i] > 5:
           linea2Vehiculos.append(matriz[2][i])
    
    print(f"Los vehículos con mayor recaudación de la linea 0 obtuvieron las siguientes recaudaciones: {linea0Vehiculos}")
    print(f"Los vehículos con mayor recaudación de la linea 1 obtuvieron las siguientes recaudaciones: {linea1Vehiculos}")
    print(f"Los vehículos con mayor recaudación de la linea 2 obtuvieron las siguientes recaudaciones: {linea2Vehiculos}")
           
            
#funciones 6 Calcular la recaudación promedio por vehículo de cada línea

def mostrarPromedioPorLinea(matriz):
    linea0Total=0
    linea1Total = 0
    linea2Total =0

    for i in range(len(matriz[0])):
        linea0Total += matriz[0][i]
    for i in range(len(matriz[1])):
        linea1Total += matriz[1][i]
    for i in range(len(matriz[2])):
        linea2Total += matriz[2][i]

    promedioLinea0 = linea0Total / 5
    promedioLinea1 = linea1Total/ 5
    promedioLinea2 = linea2Total /5
    
    print(f"La recaudación promedio de la línea 0 es de : ${promedioLinea0} mil pesos")
    print(f"La recaudación promedio de la línea 1 es de : ${promedioLinea1}  mil pesos")
    print(f"La recaudación promedio de la línea 2 es de : ${promedioLinea2} mil pesos")
           
            



