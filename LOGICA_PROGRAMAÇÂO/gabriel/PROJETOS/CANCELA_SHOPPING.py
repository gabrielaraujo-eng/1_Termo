# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

print("=============================================================\n")
print("Bem-vindo ao sistema de gerenciamento de cancelas do shopping!\n")
print("=============================================================\n")
  
numerodoveiculoaentrar = 0
tarifa_por_hora = 9.0
print("qual opção deseja escolher? 1 - sem parar, 2 - tiket")
entrada = input("Deseja entrar no shoppingpor qual opção? 1 ou 2? ")
while True:
    if entrada == "1":
        numerodoveiculoaentrar += 1
        
        placa = input(f"Digite a placa do veículo {numerodoveiculoaentrar}: ")
        tempo = float(input("Digite o horario atual: "))
        saida = float(input("Digite o horario de saída: "))
        valor = (saida - tempo) * tarifa_por_hora
    
        print(f"\n----- Dados do Veículo -----")
        print(f"Placa: {placa}")
        print(f"Tempo de permanência: {saida - tempo} horas")
        print(f"Valor a pagar: R${valor}")
        print(f"Você é o {numerodoveiculoaentrar}º veículo a entrar no shopping.\n")
        print("\nEncerrando o sistema. Tenha um bom dia!")
        break

    else:
        print("Opção inválida! Digite '1' ou '2'.\n")
        break

while True:
    if entrada == "2":
        numerodoveiculoaentrar += 1
        
        placa = input(f"Digite a placa do veículo {numerodoveiculoaentrar}: ")
        tempo = float(input("Digite o horario atual: "))
        saida = float(input("Digite o horario de saída: "))
        valor = (saida - tempo) * tarifa_por_hora
    
        print(f"\n----- Dados do Veículo -----")
        print(f"Placa: {placa}")
        print(f"Tempo de permanência: {saida - tempo} horas")
        print(f"Valor a pagar: R${valor}")
        print(f"Você é o {numerodoveiculoaentrar}º veículo a entrar no shopping.\n")
        print("qual a forma de pagamento? 1 - dinheiro, 2 - cartão")
        pagamento = input("Escolha a forma de pagamento: 1 ou 2? ")
        if pagamento == "1":
            print("Pagamento em dinheiro selecionado. Por favor, dirija-se ao caixa para efetuar o pagamento.")
            break
        elif pagamento == "2":
            print("Pagamento com cartão selecionado. Por favor, dirija-se ao caixa para efetuar o pagamento.")
            break
        else:
            print("Opção de pagamento inválida! Por favor, escolha 1 ou 2.\n")
            break
        
        
        