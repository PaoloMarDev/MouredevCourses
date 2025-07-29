### Strings ###

my_str = "Mi String"
my_other_str = 'Mi String'

print(len(my_str))
print(len(my_other_str))

print(my_str + " " + my_other_str)

my_new_line_str = "Este es un String\ncon salto de linea"
print(my_new_line_str)

my_tab_str = "\tEste es un String con tabulación"
print(my_tab_str)

my_scape_str = "\\tEste es un String \n escapado"
print(my_tab_str)

# Formateo

name, surname, age = "Paolo", "Martini", 21

print("Mi nombre es {} {} y mi edad es {} ".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d " %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[1:3]
print(language_slice)


language_slice = language[1]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)


# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))



