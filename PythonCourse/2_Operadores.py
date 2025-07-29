### Operadores Aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 4) 
print(10 // 4) 
print(10 ** 4) 

print(10 ** 4 + 3 - 7 / 1 // 4) 


print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Python") ### No cuenta la cantidad de caracteres ###
print("Hola" < "Python") ### sino el orden alfabético ###
print("Hola" >= "Python")
print(len("Hola") >= len("Python")) ### Cuenta de caracteres
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python") # &&
print(3 > 4 or "Hola" > "Python") # ||

print(3 < 4 and "Hola" < "Python") # &&
print(3 < 4 or "Hola" < "Python") # ||

print(not (3 > 4)) # !

