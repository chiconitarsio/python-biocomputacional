import numpy as np  
from scipy.special import factorial  

def sinh_taylor(x, termos=50):  
    n = np.arange(termos)  
    return np.sum((x**(2*n + 1)) / factorial(2*n + 1))  

def cosh_taylor(x, termos=50):  
    n = np.arange(termos)  
    return np.sum((x**(2*n)) / factorial(2*n))  

x = float(input("Digite x: "))  
sinh_valor = sinh_taylor(x)  
cosh_valor = cosh_taylor(x)  

print(f"sinh({x}) = {sinh_valor}")  
print(f"cosh({x}) = {cosh_valor}")  
print(f"cosh²({x}) - sinh²({x}) = {cosh_valor**2 - sinh_valor**2}")