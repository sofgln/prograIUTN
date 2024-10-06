
# 1-Escribir una función que reciba una lista de enteros, la misma calculará y 
# devolverá el promedio de todos los números.

lista_numeros = [1,2,3,4,5]

def calcular_promedio(lista)->float:
    total = 0
    for elemento in lista:
        total += elemento
        promedio = total / len(lista)
    return f"El promedio de la lista es de :{promedio}"

     

print(calcular_promedio(lista_numeros))


#2-Escribir una función parecida a la anterior, pero la misma deberá calcular y 
#devolver el promedio de los números positivos.

lista_nums_mixta= [10,-20,30,-40]

def calcular_promedio_positivo(lista)->float:
    acumulador_positivos = 0
    contador_positivos = 0
    for elemento in lista:
        if elemento > 0:
            acumulador_positivos += elemento
            contador_positivos += 1
            promedio = acumulador_positivos / contador_positivos
        return f"El promedio de la lista de números positivos es :{promedio}"

     

print(calcular_promedio_positivo(lista_nums_mixta))



#3-Escribir una función que calcule y retorne el producto de todos los elementos 
#de la lista que recibe como parámetro.

lista_productos = [3,3,3]

def calcular_productos(lista)->int:
    

#4-Escribir una función que reciba como parámetros una lista de enteros y 
#retorne la posición del valor máximo encontrado.

#5-Escribir una función que reciba como parámetros una lista de enteros y 
#muestre la/las posiciones en donde se encuentra el valor máximo hallado
#.
#6-Escribir una función llamada reemplazar_nombres que reciba como parámetros 
#una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. 
#La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista 
#con su correspondiente reemplazo y luego retornar la cantidad total de 
#reemplazos realizados.
