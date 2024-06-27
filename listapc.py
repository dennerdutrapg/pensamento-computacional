import random
import time

def pesquisa_sequencial(lista, elemento):
    """
    Função para realizar pesquisa sequencial em uma lista.
    
    Parâmetros:
    - lista: lista de elementos a ser pesquisada.
    - elemento: elemento que está sendo procurado na lista.
    
    Retorna:
    - O índice do elemento na lista se encontrado, ou -1 se não encontrado.
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Retorna o índice onde o elemento foi encontrado
    return -1  # Retorna -1 se o elemento não foi encontrado

def pesquisa_binaria(lista, elemento):
    """
    Função para realizar pesquisa binária em uma lista ordenada.
    
    Parâmetros:
    - lista: lista de elementos ordenados em ordem crescente.
    - elemento: elemento que está sendo procurado na lista.
    
    Retorna:
    - O índice do elemento na lista se encontrado, ou -1 se não encontrado.
    """
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        # Verifica se o elemento está no meio da lista
        if lista[meio] == elemento:
            return meio  # Retorna o índice onde o elemento foi encontrado
        
        # Se o elemento é maior, descarta a metade esquerda
        elif lista[meio] < elemento:
            inicio = meio + 1
        
        # Se o elemento é menor, descarta a metade direita
        else:
            fim = meio - 1
    
    return -1  # Retorna -1 se o elemento não foi encontrado

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

# Função para realizar os testes
def realizar_testes(tamanhos, termos_busca):
    """
    Função para realizar testes variando o tamanho da entrada e o termo de busca.
    
    Parâmetros:
    - tamanhos: lista de inteiros representando os diferentes tamanhos de entrada.
    - termos_busca: lista de inteiros representando os diferentes termos de busca.
    
    Retorna:
    - None (imprime os resultados dos testes).
    """
    for tamanho in tamanhos:
        vetor = preencher_vetor(tamanho)
        vetor.sort()  # Ordena o vetor para aplicar a pesquisa binária
        
        print(f"\n### Teste com tamanho do vetor {tamanho} ###")
        
        for termo in termos_busca:
            # Teste com pesquisa sequencial
            inicio = time.time()
            indice_sequencial = pesquisa_sequencial(vetor, termo)
            fim = time.time()
            tempo_sequencial = fim - inicio
            
            resultado_sequencial = f"Termo {termo} {'encontrado' if indice_sequencial != -1 else 'não encontrado'} pela pesquisa sequencial em {tempo_sequencial:.6f} segundos"
            
            # Teste com pesquisa binária
            inicio = time.time()
            indice_binaria = pesquisa_binaria(vetor, termo)
            fim = time.time()
            tempo_binaria = fim - inicio
            
            resultado_binaria = f"Termo {termo} {'encontrado' if indice_binaria != -1 else 'não encontrado'} pela pesquisa binária em {tempo_binaria:.6f} segundos"
            
            print(resultado_sequencial)
            print(resultado_binaria)

# Definição dos tamanhos e termos de busca para testes
tamanhos_teste = [100, 500, 1000, 5000, 10000]  # Tamanhos variados para o vetor
termos_busca = [0, 50, 100, 5000, 10000, 20000]  # Termos de busca que podem ou não estar no vetor

# Executar os testes
realizar_testes(tamanhos_teste, termos_busca)
