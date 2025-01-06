from typing import Optional

from aresta_ponderada import ArestaPonderada
from arvore_ponderada import ArvorePonderada
from heap_minima_aresta import HeapMinimaAresta


class Particao:
    def __init__(self, quantidadeVertices: int) -> None:
        self.arvoreGeradoraMinima: Optional[ArvorePonderada] = None
        self.arestasAbertas: HeapMinimaAresta = HeapMinimaAresta()
        self.arestasObrigatorias: list[ArestaPonderada] = list()
        self.quantidadeVertices = quantidadeVertices
        self.custo = 0

    def inserirArestaObrigatoria(self, valores: tuple[int|float]) -> None:
        aresta: ArestaPonderada = ArestaPonderada(*valores)
        self.arestasObrigatorias.append(aresta)

    def inserirArestaAbertas(self, valores: tuple[int|float]) -> None:
        aresta: ArestaPonderada = ArestaPonderada(*valores)
        self.arestasAbertas.inserirElemento(aresta)

    def removerArestaAbertaMinima(self) -> ArestaPonderada:
        return self.arestasAbertas.removerElementoMinimo()

    def __gt__(self, outraParticao: "Particao") -> bool:
        return self.custo > outraParticao.custo

    def __eq__(self, outraParticao: "Particao") -> bool:
        return self.custo == outraParticao.custo

    def __ge__(self, outraParticao: "Particao") -> bool:
        return self.custo >= outraParticao.custo

    def getArvoreGeradoraMinima(self) -> Optional[ArvorePonderada]:
        return self.arvoreGeradoraMinima

    def calcularArvoreGeradoraMinima(self) -> bool:
        self.arvoreGeradoraMinima = ArvorePonderada(self.quantidadeVertices, self.arestasObrigatorias)
        heapTemp = self.arestasAbertas.copia()

        while len(self.arestasAbertas) and self.arvoreGeradoraMinima.size() < self.quantidadeVertices - 1:
            arestaMinima: ArestaPonderada = heapTemp.removerElementoMinimo()
            self.arvoreGeradoraMinima.inserirAresta(arestaMinima)

        del heapTemp

        if self.arvoreGeradoraMinima.size() == self.quantidadeVertices - 1:
            self.custo = self.arvoreGeradoraMinima.getCusto()
            return True


        return False



