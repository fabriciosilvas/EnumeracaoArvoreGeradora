from particao import Particao
from aresta_ponderada import ArestaPonderada
from arvore_ponderada import ArvorePonderada
from heap_minima_aresta import HeapMinimaAresta
from heap_minima_particao import HeapMinimaParticao

def particionamento(particao: Particao, particoes: HeapMinimaParticao):
    pass

def main():
    with open("grafo.txt", "r") as grafo:
        qtdVertices = int(grafo.readline())
        particoes: HeapMinimaParticao = HeapMinimaParticao(qtdVertices)

        for linha in grafo:
            l = tuple(map(int, linha.strip('\n').split(' ')))
            print(l)

main()