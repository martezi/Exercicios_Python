c=0
n=0
s=0
t=0
while c!=999:
    t+=1
    s += n
    n=int(input('Digite um número [999 pra parar]: '))
    if n==999:
        n=n-999
        t-=1
        break
print('Você digitou {} valores!\n'
      'Todos os valores somados foi: {}'.format(t,s))


