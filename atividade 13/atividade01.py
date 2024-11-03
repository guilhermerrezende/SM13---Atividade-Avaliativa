# GUILHERME REZENDE DAMACENO


# Função para calcular o salário do vendedor
def calcular_salario(salario_fixo, comissao_por_carro, valor_total_vendas, carros_vendidos):
    # Caso em que o vendedor não vendeu nenhum carro
    if carros_vendidos == 0:
        return salario_fixo  # Apenas o salário fixo, sem comissão nem percentual sobre vendas
    else:
        # Calculando a comissão total pelo número de carros vendidos
        comissao_total = comissao_por_carro * carros_vendidos
        # Calculando o percentual de 5% sobre o total das vendas
        percentual_sobre_vendas = 0.05 * valor_total_vendas
        
        # Condição para aplicar o bônus de 10% se o vendedor vendeu mais de 10 carros
        if carros_vendidos > 10:
            bonus = 0.1 * valor_total_vendas
        else:
            bonus = 0  # Sem bônus se vendeu 10 carros ou menos
        
        # Somando todos os valores para obter o salário final
        salario_final = salario_fixo + comissao_total + percentual_sobre_vendas + bonus
        return salario_final

# Solicitando os valores de entrada ao usuário
try:
    salario_fixo = float(input("Digite o valor do salário fixo: R$ "))
    comissao_por_carro = float(input("Digite o valor da comissão por carro vendido: R$ "))
    valor_total_vendas = float(input("Digite o valor total das vendas: R$ "))
    carros_vendidos = int(input("Digite o número de carros vendidos: "))
    
    # Calculando o salário final do vendedor
    salario_calculado = calcular_salario(salario_fixo, comissao_por_carro, valor_total_vendas, carros_vendidos)
    print(f"O salário final do vendedor é: R$ {salario_calculado:.2f}")

except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos para o cálculo do salário.")
