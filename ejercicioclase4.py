#Ejercicios Clase 4:

#Debemos alquilar el servicio de transporte para llegar a Mar del Plata con un
#grupo de personas, de cada persona debemos obtener los siguientes datos:

#- número de cliente
#- estado civil ("soltero", "casado"  o "viudo")
#- edad (solo mayores de edad, más de 17)
#- dni (validar que el numero sea de 8 digitos)

#NOTA: el precio por pasajero es de $60000.

#Se debe informar (solo si corresponde):

#a)  La cantidad de personas con estado "casado" de más de 40 años y
#  menos de 60 años.
#b)  el número de cliente y edad de la mujer soltera más joven.
#c)  cuánto sale el viaje total sin descuento.
#d)  si hay más del 50% de los pasajeros que tiene más de 60 años , el precio
#    final tiene un descuento del 25%, que solo mostramos si corresponde.

#Crear funciones para realizar la validación e ingreso de datos, incorporandolas a nuestros módulos

from moduloejercicio4 import *


casadoMayoresCounter = 0
mujerSolteraJovenEdad = 0
mujerSolteraJovenNumero = 0
totalSinDescuento = 0
porcentajeSesentaAños = 0
pasajerosCounter = 0
pasajerosMayoresASesentaCounter = 0
hayDescuento = False
totalDescuento = 0


def nuevoViaje():
    while True :
      numeroCliente = pedirNumeroCliente()
      estadoCivil = seleccionarEstadoCivil()
      edad = ingresarEdad()
      dni = ingresarDNI()
      genero = ingresarGenero()

      # informe c
      totalSinDescuento += 60000
      pasajerosCounter += 1


      #informe a
      if estadoCivil =="casado" and edad > 40 and edad < 60:
         casadoMayoresCounter += 1
      # informe b
      if genero == "femenino" and edad > 0 and edad < mujerSolteraJovenEdad:
         mujerSolteraJovenEdad = edad
         mujerSolteraJovenNumero = numeroCliente

    #informe d
      if edad >= 60 :
         pasajerosMayoresASesentaCounter += 1
      porcentajeSesentaAños = (pasajerosMayoresASesentaCounter * 100)/ pasajerosCounter
      if porcentajeSesentaAños > 50:
         hayDescuento = True
         totalADescontar = totalSinDescuento * 0.25
         totalDescuento = totalSinDescuento - totalADescontar
         




     
      continuar = input("Desea ingresar otro pasajero? si/no: ")
      if continuar == "no":
         break
      
      #informe a
      if casadoMayoresCounter > 0:
        print(f"La cantidad total  de pasajeros casados entre 40 y 60 años es {casadoMayoresCounter}")

      #informe b
      print(f"La clienta más jóven soltera tiene el número de cliente {mujerSolteraJovenNumero} con {mujerSolteraJovenEdad} años")

      #informe c
      print(f"el viaje total sin descuentos es de ${totalSinDescuento}")

      #informe D
      if hayDescuento:
         print(f"Por haber un porcentaje del {porcentajeSesentaAños}% de pasajeros mayores a 60 años al viaje se le aplica un descuento del 25% quedando un precio total de ${totalDescuento}")




    




        
        
 
