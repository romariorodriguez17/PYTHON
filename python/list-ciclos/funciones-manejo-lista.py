## funciones para manejo de listas 

## cambiar elementos de una lista

mis_frutas = ["manzana", "banana", "cereza"]
mis_frutas[1] = "kiwi"
print(mis_frutas)

## añadiendo un nuevo elemento 
mis_frutas.append("naranja")
print(mis_frutas)

##eliminando elemento de la lista 

mis_frutas.remove("manzana")
print(mis_frutas)


## eliminando el ultimo elemento de la lista

mis_frutas.pop()
print(mis_frutas)


## ordenando la lista en orden alfabetico 

mis_frutas.sort()
print(mis_frutas) 

### ejemplos adicionales 

# Lista inicial para ejemplos
numeros = [4, 2, 7, 1, 3, 7]

# 1 insert(posición, valor) → Inserta en una posición específica
numeros.insert(2, 99)  # Inserta el número 99 en la posición 2 (índice empieza en 0)
print("Insert:", numeros)  # [4, 2, 99, 7, 1, 3, 7]

# 2 extend(otra_lista) → Agrega todos los elementos de otra lista
numeros.extend([8, 9, 10])
print("Extend:", numeros)  # [4, 2, 99, 7, 1, 3, 7, 8, 9, 10]

# 3 count(valor) → Cuenta cuántas veces aparece un valor
print("Count (7):", numeros.count(7))  # 2 veces aparece el 7

# 4 index(valor) → Devuelve el índice de la primera ocurrencia
print("Index (99):", numeros.index(99))  # 2

# 5 reverse() → Invierte el orden de la lista
numeros.reverse()
print("Reverse:", numeros)

# 6 copy() → Crea una copia superficial de la lista
copia_numeros = numeros.copy()
print("Copy:", copia_numeros)

# 7 clear() → Elimina todos los elementos de la lista
copia_numeros.clear()
print("Clear:", copia_numeros)  # []

# 8 sorted(lista) → Devuelve una nueva lista ordenada sin modificar la original
print("Sorted:", sorted(numeros))  # Lista ordenada temporalmente
print("Original sigue igual:", numeros)

# 9 pop(indice) → Elimina y devuelve el elemento en un índice específico
valor_eliminado = numeros.pop(3)  # Elimina el valor en índice 3
print("Pop con índice:", valor_eliminado, numeros)

# 10 slicing (no es método, pero muy útil) → Obtener sublistas
print("Slice 2:5", numeros[2:5])  # Elementos desde índice 2 hasta 4
print("Slice inverso", numeros[::-1])  # Lista invertida