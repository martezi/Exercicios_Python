d=int(input('Qual a distância em km da sua viagem? '))
if d<=200:
    v=d*0.50
    print('O valor da viagem ficaria {}'.format(v))
else:
    v=d*0.45
    print('O valor da viagem ficaria {}'.format(v))
