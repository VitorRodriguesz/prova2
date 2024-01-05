# Pergunta ao usuário a velocidade do carro
velocidade = float(input("Digite a velocidade do carro em km/h: "))

# Verifica se a velocidade ultrapassa 80 km/h
limite_velocidade = 80

if velocidade > limite_velocidade:
    # Calcula o valor da multa
    excedente = velocidade - limite_velocidade
    valor_multa = excedente * 20

    # Exibe a mensagem de multa e o valor
    print(f"Você foi multado! Velocidade excedida: {excedente:.2f} km/h")
    print(f"Valor da multa: R${valor_multa:.2f}")
else:
    # Se a velocidade não ultrapassar 80 km/h, exibe uma mensagem
    print("Velocidade dentro do limite permitido.")