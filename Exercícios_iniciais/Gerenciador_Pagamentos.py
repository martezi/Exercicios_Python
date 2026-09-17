print('=========== LOJA GUANABARA ===========')
p=float(input('Valor total das compras: R$ '))
print('FORMAS DE PAGAMENTO: ')
print('[ 1 ] à vista no dinheiro ou PIX.\n'
      '[ 2 ] à vista no cartão\n'
      '[ 3 ] 2x no cartão.\n'
      '[ 4 ] 3x no cartão ou mais.')
r=int(input('Digite o número da opção desejada: '))
if r==1:
    print('Agradecemos sua compra.\n'
          'Pagamentos a vista recebem 10% de desconto.\n'
          'Sua compra de R$ {:.2f} R$ vai passar a custar R$ {:.2f} no final.\n'
          'Obrigado, e volte sempre!'.format(p,p-(p*(10/100))))
elif r==2:
    print('Agradecemos sua compra.\n'
          'Pagamentos via cartão de crédito ou débito, ganham desconto de 5%.\n'
          'Sua compra de R$ {:.2f} vai passar a custar R$ {:.2f} no final.\n'
          'Obrigado, e volte sempre!'.format(p,p-(p*(5/100))))
elif r==3:
    print('Agradecemos sua compra.\n'
          'Pagamento dividido em 2x sem juros.\n'
          'Total a pagar duas parcelas de R$ {:.2f}.\n'
          'Obrigado, e volte sempre!'.format(p/2))
elif r==4:
    print('Agradecemos sua compra.')
    r2=int(input('Deseja parcelar em até quantas vezes? (Juros se aplicam): '))
    print('Sua compra será parcelada em {} parcelas de R$ {:.2f}, com juros de 20%.\n'
          'Total a pagar: R$ {}\n'
          'Obrigado, e volte sempre!'.format(r2, ((p*(20/100))+p)/r2, (p*(20/100))+p))
else:
    print('Nenhuma das opções selecionadas.\n'
          'Por favor, volte e selecione uma opção desejada.')
