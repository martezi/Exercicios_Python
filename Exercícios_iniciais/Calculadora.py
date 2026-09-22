so=0
c=1
while c==1:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    re = int(input('       [ 1 ] Somar\n'
                   '       [ 2 ] Multiplicar\n'
                   '       [ 3 ] subtrair\n'
                   '       [ 4 ] Dividir\n'
                   '       [ 5 ] Sair do programa\n'
                   '>>>>>>>>> Qual é a sua escolha? '))
    if re==1:
        so=n1+n2
        print('A soma entre {} + {} é {}'.format(n1,n2,so))
        so=0
    elif re==2:
        so=n1*n2
        print('A multiplicação entre {} x {} é {}'.format(n1,n2,so))
        so=0
    elif re==3:
        so=n1-n2
        print('A subtração entre {} x {} é {}'.format(n1,n2,so))
        so=0
    elif re==4:
        so=n1/n2
        print('{} dividido por {} é {}'.format(n1,n2,so))
    elif re==5:
        c+=1
    else:
        print('Selecione uma opção válida!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
      'Obrigado por utilizar a calculadora!')