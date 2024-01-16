n1 = int(input('Qual a distancia da sua viagem? Em Km: '))
print(f'Voce esta prestes a começar uma viagem de {n1}Km')
if n1 <= 200:
    s = n1 * 0.50
    print(f'E o preço da sua passagem será de R${s:.2f}')
else:
    s2 = n1 * 0.45
 # s2 = n1 * 0.50 if n1 <= 200 else n1 * 45
    print(f'E o preço da sua passagem será de R${s2:.2f}')

