print('*******************')
print('Jogo de Adivinhação')
print('********************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
  print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
  chute = input('Informe seu número:')

  print('Você digitou: ', chute)
  chute_int = int(chute)

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
  rodada = rodada + 1

print('Fim de jogo')
