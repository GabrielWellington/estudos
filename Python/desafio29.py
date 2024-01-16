velocidade = int(input('Qual a velocidade atual do carro?: '))
if velocidade > 80:
    print('Voce foi multado por ultrapassar a velocidade permitida de 80km/h')
    multa = (velocidade - 80) * 7.00
    print(f'Voce devera pagar uma multa no total de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')



