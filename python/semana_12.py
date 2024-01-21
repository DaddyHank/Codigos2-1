#Dividir entre 0...

try:
    n1 = input("Escriba un número")
    n2 = input("Escriba otro número")
    lista1 = ["a", "b", "c", "d"]
    print(n1/n2)
except ZeroDivisionError:
    print("Error, no es posible dividir entre cero")
except TypeError:
    print("Error, el tipo ingresado no es el correcto")
except ValueError:
    print("Error, número no válido")
except IndexError:
    print("Indice fuera de rango")
