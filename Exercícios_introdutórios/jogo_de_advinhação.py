import random
n = random.randint(1, 5)
r=int(input('Qual o número escolhido pelo computador de 1 a 5? '))
if r==n:
    print('Acertou! o número escolhido era mesmo {}'.format(n))
else:
    print('Errou! o número escolhido era na verdade foi o {}'.format(n))