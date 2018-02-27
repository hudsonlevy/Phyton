velocidade = int(input('Digite sua velocidade: '))
if velocidade > 110:
    multa = (velocidade - 110) * 5
    print('Sua multa é R$ %d.' %multa)
if velocidade <= 110:
    print('Você não foi multado. Parabéns!')    
