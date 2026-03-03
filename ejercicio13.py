
precio_producto = int(input("Ingrese el precio del producto: "))
porcentaje = 10

if precio_producto > 100000:
    descuento = precio_producto * (porcentaje/100)
    print("Precio final con descuento del 10%:", descuento)
    
else:
    print("No hay descuento")
    print("Precio final:",precio_producto)