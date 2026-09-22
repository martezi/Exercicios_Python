import math
n=int(input('Digite um número para descobrir o fatorial: '))
print('Calculando o fatorial de {}!'.format(n))
c=n
print('Calculando {}! = '.format(n),end='')
while c>0:
    if c > 1:
        print(c, end=' x ')
    else:
        print(c, end=' = ')
        print(math.factorial(n), end='')
    c-=1
