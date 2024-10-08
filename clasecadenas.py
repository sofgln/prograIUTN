#Crear una función que reciba una cadena y un caracter.
#La función deberá devolver el índice en el que se encuentre la primera ocurrencia de dicho caracter, o -1 en caso de que no esté.

def buscarCaracter(cadena : str, caracter):
    indiceCaracter = -1
    for i in range(len(cadena)):
         if cadena[i] == caracter:
            indiceCaracter = i
            return indiceCaracter
    return indiceCaracter
    
        



print(buscarCaracter("Hola Mundo","i"))

#Crear una función que reciba como parámetro una cadena y 
# determine si la misma es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.

#def IsPalindromo (cadena)-> bool:
#    cadenaIngresada = cadena
#    cadena2 = cadena.reverse()
#    if cadenaIngresada == cadena2:
#        return True
    
#print(IsPalindromo("rotomotor"))


#Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos consecutivos.


#Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def caracterRepetitivo(cadena: str)->str:
  
    nuevaCadena= ""
    for i in range(len(cadena)):
        if cadena[i] == cadena[i-1]:
            pass
        else:
            nuevaCadena += cadena[i]
    return nuevaCadena


print(caracterRepetitivo("Hooola"))
        
#Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.

#Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
def suprimirVocales(cadena: str)->str:
    vocales= ["a","e","i","o","u","A","E","I","O","U"]
  
    nuevaCadena= ""
    for i in range(len(cadena)):
        if cadena[i] not in vocales  :
            nuevaCadena += cadena[i]
        else:
            pass
    return nuevaCadena


print(suprimirVocales("Maria"))





