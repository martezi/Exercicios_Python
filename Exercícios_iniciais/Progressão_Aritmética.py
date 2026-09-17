print('=======================\n'
      '10 TERMOS DE UMA PA\n'
      '=======================')
p1=int(input('Primeiro termo: '))
r=int(input('Razão: '))
for c in range(1,p1+1,r):
    print('{} -> '.format(c),end='')
    if c%p1==0:
        print('ACABOU')