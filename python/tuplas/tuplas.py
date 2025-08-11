## tuplas son elementos que inmutables que no podemos modificar , mantienen el orden 

# 1 Crear una tupla
mi_tupla = ("manzana", "banana", "cereza")
print(mi_tupla)  # ('manzana', 'banana', 'cereza')

# 2 Tupla con datos de diferentes tipos
mi_tupla2 = (25, "Hola", True, 3.14)
print(mi_tupla2)

# 3 Acceder a elementos por índice
print(mi_tupla[0])  # manzana
print(mi_tupla[-1]) # cereza

# 4 Tupla con un solo elemento (importante la coma final)
una_tupla = ("manzana",)  
print(type(una_tupla))  # <class 'tuple'>

# 5 Conversión de lista a tupla
mi_lista = [1, 2, 3]
tupla_convertida = tuple(mi_lista)
print(tupla_convertida)  # (1, 2, 3)

# 6 Contar elementos y obtener índice
print(mi_tupla.count("banana"))  # 1
print(mi_tupla.index("cereza"))  # 2
