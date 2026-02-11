import math

lista = []

def somatoria_sinh(valor1, valor2, lista):
    valor4 = 2*valor2+1
    valor1 += (1/math.factorial(valor4))*valor1**valor4

    lista.append(valor1)
    
    if valor2 <19:
        a += 1
        return somatoria_sinh(valor1, valor2, lista)
    else:
        return valor1
    
valor1 = 0
valor2 = 0
result = somatoria_sinh(valor1, valor2, lista)
print = (result)
    

