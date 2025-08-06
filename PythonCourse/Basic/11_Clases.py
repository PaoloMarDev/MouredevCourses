### Clases ###

class MyEmptyPerson:
    pass



print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.__name = name # Esto es que es privado en vez de público
        self.__surname = surname # Esto es que es privado en vez de público
        self.full_name = f"{name} {surname} ({alias})"
    
    def walk(self):
        print(f"{self.full_name} está caminando")

    def get_name(self):
        return self.__name


my_person = Person("Paolo", "Martini")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)
print(my_other_person.get_name())
