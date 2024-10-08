def busqueda_lineal(lista : list, valor : any) -> int:
    """
    Realiza una busqueda sobre una lista de forma lineal

    Parametros:
    lista: representa el conjunto de datos sobre el cual se va a realizar la busqueda
    valor: valor del cual se desea saber su indice

    Retorno: 
    Retorna None si el valor no se encuentra o el indice del primer elemento que
    coincide con el valor buscado
    """
    retorno = None
    for i in range(len(lista)):
        if lista[i] == valor:
            retorno = i
            break
    return retorno