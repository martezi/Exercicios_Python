pr = []
temp = []
m = n = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    c = str(input('Continue? [S/N]: ')).strip().upper()

    if len(pr) == 0:
        m = n = temp[1]
    else:
        if temp[1] > m:
            m = temp[1]
        if temp[1] < n:
            n = temp[1]

    pr.append(temp[:])
    temp.clear()

    if c == 'N':
        break

print(f'{"=-" * 30}')
print(f'Ao todo, você cadastrou {len(pr)} pessoas.')

mai = [p[0] for p in pr if p[1] == m]
men = [p[0] for p in pr if p[1] == n]

if len(mai) > 1:
    nom_mai = ', '.join(mai[:-1]) + ' e ' + mai[-1]
else:
    nom_mai = mai[0]

if len(men) > 1:
    nom_men = ', '.join(men[:-1]) + ' e ' + men[-1]
else:
    nom_men = men[0]

print(f'O maior peso foi {m}kg, e foi o peso de {nom_mai}.')
print(f'O menor peso foi {n}kg, e foi o peso de {nom_men}.')