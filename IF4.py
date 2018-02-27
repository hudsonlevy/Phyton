minutos = int(input('Digite os minutos utilizados: '))
if minutos < 200:
    conta = minutos * 0.2
    print('Sua conta é %6.2f' %conta)
if minutos >= 200 and minutos <= 400:
    conta = minutos * 0.18
    print('Sua conta é %6.2f' %conta)
if minutos > 400:
   conta = minutos * 0.15
   print('Sua conta é %6.2f' %conta)
