class ArestaPonderada:
    def __init__(self, verticeInicial: int, verticeFinal: int, peso: int|float) -> None:
        self.peso = peso
        self.verticeInicial = verticeInicial
        self.verticeFinal = verticeFinal

    def getVerticeInicial(self) -> int:
        return  self.verticeInicial

    def getVerticeFinal(self) -> int:
        return self.verticeFinal

    def getPeso(self) -> float:
        return self.peso

    def setPeso(self, peso: float) -> None:
        self.peso = peso

    def __str__(self) -> str:
        return f"({self.verticeInicial}, {self.verticeFinal}, {self.peso})"

    def __eq__(self, outraAresta: "ArestaPonderada") -> bool:
        return outraAresta.getPeso() == self.getPeso()

    def __gt__(self, outraAresta: "ArestaPonderada") -> bool:
        return self.getPeso() > outraAresta.getPeso()

    def __ge__(self, outraAresta: "ArestaPonderada") -> bool:
        return self.getPeso() >= outraAresta.getPeso()


if "__main__" == __name__:
    a = ArestaPonderada(5, 5, 1)
    b = ArestaPonderada(5, 5, 2)

    print(a != b)


