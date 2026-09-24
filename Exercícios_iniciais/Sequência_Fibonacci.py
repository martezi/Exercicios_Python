print('==============================')
print('   Sequência de Fibonacci')
print('==============================')
t=int(input('Quantos termos você quer mostrar? '))
c=0
a=0
b=1
while c<t:
    print(a,end=' -> ')
    a,b=b,a+b
    c+=1
    if c==t:
        print('FIM')
        r=str(input('Deseja continuar? [S/N]: ')).upper()
        if r=='S':
            c=0
            t=int(input('Quantos termos deseja ver a mais? '))
        else:
            break
print('Obrigado por utilizar o programa!')