from particao import Particao
from typing import  Optional


class HeapMinimaParticao:
    def __init__(self, quantidadeVertices: int):
        self.vetorElementos: list[Particao] = list()
        self.tamanhoHeap = 0
        self.quantidadeVertices = quantidadeVertices

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
            temp: Particao = self.vetorElementos[indice]
            self.vetorElementos[indice] = self.vetorElementos[menorElemento]
            self.vetorElementos[menorElemento] = temp

            self.minHeapfy(menorElemento)


    def construirHeapMinima(self) -> None:
        self.tamanhoHeap = len(self.vetorElementos)
        tamanhoHeap: int = len(self.vetorElementos)
        for i in range((tamanhoHeap - 2) // 2, -1, -1):
            self.minHeapfy(i)

    def inserirElemento(self, elemento: Particao) -> None:
        self.tamanhoHeap += 1
        novaParticao: Particao = Particao(self.quantidadeVertices)
        self.vetorElementos.append(novaParticao)
        self.diminuirValorElemento(self.tamanhoHeap - 1, elemento)

    def obterElementoMinimo(self) -> Particao:
        return self.vetorElementos[0]

    def removerElementoMinimo(self) -> Optional[Particao]:
        if self.tamanhoHeap < 1:
            print("Heap não possui elementos")
            return None

        elementoMinimo: Particao = self.vetorElementos[0]
        self.vetorElementos[0] = self.vetorElementos[self.tamanhoHeap - 1]
        self.tamanhoHeap -= 1

        self.minHeapfy(0)
        return elementoMinimo

    def __len__(self):
        return self.tamanhoHeap


    def diminuirValorElemento(self, tamanhoHeap: int, elemento: Particao) -> None:
        if elemento > self.vetorElementos[tamanhoHeap]:
            print("Erro")
            return

        self.vetorElementos[tamanhoHeap] = elemento
        while tamanhoHeap > 0 and self.vetorElementos[self.getPai(tamanhoHeap)] > self.vetorElementos[tamanhoHeap]:
            temp: Particao = self.vetorElementos[tamanhoHeap]
            self.vetorElementos[tamanhoHeap] = self.vetorElementos[self.getPai(tamanhoHeap)]
            self.vetorElementos[self.getPai(tamanhoHeap)] = temp
            tamanhoHeap = self.getPai(tamanhoHeap)

    def __str__(self) -> str:
        string: str = "["

        k: int = len(self.vetorElementos)
        for elem in range(k - 1):
            string += f"{str(self.vetorElementos[elem])}, \n"

        if k:
            string += f"{str(self.vetorElementos[k - 1])}]"
        else:
            string += "]"

        return string