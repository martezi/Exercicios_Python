import math
tf=0
m=0
me=0
mv=0
for c in range(1,5):
    print ('=-=-=-=-= {}ᵃ PESSOA -=-=-=-=-='.format(c))
    n=str(input('Nome: '))
    i=int(input('Idade: '))
    me+=i
    s=str(input('Sexo [M/F]: '))
    if s=='f' and i<=20:
        tf=tf+1
    if i>=m:
        m=i
        mv=n
print('=-=-=-==-=-=-==-=-==-=-=-==-=-=-=-==-=-=-==-=-')
som=me/4
print('- A média da idade das quatro pessoas é {} anos. Arredondando para cima, fica {} anos'.format(som,math.ceil(som)))
print('- A pessoa mais velha tem {} anos, e se chama {}'.format(m,mv))
if tf==1:
    print('- Ao todo tem uma mulher no grupo, que tem menos de 20 anos.'.format(tf))
elif tf>=2:
    print('- Ao todo são {} mulheres no grupo, que tem menos de 20 anos.'.format(tf))
else:
    print('- Não tem mulheres no grupo que tem menos de 20 anos.')
print('=-=-=-==-=-=-==-=-==-=-=-==-=-=-=-==-=-=-==-=-')