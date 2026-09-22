import random
r=random.randint(1,10)
t=1
print('Sou seu computador...\n'
      'Acabei de pensar em um número de 0 a 10.\n'
      'Consegue advinhar?')
p=int(input('Então vamos começar. Qual seu palpite? '))
while p!=r:
    if p<r:
        p=int(input('Quase.. Um pouco mais. Tente novamente: '))
        t+=1
    elif p>r:
        p=int(input('Quase.. Um pouco menos. Tente novamente: '))
        t+=1
if p==r:
    if t<=5:
        print('Aeeeee, acertou!\n'
              'Você conseguiu na {} tentativa. está muito bom!'.format(t))
    elif t>=6:
        print('Cacete, finalmente hein!\n'
              'Você foi péssimo, acertou só na {} tentativa!\n'
              'Mas parabéns, eu acho...'.format(t))