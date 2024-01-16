nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome todo maiusculo é:',nome.upper())
print('Seu nome todo minusculo é:',nome.lower())
n1 = len(''.join(nome.split()))
print(f'Seu nome tem {n1} letras ao todo.')
nome1 = nome.split()
n2 = len(nome1[0])
print(f'Seu primeiro nome é {(nome1[0])} e tem {n2} letras.')



