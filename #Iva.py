#Iva
IVA = 0.15                              
DESCUENTO = 0.10                       

precio = float(input("Precio sin IVA: $"))


monto_descuento = precio * DESCUENTO
precio_con_descuento = precio - monto_descuento

iva = precio_con_descuento * IVA

total = precio_con_descuento + iva

print(f"Descuento: ${monto_descuento:.2f}")
print(f"IVA:       ${iva:.2f}")
print(f"Total:     ${total:.2f}")