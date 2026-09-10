#impar o par
num = int(input("Ingresa un número: "))


resultado = "par" if num % 2 == 0 else "impar"

if num % 3 == 0 and num % 5 == 0:
    multiplo = "múltiplo de ambos (3 y 5)"
elif num % 3 == 0:
    multiplo = "múltiplo de 3"
elif num % 5 == 0:
    multiplo = "múltiplo de 5"
else:
    multiplo = "no es múltiplo de 3 ni de 5"

print(f"{num} es {resultado} y es {multiplo}.")