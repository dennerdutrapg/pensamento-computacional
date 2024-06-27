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

# Exemplo de uso:
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17]
elemento_busca = 13

indice_encontrado = pesquisa_binaria(lista_ordenada, elemento_busca)

if indice_encontrado != -1:
    print(f"O elemento {elemento_busca} foi encontrado na posição {indice_encontrado}.")
else:
    print(f"O elemento {elemento_busca} não foi encontrado na lista.")
