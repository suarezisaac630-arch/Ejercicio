#tiempo
tiempo = input("Ingresa el tiempo (hh:mm:ss): ")
horas, minutos, segundos = tiempo.split(":")
total = (int(horas) * 3600) + (int(minutos) * 60) + int(segundos)
print(f"Segundos totales: {total}")