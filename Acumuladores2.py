n = 1
soma = 0
while n <= 10:
    x = int(input('Digite o %d� n�mero: ' %n))
    soma = soma + x
    n = n + 1
print ('M�dia: %5.2f' %(soma/10))
