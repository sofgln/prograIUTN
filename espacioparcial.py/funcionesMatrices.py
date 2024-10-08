#como mostrar una matriz
matrizEjemplo = [[1,2,3,4],
                 [5,6,7,8]]

#mostrar matriz
def mostrarMatriz(matriz):
    """ esta funcion recibe una matriz y la muestra
    de una manera amigable al usuario """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")


#print(matrizEjemplo[1][2]) #primero fila después columna
#print(matrizEjemplo[0][-1])#muestra el último elemento

#mostrar una sola fila
#print(matrizEjemplo[1])

#mostrar coordenadas de donde se encuentra cada dato en una matriz
def mostrarCoordenadasMatriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            dato = matriz[fila][columna]
            print(f'Fila: {fila} | Columna: {columna} | Dato: {dato}')

#funcion para modificar matriz

def modificarDato(matriz,fila:int,columna:int,dato)->None:
    """esta función permite modificar un dato pasandole a la 
    función su ubicación  y el dato a ingresar"""
    matriz[fila][columna]= dato

    print(f"el nuevo valor de la fila {fila} columna {columna} es: " +matriz[fila][columna])




#inicializar matriz
def iniciarMatriz(filas:int,columnas:int,valorInicial: any)-> list:
    """esta función inicializa una matriz a demanda indicandole 
    su cantidad de filas, columnas y dato inicial, retorna una matriz en 0 para
    inicializarla dentro de una variable"""
    matriz=[]
    for i in range(filas):
        fila = [valorInicial] * columnas
        matriz += [fila]
    return matriz



def cargarMatriz(matriz:list):
    """esta función toma como parametro una matriz y permite cargarla manualmente"""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]= int(input(f"Fila {i} Columna{j}: "))


def cargaAleatoriaMatriz(matriz:list):
    """permite la carga de una matriz indicandole fila y 
    columna donde se desea ingresar el dato"""
    seguir = "s"
    while seguir == "s":
        fila =int(input("Indice de fila:"))
        columna =int(input("Indice de columna:"))
        dato =int(input("dato a cargar:"))
        matriz[fila][columna]= dato
        seguir = input("desea seguir cargando? s/n: ").lower


def buscar_dato_en_matriz(matriz: list[list], valor: int):
    """buscar dato especifico en matriz"""
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                print(f'El valor: {valor} fue encontrado en la fila {fila} | columna {columna}')


def suma_matrices(matriz_1: list[list], matriz_2: list[list]) -> list[list]:
    """suma 2 matrices y retorna la nueva matriz"""
    matriz_3 = []
    
    for fila in range(len(matriz_1)):
        fila_de_suma = []
        for columna in range(len(matriz_1[fila])):
            suma = matriz_1[fila][columna] + matriz_2[fila][columna]
            fila_de_suma.append(suma)
        matriz_3.append(fila_de_suma)
    return matriz_3

def busqueda_lineal_matriz2(matriz : list, valor : any) -> list:
    """
    Realiza una busqueda sobre una matriz de forma lineal

    Parametros:
    matriz: representa el conjunto de datos sobre el cual se va a realizar la busqueda
    valor: valor del cual se desea saber su indice

    Retorno: 
    Retorna None si el valor no se encuentra o una lista con los indices del elemento
    encontrado
    """
    retorno = None
    for i in range(len(matriz)):
        resultado = busqueda_lineal_matriz2(matriz[i], valor)
        if resultado != None:
            retorno = [i, resultado]
            break
    return retorno













