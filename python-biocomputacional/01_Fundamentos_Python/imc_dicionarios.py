lista = []

def tabela_imc(imc):
    if imc < 24.9:
        print('Peso normal')
    elif imc > 25 and imc < 29.9:
        print('Sobrepeso')
    else:
        print('Obesidade')   

def imc(peso, altura):
    return peso / (altura**2)

dic = {}

dic['nome'] = input('Digite o nome:')
dic['sexo'] = input('sexo:')
dic['peso'] = input('Peso:')
dic['altura'] = input('Altura:')

imc_pessoa = imc(dic['peso'], dic['altura'])
dic['imc'] = imc_pessoa

lista.append(dic)

situacao = tabela_imc(imc_pessoa)

for i in lista.remove(imc_pessoa):
    print(lista)

print(f'Imc: {imc_pessoa:.2f}')
print(situacao)
