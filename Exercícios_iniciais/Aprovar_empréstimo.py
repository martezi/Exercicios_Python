v=float(input('Qual o valor do imóvel que voce deseja comprar? '))
s=float(input('Qual o seu salário bruto mensal? '))
m=int(input('Deseja parcelar em quantos meses? '))
if s<=v*0.30:
    print('Voce optou em parcelar em {}x sem juros.\n'
          'O valor total a se pagar é de {:.2f} R$ por mês'.format(m,v/m))
else:
    print('Infelizmente o seu salário não cobre 30% do valor do empréstimo.\n'
          'Empréstimo negado!')