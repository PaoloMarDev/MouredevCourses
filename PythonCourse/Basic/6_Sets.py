### Sets ###

# Lista que no puede tener valores repetidos

my_set = set()
my_other_set = {}


print(type(my_set))
print(type(my_other_set))

my_other_set = {"Paolo", "Martini", 21}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Alien300")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Alien300") # Un set no admite repetidos

print(my_other_set) 

print("Paolo" in my_other_set)
print("paolo" in my_other_set)

my_other_set.remove("Paolo")
print(my_other_set) 

my_other_set.clear()
print(my_other_set) 
print(len(my_other_set)) 

del my_other_set
# print(my_other_set) Error porque eliminamos el objeto 

my_set = {"Paolo", "Martini", 21}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Python", "c++", "c#"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JS", "HTML", "CSS"}))

print(my_new_set.difference(my_set))

