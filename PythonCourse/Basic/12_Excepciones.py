### Excepciones Manejo ###

numberOne = 5 
numberTwo = 1
numberTwo = "1"

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    # Se ejecuta si se produce un error
    print("Se ha producido un error")

# try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")


# try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")


## -------Nuevo ejemplo--------
# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except TypeError:
    # Se ejecuta si se produce un error
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")


# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)

