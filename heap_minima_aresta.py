from math import inf
from aresta_ponderada import ArestaPonderada
from typing import Optional



class HeapMinimaAresta:
    def __init__(self, tamanhoHeap: int = 0, vetorElementos: Optional[list[ArestaPonderada]] = None):
        self.tamanhoHeap: int = tamanhoHeap

        if vetorElementos is None:
            self.vetorElementos: list[ArestaPonderada] = list()
        else:
            self.vetorElementos = vetorElementos

    def getVetorElementos(self) -> list[ArestaPonderada]:
        return self.vetorElementos

    def getPai(self, indice: int) -> int:
        return max((indice - 1), 0) // 2

    def getFilhoEsquerdo(self, indice: int) -> int:
        return 2 * indice + 1

    def getFilhoDireito(self, indice: int) -> int:
        return 2 * (indice + 1)

    def minHeapfy(self, indice: int) -> None:
        filhoEsquerdo: int = self.getFilhoEsquerdo(indice)
        filhoDireito: int = self.getFilhoDireito(indice)
        menorElemento: int = indice



        if filhoEsquerdo < self.tamanhoHeap and self.vetorElementos[filhoEsquerdo] < self.vetorElementos[indice]:
            menorElemento = filhoEsquerdo

        if filhoDireito < self.tamanhoHeap and self.vetorElementos[filhoDireito] < self.vetorElementos[menorElemento]:
            menorElemento = filhoDireito

        if menorElemento != indice:
            temp: ArestaPonderada = self.vetorElementos[indice]
            self.vetorElementos[indice] = self.vetorElementos[menorElemento]
            self.vetorElementos[menorElemento] = temp

            self.minHeapfy(menorElemento)

    def atualizaValor(self, indice: int, novoValor: int|float) -> None:
        self.vetorElementos[indice].setPeso(novoValor)

        self.minHeapfy(indice)

    def construirHeapMinima(self) -> None:
        self.tamanhoHeap = len(self.vetorElementos)
        tamanhoHeap: int = len(self.vetorElementos)
        for i in range((tamanhoHeap - 2) // 2, -1, -1):
            self.minHeapfy(i)

    def heapSort(self) -> None:
        self.construirHeapMinima()
        tamanhoHeap: int = len(self.vetorElementos)
        for elem in range(tamanhoHeap - 1, 0, -1):
            temp: ArestaPonderada = self.vetorElementos[0]
            self.vetorElementos[0] = self.vetorElementos[elem]
            self.vetorElementos[elem] = temp
            self.tamanhoHeap -= 1
            self.minHeapfy(0)

    def inserirElemento(self, elemento: ArestaPonderada) -> None:
        self.tamanhoHeap += 1
        novaAresta: ArestaPonderada = ArestaPonderada(-1, -1, inf)
        self.vetorElementos.append(novaAresta)
        self.diminuirValorElemento(self.tamanhoHeap - 1, elemento)

    def obterElementoMinimo(self) -> ArestaPonderada:
        return self.vetorElementos[0]

    def removerElementoMinimo(self) -> Optional[ArestaPonderada]:
        if self.tamanhoHeap < 1:
            print("Heap não possui elementos")
            return None

        elementoMinimo: ArestaPonderada = self.vetorElementos[0]
        self.vetorElementos[0] = self.vetorElementos[self.tamanhoHeap - 1]
        self.vetorElementos.pop(self.tamanhoHeap - 1)
        self.tamanhoHeap -= 1

        self.minHeapfy(0)
        return elementoMinimo

    def __len__(self):
        return self.tamanhoHeap

    def copia(self) -> "HeapMinimaAresta":
        heapCopia: HeapMinimaAresta = HeapMinimaAresta(self.tamanhoHeap, self.vetorElementos[:])

        return heapCopia


    def diminuirValorElemento(self, tamanhoHeap: int, elemento: ArestaPonderada) -> None:
        if elemento > self.vetorElementos[tamanhoHeap]:
            print("Erro1")
            return

        self.vetorElementos[tamanhoHeap] = elemento
        while tamanhoHeap > 0 and self.vetorElementos[self.getPai(tamanhoHeap)] > self.vetorElementos[tamanhoHeap]:
            temp: ArestaPonderada = self.vetorElementos[tamanhoHeap]
            self.vetorElementos[tamanhoHeap] = self.vetorElementos[self.getPai(tamanhoHeap)]
            self.vetorElementos[self.getPai(tamanhoHeap)] = temp
            tamanhoHeap = self.getPai(tamanhoHeap)
    

    def __str__(self) -> str:
        string: str = "["

        k: int = len(self.vetorElementos)
        for elem in range(k-1):
            string += f"{str(self.vetorElementos[elem])}, "

        if k:
            string += f"{str(self.vetorElementos[k-1])}]"
        else:
            string += "]"

        return string





if __name__ == '__main__':
    arestas = [
        (1, 2, 7),
        (3, 4, 5),
        (5, 6, 10),
        (2, 7, 3),
        (8, 9, 4),
        (1, 5, 8),
        (3, 8, 6),
        (4, 6, 9),
        (7, 2, 1),
        (9, 1, 5),
        (10, 4, 7),
        (2, 3, 2),
        (6, 7, 11),
        (8, 5, 13),
        (3, 9, 12),
        (4, 10, 6),
        (5, 1, 14),
        (7, 3, 9),
        (2, 6, 4),
        (10, 8, 15)
    ]
    arest = [
        (1, 2, 7),
        (3, 4, 5),
        (5, 6, 10)]
    heap = HeapMinimaAresta()
    for i, j, m in arestas:
        a = ArestaPonderada(i, j, m)

        heap.inserirElemento(a)

    print(heap)



    #heap.heapSort()
    for i in range(len(arestas)):
        print(heap.removerElementoMinimo())