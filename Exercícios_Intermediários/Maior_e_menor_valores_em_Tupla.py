import random
n=(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),
   random.randint(1,10))
print(f'''Os números sorteados foram: {n}
O maior valor sorteado foi: {max(n)}
O menor valor sorteado foi: {min(n)}''')
