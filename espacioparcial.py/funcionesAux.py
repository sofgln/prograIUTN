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


#Validar nombre
def validarNombre():
    nombre = input("", "Ingrese nombre: ")
    while nombre == "":
             nombre = input("", "Reingrese nombre: ")


#validar edad


def validarEdad():
      edad = int(input("Mensaje", "Ingrese una edad: "))
      while edad < 18 or edad >= 90:
            edad = int(input("Mensaje", "Reingrese una edad valida: "))

#validar legajo
def validarLegajo():
 legajo = int(input("Mensaje", "Ingrese un numero de legajo: "))
 while legajo < 1000 or legajo > 9999:
            legajo = int(input("Mensaje", "Registre un legajo valido: ")) 

#validar estado civil
def valirdarEstadoCivil():
    estado = input("Mensaje", "Registre su estado civil: ")
    while estado != "Soltero/a" and estado != "Casado/a" and estado != "Viudo/a" and estado != "Divorciado/a":
         estado = input("Mensaje", "Reingrese su estado civil valido: ")







