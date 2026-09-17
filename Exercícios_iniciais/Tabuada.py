t=0
n=int(input('Digite um número pra ver sua tabuada: '))
for c in range(1,11):
    t=n*c
    print('{} x {} = {}'.format(n,c,t))