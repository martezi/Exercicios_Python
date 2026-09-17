import random
import time
r=int(input('-=-=-=-=-=-=-=-==-=-=-\n'
      '     Suas Opções:\n'
      '-=-=-=-=-=-=-=-==-=-=-\n'
      '[ 1 ] Pedra\n'
      '[ 2 ] Papel\n'
      '[ 3 ] Tesoura\n'
      '-=-=-=-=-=-=-=-==-=-=-\n'
      'Escolha: '))
v=(random.randint(1,3))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!')
time.sleep(1)
if r==1 and v==1:
    print('-=-=-=-=-=-=-=-==-=-=-\n'
          'COMPUTADOR JOGOU PEDRA\n'
          'JOGADOR JOGOU PEDRA\n'
          '-=-=-=-=-=-=-=-==-=-=-\n'
          'EMPATE TÉCNICO!')
elif r==1 and v==2:
    print('-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR JOGOU PAPEL\n'
          'JOGADOR JOGOU PEDRA\n'
          '-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR GANHOU!')
elif r==1 and v==3:
    print('-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR JOGOU TESOURA\n'
          'JOGADOR JOGOU PEDRA\n'
          '-=-=-=-=-=-=-=-=-=-=-=-\n'
          'JOGADOR GANHOU!')
if r==2 and v==1:
    print('-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR JOGOU PEDRA\n'
          'JOGADOR JOGOU PAPEL\n'
          '-=-=-=-=-=-=-=-=-=-=-=-\n'
          'JOGADOR GANHOU!')
elif r==2 and v==2:
    print('-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR JOGOU PAPEL\n'
          'JOGADOR JOGOU PAPEL\n'
          '-=-=-=-=-=-=-=-=-=-=-=-\n'
          'EMPATE TECNICO!')
elif r==2 and v==3:
    print('-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR JOGOU TESOURA\n'
          'JOGADOR JOGOU PAPEL\n'
          '-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR GANHOU!')
if r==3 and v==1:
    print('-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR JOGOU PEDRA\n'
          'JOGADOR JOGOU TESOURA\n'
          '-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR GANHOU!')
elif r==3 and v==2:
    print('-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR JOGOU PAPEL\n'
          'JOGADOR JOGOU TESOURA\n'
          '-=-=-=-=-=-=-=-=-=-=-=-\n'
          'JOGADOR GANHOU!')
elif r==3 and v==3:
    print('-=-=-=-=-=-=-=-=-=-=-=-\n'
          'COMPUTADOR JOGOU TESOURA\n'
          'JOGADOR JOGOU TESOURA\n'
          '-=-=-=-=-=-=-=-=-=-=-=-\n'
          'EMPATE TECNICO!')



