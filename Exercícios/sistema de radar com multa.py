velocidade_carro = int(input('Digite a velocidade do carro: '))

if velocidade_carro > 110:
    multa = (velocidade_carro - 110) * 5
    print(f' Multado! Valor da multa: R${multa:.2f}')
