from math import sqrt
def suma(x, y):
    return x + y
#==================
def resta(x, y):
    return x - y
#==================
def multipli(x, y):
    return x * y
#==================
def divi(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("error")
#==================
def exp(x, y):
    return  pow(x, y)
#==================
def cuadratica(A, B, C):
    if ((B**2)-4*A*C) < 0:
        print("La solución de la ecuación es con numeros complejos")
    else:
        x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)  # Fórmula de Bhaskara parte positiva
        x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)  # Fórmula de Bhaskara parte negativa
        return x1