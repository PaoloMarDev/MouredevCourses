### Condicionales ###

my_condition = False

if(my_condition):
    print("Se ejecuta la condición del if")

my_condition = 5 * 3

if(my_condition == 10):
    print("Se ejecuta la condición del segundo if")

if(my_condition > 10 and my_condition < 20):
    print("Es mayor que 10")
elif(my_condition == 25):
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


print("La ejecución continúa")

my_string = ""

"""
if my_string: # Si no tiene una condición python busca que tenga valor la variable
    print("Mi cadena de texto es vacía")
"""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de texto":
    print("Esta cadena de texto coincide")
