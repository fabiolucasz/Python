c = float(input('Cigarros por dia: '))
a = float(input('Quantos anos fumando? '))

total = c * 365 * a
dias = total / 144

print (f'Você perdeu {dias:.2f} dias')
