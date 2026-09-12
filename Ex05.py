s=float(input('Qual o salário do funcionário? '))
if s>=1250.00:
    print('Para o seu salário, seu aumento será de 10%\n'
          'Novo salário: {:.2f}'.format(s*1.10))
else:
    print('Como seu salário está abaixo do nosso padrão de 1250 reais\n'
          'Receberá um aumento de 15%\n'
          'Novo salário: {:.2f}'.format(s*1.15))
