#base por altura
import math

# --- Cálculo del Rectángulo ---
base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura                
perimetro = 2 * (base + altura)     

print(f"Área del rectángulo: {area:.2f}")
print(f"Perímetro del rectángulo: {perimetro:.2f}")
print("-" * 25)

radio = float(input("Radio del círculo: "))

area_circulo = math.pi * (radio ** 2)      
perimetro_circulo = 2 * math.pi * radio    

print(f"Área del círculo: {area_circulo:.2f}")
print(f"Perímetro del círculo: {perimetro_circulo:.2f}")