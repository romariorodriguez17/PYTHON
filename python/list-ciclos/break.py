numeros = [1, 2, 4, 3, 5, 6]
encontrado = False

for numero in numeros:
    if numero == 3:
        print(f"¡El número {numero} ha sido encontrado!")
        encontrado = True
        break  # Esto detiene el ciclo inmediatamente
    print(f"Revisando el número: {numero}")

if encontrado:
    print("La búsqueda ha terminado exitosamente.")


for segundo in range(20):
    if segundo == 12:
        print("debes detener el ciclo")
        break
    print(f"Segundo actual: {segundo}")


## while con break 

while True:
    entrada = input("Ingresa un número (o 'salir' para terminar): ")
    if entrada.lower() == "salir":
        print("Saliendo del programa.")
        break  # El break termina el bucle
    try:
        numero = int(entrada)
        print(f"Ingresaste el número: {numero}")
    except ValueError:
        print("Entrada no válida, por favor, ingresa un número.")

print("El programa ha finalizado.")

## otro ejemplo de break con for 

numeros = [1, 3, 5, 7, 9, 11]

for numero in numeros:
    print("Viendo el número:", numero)
    if numero == 7:
        print("¡Encontramos el 7! Deteniendo el ciclo.")
        break
    print("Ciclo terminado.") 

# Ejemplo de uso de break en un ciclo for

productos = ["manzana", "pera", "naranja", "mango"]

buscado = "naranja"
for producto in productos:
    if producto == buscado:
        print(f"{buscado} encontrado.")
        break



#ejemplo de uso de break en un ciclo while

numero = 1

while numero <= 10:
    print("Probando con:", numero)
    if numero % 4 == 0:
        print(f"{numero} es divisible por 4. ¡Alto!")
        break
    numero += 1
print("Ciclo completado sin interrupciones.")


# Ejemplo de uso de break en un ciclo while

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("El bucle terminó sin usar break")
print("El bucle terminó con break")