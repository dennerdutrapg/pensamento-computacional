import random
import time

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

# Medição de tempo para pesquisa binária
def medir_tempo_pesquisa_binaria(tamanho):
    vetor = preencher_vetor(tamanho)
    elemento_busca = vetor[-1]  # Busca o último elemento gerado
    vetor.sort()  # Ordena o vetor para aplicar a pesquisa binária
    
    inicio = time.time()
    indice_encontrado = pesquisa_binaria(vetor, elemento_busca)
    fim = time.time()
    
    tempo_execucao = fim - inicio
    return tempo_execucao

# Tamanho do vetor para teste
tamanho_teste = 10000

# Medição de tempo para pesquisa binária
tempo_binaria = medir_tempo_pesquisa_binaria(tamanho_teste)
print(f"Tempo de execução da pesquisa binária para tamanho {tamanho_teste}: {tempo_binaria:.6f} segundos")
