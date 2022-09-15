print("Bem vindo a calculadora de gorjetas!")
total = float(input("Qual o valor total da conta? R$\n"))
gorjeta = int(input("Quanto de gorjeta você quer dar? 10, 12 ou 15%\n"))
pessoas = int(input("Com quantas pessoas vai ser dividida a conta?\n"))
porcentagem_gorjeta = gorjeta / 100
valor_total_gorjeta = total * porcentagem_gorjeta
total_da_conta = total + valor_total_gorjeta
total_por_pessoa = total_da_conta / pessoas
total_final = round(total_por_pessoa, 2)
print("Cada pessoa deverá pagar {} reais.".format(total_final))