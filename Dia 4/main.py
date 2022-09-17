import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagens_jogo = [pedra, papel, tesoura]

escolha_usuario = int(input(
    "Qual você escolhe? Digite 0 para pedra, 1 para papel ou 2 para tesoura.\n"))
print(imagens_jogo[escolha_usuario])

escolha_computador = random.randint(0, 2)
print("O computador escolheu: ")
print(imagens_jogo[escolha_computador])

if escolha_usuario >= 3 or escolha_usuario < 0:
    print("Você digitou um número inválido. Você perdeu!")
elif escolha_usuario == 0 and escolha_computador == 2:
    print("Você ganhou!")
elif escolha_computador == 0 and escolha_usuario == 2:
    print("Você perdeu!")
elif escolha_computador > escolha_usuario:
    print("Você perdeu!")
elif escolha_usuario > escolha_computador:
    print("Você ganhou!")
elif escolha_computador == escolha_usuario:
    print("Foi um empate")
elif escolha_usuario >= 3:
    print("Você digitou um número inválido. Você perdeu!")
