p=float(input('Qual é o seu peso? (kg) '))
a=float(input('Qual é a sua altura? (m) '))
imc=p/(a**2)
print('Seu IMC é de {:.1f}5'.format(imc))
if imc>=40:
    print('Está em Obesidade Mórbida.\n'
          'Procure ajuda imediatamente.')
elif imc>=30 and imc<=39:
    print('Está em Obesidade.')
elif imc>=25 and imc<=29:
    print('Está em Sobrepeso.')
elif imc>=18.5 and imc<=24:
    print('Está em seu peso ideal.\n'
          'Parabéns!')
else:
    print('Está abaixo do peso.')
