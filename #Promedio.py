#Promedio
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1 + n2 + n3) / 3      # PROCESO en una línea
print(f"Promedio: {promedio:.1f}")  # :.1f muestra un decimal
if promedio >= 7:
    print("Aprueba")
else:
    print("Reprueba")