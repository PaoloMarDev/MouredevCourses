### Bucles ###

# While


my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")


print("La ejecución continúa")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es igual a 15")
        print("Se detiene la condición")
        break

    print("Mi condición es menor que 20")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]
my_tuple = (21, 1.7, "Paolo", "Martini", "Paolo")
my_dict = { "Nombre" : "Paolo",
            "Apellido": "Martini",
            "Edad": 21,
            "Lenguajes": {"Python", "Swift", "Kotlin"},
            1: 1.70}
my_set = {"Paolo", "Martini", 21}


for element in my_list:
    print(element)


for element in my_set:
    print(element)

for element in my_tuple:
    print(element)

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario ha finalizado")



for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

