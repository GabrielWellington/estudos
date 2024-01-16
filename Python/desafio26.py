"""frase = str(input('Digite uma frase: ')).strip().upper()
a = frase.count('A')
print(f'A letra A aparece {a} vezes')
p2 = frase.find('A')+1
print(f'A primeira letra "A" apareceu na posição {p2}')
p3 = frase.rfind('A')+1
print(f'A ultima letra "A" aparece na posição {p3}')"""

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A frase tem {frase.count("A")} letra A')
print(f'A letra A aparece a primeira vez na {frase.find("A")+1}º posição')
print(f'A letra A aparece a ultima vez na {frase.rfind("A")}º posição')

