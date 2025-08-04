### Modulos ### 
# En resumen esto es como se importan librerías o codigos
# y como usarlos. El problema con los que inician con
# número es que python no permite importar algo que
# empiece con un numero ejemplo: "10_funciones"



import my_module
from my_module import PrintValue, sum


my_module.sum(5, 3, 1) 
my_module.PrintValue("Hola Mundo :D")


sum(5, 3, 1)
PrintValue("Hola Mundo :D")

import math

print(math.pi)
print(math.sin(1))
print(math.cos(1))
print(math.pow(2, 8))

from math import pi as PI_VALUE

print(PI_VALUE)

