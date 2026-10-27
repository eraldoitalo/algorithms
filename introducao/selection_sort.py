# selection sort é um algoritmo de ordenacao simples que fuinciona encontrando o menor elemento de uma lista
# e colocando-o na posicao correta

def selection_sort(lista): 
    n = len(lista) # "len" ler a lista de elementos 

    for i in range(n): # o primeiro for percorre as posicoes da lista
        menor = i 

        for j in range(i + 1, n): # o segundo for procuras o menor elemento da lista
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return lista

numeros = [64, 58, 32, 10, 48, 32, 73, 95, 49, 55]

print(selection_sort(numeros)) 

# A complexidade de tempo dessa funcao e O(n^2), pois temos dois loops O(n) aninhados.

