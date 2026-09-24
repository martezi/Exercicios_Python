print('GERADOR DE PA\n'
      '=-=-=-=-=-=-=-=-=-=-=-')
p1=int(input('Primeiro termo: '))
p2=int(input('Segundo termo: '))
c=0
r=10
t=0
while c<r:
    print(p1, end=' -> ')
    p1+=p2
    c+=1
    t+=1
    if c==r:
        print(end='PAUSA')
        print()
    if c==r:
        r=0
        r=int(input('Quantos termos você quer mostrar a mais? '))
        c=0
print('Progressão finalizada com {} termos mostrados.'.format(t))