### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]


print(my_list)
print(len(my_list))

my_other_list = [21, 1.70, "Paolo", "Martini"]

print(my_other_list)
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Paolo"))


age, height, name, surname = my_other_list
age, height, name, surname = my_other_list[0], my_other_list[1], my_other_list[2], my_other_list[3] 
print(name)

print(my_list + my_other_list)

# Funciones precargadas
my_other_list.append("Alien300")
print(my_other_list)

my_other_list.insert(1, "Morado")
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop()
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)


del my_list[2]
print(my_list)

my_new_list = my_list.copy()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[0:2])



