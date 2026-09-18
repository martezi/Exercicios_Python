
n=int(input('Digite um número: '))
tot=0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[34m',end='')
        tot+=1
    else:
        print('\033[31m', end='')
    print('{} '.format(c),end='')
print('\n\033[mO número {} é dividivel {} vezes'.format(n,tot))
if tot == 2:
    print('Portanto, o {} é um número primo'.format(n))
else:
    print('Portanto, o {} não é um número primo'.format(n))