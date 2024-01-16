salario = float(input('Qual salário do funcionario? R$: '))
if salario <= 1250:
    s = salario * 0.15 + salario
    print(f'Quem ganhava R${salario:.0f}, passa a ganhar R${s:.2f}')
else:
    var = salario > 1250
    s = salario * 0.10 + salario
    print(f'Quem ganhava R${salario:.0f}, passa a ganhar R$: {s:.2f}')

# Forma do Guanabara para calcular porcentagem:
# s = salario + (salario * 15 / 100)
# s = salario + (salario * 10 / 100)


