print("Bem vindo a calculadora de gorjetas!")
total = float(input("Qual o valor total da conta?\n"))
gorjeta = int(input("Quanto você deseja dar de gorjeta? 10, 12 ou 15%?\n"))
pessoas = int(input("Quantas pessoas vão dividir a conta?\n"))
porcentagem_gorjeta = gorjeta / 100
total_gorjetas = total * porcentagem_gorjeta
total_conta = total + total_gorjetas
total_por_pessoa = total_conta / pessoas
total_final = round(total_por_pessoa, 2)
print("Cada pessoa deverá pagar {} reais.".format (total_final))