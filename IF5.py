minutos = int(input('Digite os minutos utilizados: '))
if minutos < 200:
    preco = 0.2
else:
     if minutos <= 400:
         preco = 0.18
     else:
         if minutos <= 800:
             preco = 0.15
         else:
             preco = 0.08
print('Sua conta é %6.2f' %(preco * minutos))
