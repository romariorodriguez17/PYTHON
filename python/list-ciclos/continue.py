#lista de tareas con continue 

tareas_realizar = ["tarea1", "tarea2", "tarea3", "tarea4"]

for tarea in tareas_realizar:
    if tarea == "tarea2":
        continue
    print("Realizando:", tarea)


## ejemplo con continue 
# Example 1: Skip even numbers
for num in range(1, 6):
  if num % 2 == 0:
    continue
  print(f"Odd number: {num}")

# Example 2: Skip empty strings
names = ["John", "", "Alice", "", "Bob"]
for name in names:
  if name == "":
    continue
  print(f"Processing name: {name}")

# Example 3: Skip negative numbers
numbers = [1, -2, 3, -4, 5]
sum_positive = 0
for n in numbers:
  if n < 0:
    continue
  sum_positive += n
print(f"Sum of positive numbers: {sum_positive}")