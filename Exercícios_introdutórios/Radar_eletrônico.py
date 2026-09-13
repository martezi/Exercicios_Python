print('O limite de velocidade é de 80km/h\n'
      'A multa é de 7 reais pra cada km acima do permitido')
v=(int(input('Qual a velocidade do seu carro? ')))
if v>=80:
    print('Seu carro foi multado')
    print('A multa a pagar é de {}'.format((v-80)*7))
else:
    print('Você está na velocidade permitida. Parabéns!')


