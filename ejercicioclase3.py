#Ejercicio 3-1:
#Crear una función que permita determinar si un número es par o no.
#La función retorna true en caso afirmativo y false en caso contrario.

#numero = int(input("Ingrese un número: "))

#def numero_par(numero)-> bool:
 #   '''esta función pide un número y devuelve si es par o impar'''
    #  if numero % 2 == 0:
     #   return True
    
    #return False
    
#print(numero_par(numero))


#Ejercicio 3-2:
#Crear una función que calcule el resultado de la potencia entre dos numeros
#recibidos por parametro y lo retorne. Validar que el exponente no sea negativo
#num1 = int(input("Ingrese la base:"))
#while num1 < 0 :
        # num1 = int(input("Ingrese un número entero:"))
#num2 = int(input("Ingrese el exponente:"))
#while num2 < 0 :
        # num1 = int(input("Ingrese un número entero:"))

#def potencia_entre_dos(num1: int, num2: int)-> int:
 #   '''esta función calcula la potencia entre los dos número ingresados'''
  
         
   # potencia = num1 ** num2
    #return potencia

#print(potencia_entre_dos(num1,num2))

#Ejercicio 3-3:
#Crear una función que pida el ingreso de un numero. Validar que dicho ingreso
#sea un numero antes de retornarlo. En caso afirmativo, retornar el numero,
#caso contrario retornar None

#num_a_validar = input("Ingrese un número:")
#def validar_numero(num_a_validar):
      #if num_a_validar.isdigit():
            #return num_a_validar
      #else:
            #return None
      
#print(validar_numero(num_a_validar))

#Ejercicio 3-4:
#Realizar un programa en donde se puedan utilizar los prototipos de la función
#Sumar en sus 4 combinaciones.
#sumar1(int, int) -> int;
#sumar2() -> int;
#sumar3(int, int) -> None;
#sumar4() -> None;

#int1 = int(input("Ingrese un número:"))
#int2= int(input("Ingrese el segundo número:"))
#def sumar1(int1,int2)-> int:
 #   resultado_suma1 = int1 + int2
  #  return resultado_suma1

#print(sumar1(int1,int2))



#def sumar2()-> int:
#    int3 = int(input("Ingrese un número:"))
#   int4= int(input("Ingrese el segundo número:"))
#    resultado_suma2 = int3 + int4
#   return resultado_suma2

#print(sumar2()) 


#int5 = int(input("Ingrese un número:"))
#int6= int(input("Ingrese el segundo número:"))
#def sumar3(int5,int6)-> None:
#   resultado_suma3 = int5 + int6
#    return resultado_suma3

#print(sumar3(int5,int6))

#def sumar4()-> None:
#    int7 = int(input("Ingrese un número:"))
#    int8= int(input("Ingrese el segundo número:"))
#    resultado_suma4 = int7 + int8
#    return resultado_suma4

#print(sumar4())

#Ejercicio 3-5:
#Escribe funciones para calcular el área las siguientes figuras geométricas:
#Circulo
#Rectangulo
#Cuadrado
#Triangulo rectangulo

pi = 3.14

def area_de_circulo() :
    radio = float(input("Ingrese el radio del círculo: "))
    area = pi * radio ** 2
    return area

print(area_de_circulo())

def area_rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area_rec = base * altura
    return area_rec
print(area_rectangulo())

def area_cuadrado():
    lado = float(input("Ingrese la medida del lado del cuadrado: "))
    area_cua = lado ** 2
    return area_cua
print(area_cuadrado())


def area_triangulo_rectangulo():
    cateto = float(input("Ingrese la medida del primer cateto: "))
    cateto2 = float(input("Ingrese la medida del segundo cateto: "))
    area_tr_rec = cateto * cateto2 / 2
    return area_tr_rec
print(area_triangulo_rectangulo())
    

    







      

       












