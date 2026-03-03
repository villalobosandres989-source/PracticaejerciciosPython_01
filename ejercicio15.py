
sueldo_mensual = int(input("Cual es su sueldo mensual: "))
if sueldo_mensual< 1500000:
    print("No pagas impuestos")
    print("Sueldo neto:", sueldo_mensual)
    
elif 1500000 <= sueldo_mensual <= 3000000:
    impuesto = sueldo_mensual * 0.05
    print("Usted paga", impuesto, "en impuestos")
    print("Sueldo neto:", sueldo_mensual - impuesto)

elif sueldo_mensual> 3000000:
    impuesto = sueldo_mensual * 0.1
    print("Usted paga", impuesto, "en impuestos")
    print("Sueldo neto:", sueldo_mensual - impuesto)