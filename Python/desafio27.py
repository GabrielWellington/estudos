"""nome = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu ultimo nome é: {nome[-1]}')"""

"""nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Seu primeiro nome é {n[0]}, e seu ultimo nome é {n[-1]}')
print(f'Portanto seu nome de guerreiro será: {n[0]} {n[-1]}')"""

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu ultimo nome é: {n[len(n)-1]}')

