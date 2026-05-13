import math

# mostra o valor de pi
print("Valor de pi:", math.pi)

# pergunta quantas casas decimais o usuário quer
casas = int(input("Quantas casas decimais você quer arredondar? "))

# arredonda o valor de pi
pi_arredondado = round(math.pi, casas)

# mostra o resultado
print("Pi arredondado:", pi_arredondado)

#outro jeito sem import
c = int(input("Digite o valor de c(circunferência): "))
d = int(input("Digite o valor de d(diâmetro): "))
pi = c / d
print("Valor de pi:", pi)
casas = int(input("Quantas casas decimais você quer arredondar? ")) 
pi_arredondado = round(pi, casas)
print("Pi arredondado:", pi_arredondado)
