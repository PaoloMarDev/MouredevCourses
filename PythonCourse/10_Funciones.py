### Funciones ###

def my_function():
    print("Esto es una funcion")


my_function()
my_function()
my_function()


def sum_two_values(first_num, second_num):
    print(first_num + second_num)

sum_two_values(5, 7)
sum_two_values(3643, 34653)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_num, second_num):
    my_sum =  first_num + second_num
    return my_sum

my_result = sum_two_values_with_return(10, 5)

print(my_result)


def print_name(name, surname):
    print(f"Mi nombre es: {name} y mi apellido es: {surname}")

print_name("Paolo", "Martini")
print_name(surname = "Martini", name = "Paolo")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Paolo", "Martini", "Alien300")
print_name_with_default("Paolo", "Martini")


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper()) 

print_upper_texts("Hola", "Python", "Mourdev", "Alien300", "Alien300")
