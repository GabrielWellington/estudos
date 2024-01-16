from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar') # Faz o computador "PENSAR" em um numero
print('-=-' * 20)
a = randint(0, 5)
n1 = int(input('Em que numero pensei?: ')) # Jogador tenta adivinhar o numero
print('PROCESSANDO...')
sleep(2)
if a == n1:
    print('PARABÉNS VOCE ACERTOU!!')
else:
    print(f'Voce errou! Eu pensei no número {a} e não no {n1}')