# Analisando o tamanho do nome

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 5:
    print(f'{nome} é um nome curto')
elif tamanho <= 7:
    print(f'{nome} é um nome de tamanho médio')
else:
    print(f'{nome} é um nome longo')