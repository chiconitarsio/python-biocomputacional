#a
def soma(numero):

    numero = int(input('Digite um numero:'))

    soma = 0
    for i in str(numero):
        soma += int(i)
    return soma

a = int(input('Digite um numero: '))
print('Soma:', soma(a))

#b
lista = []
dic = {}

dic['valor'] = int(input('Digite um valor:'))
dic['chave'] = input('Nome:')

lista.append(dic)

for i,j in dic.items():
    print(i,' ',j)




