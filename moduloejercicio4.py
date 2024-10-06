#Ejercicios Clase 4:

#Debemos alquilar el servicio de transporte para llegar a Mar del Plata con un
#grupo de personas, de cada persona debemos obtener los siguientes datos:

#- número de cliente
#- estado civil ("soltero", "casado"  o "viudo")
#- edad (solo mayores de edad, más de 17)
#- dni (validar que el numero sea de 8 digitos)


def pedirNumeroCliente():
    numeroCliente = input("Ingrese el número de cliente:")
    while True:
        if numeroCliente.isdigit():
            return int(numeroCliente)
        else:
            numeroCliente = input("Ingrese el número de cliente:")
    



def seleccionarEstadoCivil():
    estadoCivil = input("Ingrese estado civil del pasajero (soltero, casado o viudo): ").lower()

    while True:
        if estadoCivil == "soltero" or estadoCivil == "casado" or estadoCivil == "viudo":
            return estadoCivil
        else:
            print("Estado civil inválido. Por favor, ingrese 'soltero', 'casado' o 'viudo'.")
            estadoCivil = input("Ingrese estado civil del pasajero (soltero, casado o viudo): ").lower()

def ingresarEdad():
    edad = input("Ingrese una edad: ")
    while edad.isdigit()== False or int(edad) < 17:
        edad = input("Reingrese una edad valida: ")
    edadInt = int(edad)
    
    
        
        

    return edadInt


def ingresarDNI():
    dni = input("Ingrese DNI: ")
    while dni.isdigit()== False or len(dni) != 8:
        dni = input("Reingrese una dni valida: ")
    
    dniInt = int(dni)
        
        

    return dniInt

def ingresarGenero():
    genero = input("Ingresar género (femenino o masculino): ").lower()
    while genero != "femenino" and genero != "masculino":
         genero = input("Ingresar género válido : ").lower()
    return genero



#print(seleccionarEstadoCivil())
#print(pedirNumeroCliente())
#print(ingresarEdad())
#print(ingresarDNI())
#print(ingresarGenero())
