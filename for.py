print('*******************')
print('Jogo de Adivinhação')
print('********************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
  print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
  chute = input('Informe um número entre 1 e 100:')
  print('Você digitou: ', chute)
  chute_int = int(chute)

  if (chute_int < 1 or chute_int > 100):
    print('Você deve digitar um número entre 1 e 100!')
    continue

  acertou = chute_int == numero_secreto
  maior = chute_int > numero_secreto
  menor = chute_int < numero_secreto
  if (acertou):
    print('Você acertou')
    break
  else:
    if (maior):
      print('Você errou! O seu chute foi maior que o número secreto.')
    elif (menor):
      print('Você errou! O seu chute foi menor que o número secreto')
print('Fim de jogo')
