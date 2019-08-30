"""Desarrollar un modulo que pida un numero romano entre 1 a 500 Opciones:
        Introduccir numero romano y mostrar su equivalente en sistema decimal
        ingresar dos numeros romanos y hacer la suma de estos
        ingresar otro numero(mayor) y realizar la resta
            Mostrar el resultado en numeros romanos
"""
#Diccionario que contiene los numeros romanos con su valor
numeros_romanos = {
    "I":1, 
    "V":5, 
    "X":10, 
    "L":50, 
    "C":100, 
    "D":500, 
    "M":1000
    }

def NumerosRomanos():
    """ Convierte un numero romano a entero , suma y resta con numeros romanos """
    romano = input("Ingrese un Numero en Romano: ").upper()
    while True:
        print("###########################################")
        print("# El numero Romano de estar entre 1 a 3999")
        print("# Ingrese una Opcion:")
        print("# 1. Conversion")
        print("# 2. Suma de Romanos")
        print("# 3. Resta de Romanos")
        print("# 4. Salir")
        print("###########################################")
        user_input = input(":")

        if user_input == "1":
            print("###########################################")
            print("El numero Romano " + romano + " Es: ")
            print(roman_to_int(romano))
            print("###########################################")
            
        elif user_input == "2":
            r2 = input('Ingrese el Segundo Numero Romano: ').upper()
            valor_r1 = roman_to_int(romano)
            valor_r2 = roman_to_int(r2)
            print("###########################################")
            print("La suma es : " + SumaRomanos(valor_r1 , valor_r2))
            print("###########################################")

        elif user_input == "3":
            r2 = input('Ingrese el Segundo Numero Romano: ').upper()
            valor_r1 = roman_to_int(romano)
            valor_r2 = roman_to_int(r2)

            if valor_r1 > valor_r2:
                print("###########################################")
                print("La suma es : " + RestaRomanos(valor_r1 , valor_r2))
                print("###########################################")
            else:
                print("###########################################")
                print("El primer numero romano es menor que el segundo")
                print("Vuelva a intentarlo")
                print("###########################################")

        elif user_input == "4":
            break
        
def roman_to_int(romano):
    """ Conviterte un Numero romano a entero"""
    n = len(romano)
    value = numeros_romanos[romano[n-1]]
    for letra in range(n-1,0,-1):
        current = numeros_romanos[romano[letra]]
        prev = numeros_romanos[romano[letra-1]]
        value += prev if prev >= current else -prev
    return value

def int_to_roman(number):
    """ Convierte un entero a numero romano. """

    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(number / ints[i])
        result.append(nums[i] * count)
        number -= ints[i] * count
    return ''.join(result)

#Suma dos Numeros
def SumaRomanos(r1 , r2):
    """ Suma dos Numero enteros"""
    value = r1 + r2
    return int_to_roman(value)
    

#Resta dos Numeros
def RestaRomanos(r1 , r2):
    """ Resta dos Numero enteros"""
    value = r1 - r2
    return int_to_roman(value)

if __name__ == '__main__':
    import sys
    NumerosRomanos()
