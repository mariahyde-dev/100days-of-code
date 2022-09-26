# Gerador de senhas
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v' 'x', 'z', 'A', 'B', 'C',
          'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
          'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '(', ')', '*', '+']

print("Bem vindo ao gerador de senhas!")
n_letras = int(input("Quantas letras você quer na sua senha?\n"))
n_simbolos = int(input("Quantos símbolos você quer na sua senha?\n"))
n_numeros = int(input("Quantos números você quer na sua senha?\n"))

senha = ""
for caractere in range(1, n_letras + 1):
    senha += random.choice(letras)

for caractere in range(1, n_simbolos + 1):
    senha += random.choice(simbolos)

for caractere in range(1, n_numeros + 1):
    senha += random.choice(numeros)

print(senha)
