import random

def preencher_vetor(tamanho):
    """
    Função para preencher um vetor com números aleatórios entre 0 e tamanho*10.
    
    Parâmetros:
    - tamanho: inteiro representando o tamanho desejado do vetor.
    
    Retorna:
    - Um vetor preenchido com números aleatórios.
    """
    vetor = []
    limite_superior = tamanho * 10
    
    for _ in range(tamanho):
        numero_aleatorio = random.randint(0, limite_superior)
        vetor.append(numero_aleatorio)
    
    return vetor

# Solicitar ao usuário o tamanho do vetor
tamanho_vetor = int(input("Digite o tamanho do vetor desejado: "))

# Preencher o vetor com números aleatórios
vetor_aleatorio = preencher_vetor(tamanho_vetor)

# Exibir o vetor gerado
print(f"Vetor gerado com {tamanho_vetor} elementos:")
print(vetor_aleatorio)
