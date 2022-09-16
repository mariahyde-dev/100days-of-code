print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Bem vindo a Ilha do Tesouro!")
print("Sua missão é encontrar o tesouro perdido.")
escolha1 = input(
    'Você está em uma encruzilhada, para onde você quer ir? Digite "esquerda" ou "direita".\n').lower()

if escolha1 == "esquerda" or escolha1 == "Esquerda":
    # Continua no jogo.
    escolha2 = input(
        'Você chegou em um lago. Há uma ilha no meio do lago. Escreve "esperar" para esperar por um barco. Digite "nadar" para atravessar nadando. \U0001F603 \n').lower()
    if escolha2 == "esperar":
        escolha3 = input(
            'Ufa! Você chegou à ilha ileso, há uma casa com 3 portas; uma vermelha, uma amarela e uma azul. Qual cor você escolhe? \U0001F914 \n').lower()
        if escolha3 == "vermelha":
            print("É um quarto pegando fogo, bicho! Game over! \U0001F525")
        elif escolha3 == "amarela":
            print("Você encontrou o tesouro! Você GANHOU!!!! \U0001F4B0 \U0001F389")
        elif escolha3 == "azul":
            print("Você entrou em um quarto cheio de zumbis. Game over \U0001F9DF")
        else:
            print("Você escolheu uma porta que não existe. Game over \U0001F611")
    else:
        print("Você foi atacado por uma piranha raivosa. Game over! \U0001F611")
else:
    print("Você caiu em um buraco. Game over! \U0001F611")
