from particao import Particao
from aresta_ponderada import ArestaPonderada
from arvore_ponderada import ArvorePonderada
from heap_minima_aresta import HeapMinimaAresta
from heap_minima_particao import HeapMinimaParticao

def particionamento(particao: Particao, particoes: HeapMinimaParticao):
    particao1: Particao = particao.copia()
    particao2: Particao = particao.copia()
    

    while particao.sizeArestaAberta():
        
        particao.removerArestaAbertaMinima()
        particao1.removerArestaAbertaMinima()
        aresta: ArestaPonderada = particao2.removerArestaAbertaMinima()
        particao2.inserirArestaObrigatoria(aresta)

        if particao1.calcularArvoreGeradoraMinima():
            particoes.inserirElemento(particao1)

        print(1, particao)
        print(2, particao1)
        print(4, particao2)

        particao1 = particao2.copia()
        

def main():
    with open("grafo.txt", "r") as grafo:
        qtdVertices = int(grafo.readline())
        particoes: HeapMinimaParticao = HeapMinimaParticao(qtdVertices)
        particao = Particao(qtdVertices)

        for linha in grafo:
            valores = tuple(map(int, linha.strip('\n').split(' ')))
            particao.inserirArestaAbertas(valores)

    with open("arvores.txt", "w") as arvores:
        particoes.inserirElemento(particao)
        if not particao.calcularArvoreGeradoraMinima():
            print("Não é possível gerar uma árvore para esse grafo")
        k=1
        menorArvore: ArvorePonderada = particao.getArvoreGeradoraMinima()

        while menorArvore is not None and k:
            particao: Particao = particoes.removerElementoMinimo()
            menorArvore: ArvorePonderada = particao.getArvoreGeradoraMinima()

            arvores.write(str(menorArvore))
            particionamento(particao, particoes)

            print(particoes)
            k = 0


        

    
            
main()