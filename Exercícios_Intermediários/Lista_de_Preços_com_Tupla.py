p=('Lápis','1.75','Borracha','2.00','Caderno','20.00','Estojo','14.00','Transferidor','4.20','Compasso','9.99','Mochila',
   '45.99','Canetas','22.30','Livro','34.90')
print(f'''{'=-='*10}
{'lISTAGEM DE PREÇO':^28}
{'=-='*10}
{''}
{'-'*40}''')
for c in range(0,len(p),2):
    print(f'{p[c]:.<30}R$ {p[c+1]}')
