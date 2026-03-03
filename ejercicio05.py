
num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))
print("Suma:", num1+num2)
print("Resta:", num1-num2)
print("Multiplicacion:", num1*num2)

if num2==0:
    print("Error, no se puede dividir entre cero")
else:
    print("Division:",num1/num2)