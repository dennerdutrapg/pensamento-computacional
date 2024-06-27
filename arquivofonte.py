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

# Exemplo de uso:
lista_exemplo = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
elemento_busca = 9

indice_encontrado = pesquisa_sequencial(lista_exemplo, elemento_busca)

if indice_encontrado != -1:
    print(f"O elemento {elemento_busca} foi encontrado na posição {indice_encontrado}.")
else:
    print(f"O elemento {elemento_busca} não foi encontrado na lista.")
