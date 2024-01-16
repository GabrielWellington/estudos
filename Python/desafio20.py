"""import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
r = random.shuffle(lista)
print(f'A ordem de apresentação será:\n{lista}\n')"""

"""from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será')
print(lista)"""

from random import shuffle
import emoji

print('Digite o nome dos alunos presentes.')

al1 = str(input('Aluno 01: '))
al2 = str(input('Aluno 02: '))
al3 = str(input('Aluno 03: '))
al4 = str(input('Aluno 04: '))
lista = [al1, al2, al3, al4]
shuffle(lista)

print(emoji.emojize('A lista de apresentação dos trabalhos é: {}.\nBoa sorte. ^^ :honeybee:'.format(lista),
                    language='alias'))



