velocidade = int(input('Digite sua velocidade: '))
if velocidade > 110:
    multa = (velocidade - 110) * 5
    print('Sua multa � R$ %d.' %multa)
if velocidade <= 110:
    print('Voc� n�o foi multado. Parab�ns!')    
