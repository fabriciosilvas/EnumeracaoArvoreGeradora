from typing import Optional
from math import inf
from aresta_ponderada import ArestaPonderada
from arvore_ponderada import ArvorePonderada
from heap_minima_aresta import HeapMinimaAresta


class Particao:
    def __init__(self, quantidadeVertices: int, custo: float = 0) -> None:
        self.arvoreGeradoraMinima: Optional[ArvorePonderada] = None
        self.arestasAbertas: HeapMinimaAresta = HeapMinimaAresta()
        self.arestasObrigatorias: list[ArestaPonderada] = list()
        self.quantidadeVertices = quantidadeVertices
        self.custo = custo
    def __str__(self) -> str:
        print(self.arestasAbertas)
        string: str = "Obr["

        k: int = len(self.arestasObrigatorias)
        for elem in range(k-1):
            string += f"{str(self.arestasObrigatorias[elem])}, "

        if k:
            string += f"{str(self.arestasObrigatorias[k-1])}]"
        else:
            string += "]"

        return string

    def sizeArestaAberta(self) -> int:
        return len(self.arestasAbertas)

    def copia(self) -> "Particao":
        novaParticao: Particao = Particao(self.quantidadeVertices)
        novaParticao.setArestasAbertas(self.arestasAbertas.copia())
        novaParticao.setArestasObrigatorias(self.arestasObrigatorias)

        return novaParticao


    def setArestasAbertas(self, arestas: HeapMinimaAresta) -> None:
        self.arestasAbertas = arestas

    def setArestasObrigatorias(self, arestas: list[ArestaPonderada]) -> None:
        self.arestasObrigatorias = arestas.copy()

    def inserirArestaObrigatoria(self, aresta: ArestaPonderada) -> None:
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



