try:
    # 1. Leer la entrada del usuario
    texto = input("Monto: $")
    
    # 2. Limpiar la entrada (reemplaza coma por punto y quita espacios o signo $)
    texto_limpio = texto.replace("$", "").replace(",", ".").strip()
    
    # 3. Convertir a número decimal
    monto = float(texto_limpio)

    # 4. Convertir a centavos enteros para evitar imprecisiones
    resto = round(monto * 100)

    # Desglose de billetes
    b50 = resto // 5000
    resto = resto % 5000

    b20 = resto // 2000
    resto = resto % 2000

    b10 = resto // 1000
    resto = resto % 1000

    b5 = resto // 500
    resto = resto % 500

    b1 = resto // 100
    resto = resto % 100

    # Desglose de monedas
    m25 = resto // 25
    resto = resto % 25

    m10 = resto // 10
    resto = resto % 10

    m5 = resto // 5
    resto = resto % 5

    m1 = resto // 1
    resto = resto % 1

    # Imprimir resultados
    print(f"$50.00 × {b50}")
    print(f"$20.00 × {b20}")
    print(f"$10.00 × {b10}")
    print(f"$5.00  × {b5}")
    print(f"$1.00  × {b1}")
    print(f"$0.25  × {m25}")
    print(f"$0.10  × {m10}")
    print(f"$0.05  × {m5}")
    print(f"$0.01  × {m1}")

except ValueError:
    print("Error: Ingresa un número válido (ejemplo: 87.35 o 50).")
