peso = float(input('Seu peso:'))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 5
else:
    multa = excesso = 0
        
print (f'Você está {excesso:.2f}Kg acima do permitido!')
print (f'Sua multa é de {multa:.2f}.')
