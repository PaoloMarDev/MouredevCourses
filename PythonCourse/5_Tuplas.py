### Tuplas ###

# (listas inmutables, o sea no pueden cambiar)
my_tuple = tuple()
my_other_typle = (35, 60, 30)


my_tuple = (21, 1.7, "Paolo", "Martini", "Paolo")
print(my_tuple)
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Paolo"))
print(my_tuple.index("Martini"))


my_sum_tuple = my_tuple + my_other_typle
print(my_sum_tuple)
 
print(my_sum_tuple[3:6])


my_tuple = list(my_tuple)
print(type(my_tuple))


my_tuple[4] = "BlackCatDev"
my_tuple.insert(1,"Morado")
print(my_tuple)
print(tuple(my_tuple))

del my_tuple[2]

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined