def bubble_sort(lista_numeros: list[int], modo: str): # ASC | DES
    """función que realiza bubble sort a una lista
    funciona con los parametros de una lista y el modo de asc o des"""
    lista_copia = lista_numeros.copy()
    for indice in range(len(lista_copia) - 1):
        for sub_indice in range(indice + 1, len(lista_copia)):
            
            if (modo == 'ASC' and lista_copia[indice] > lista_copia[sub_indice] or 
                modo == 'DES' and lista_copia[indice] < lista_copia[sub_indice]):
                lista_copia[indice], lista_copia[sub_indice] =\
                lista_copia[sub_indice], lista_copia[indice]

    return lista_copia

def selection_sort(lista_numeros: list[int], modo: str):
    """realiza un selection sort tomando como parametros una lista y el modo asc o des"""
    lista_copia = lista_numeros.copy()
    for indice in range(len(lista_copia) - 1):
        indice_minimo = indice
        for sub_indice in range(indice + 1, len(lista_copia)):
            if (modo == 'ASC' and lista_copia[indice_minimo] > lista_copia[sub_indice] or 
                modo == 'DES' and lista_copia[indice_minimo] < lista_copia[sub_indice]):
                indice_minimo = sub_indice
        
        if indice_minimo != indice:
            lista_copia[indice_minimo], lista_copia[indice] =\
            lista_copia[indice], lista_copia[indice_minimo]
            
    return lista_copia