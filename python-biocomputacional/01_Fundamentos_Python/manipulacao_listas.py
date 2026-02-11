#a
def remover_duplicados(valor,lista):
    valor = lista(set(lista))

    return remover_duplicados

lista2 = [1,1,1,2,3,4,5,5]
a = remover_duplicados(lista2)
print(a)

#b
def comparar(lista):
    if not lista:
        return None, None

    maior = menor = lista[0]

    for num in lista:
        if num > maior:
            num = maior
        elif num < menor:
            menor = num
        return maior, menor
    
lista = [1,2,3,6,5,1]
maior_num, menor_num = comparar(lista)

lista = [1,2,3,4,5,6]
print(f'Maior: {maior_num}')
print(f'Menor: {menor_num}')

