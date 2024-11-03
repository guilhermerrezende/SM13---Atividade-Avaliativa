# GUILHERME REZENDE DAMACENO


# Função para validar se a entrada é um número inteiro positivo
def validar_idade(idade):
    try:
        idade = int(idade)
        if idade > 0:
            return idade
        else:
            print("Erro: A idade deve ser um número inteiro positivo.")
            return None
    except ValueError:
        print("Erro: A idade deve ser um número inteiro positivo.")
        return None

# Função principal para calcular a soma e o produto das idades de acordo com as regras
def calcular_soma_produto_idades(homem1, homem2, mulher1, mulher2):
    # Identificando o homem mais velho e o homem mais novo
    homem_mais_velho = max(homem1, homem2)  # Definindo o homem mais velho com base nas idades fornecidas
    homem_mais_novo = min(homem1, homem2)  # Definindo o homem mais novo com base nas idades fornecidas
    
    # Identificando a mulher mais velha e a mulher mais nova
    mulher_mais_velha = max(mulher1, mulher2)  # Definindo a mulher mais velha
    mulher_mais_nova = min(mulher1, mulher2)  # Definindo a mulher mais nova
    
    # Calculando a soma do homem mais velho com a mulher mais nova
    soma = homem_mais_velho + mulher_mais_nova
    
    # Calculando o produto do homem mais novo com a mulher mais velha
    produto = homem_mais_novo * mulher_mais_velha
    
    return soma, produto

# Solicitando as idades e validando cada uma
homem1 = validar_idade(input("Digite a idade do primeiro homem: "))
homem2 = validar_idade(input("Digite a idade do segundo homem: "))
mulher1 = validar_idade(input("Digite a idade da primeira mulher: "))
mulher2 = validar_idade(input("Digite a idade da segunda mulher: "))

# Verifica se todas as idades são válidas antes de continuar
if None not in (homem1, homem2, mulher1, mulher2):
    # Calcula a soma e o produto usando a função
    soma, produto = calcular_soma_produto_idades(homem1, homem2, mulher1, mulher2)
    print(f"A soma do homem mais velho com a mulher mais nova é: {soma}")
    print(f"O produto do homem mais novo com a mulher mais velha é: {produto}")
else:
    print("Não foi possível realizar o cálculo devido a entradas inválidas.")
