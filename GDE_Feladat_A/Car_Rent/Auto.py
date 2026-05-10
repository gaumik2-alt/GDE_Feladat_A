#•	Auto (absztrakt osztály): Definiálja az autó alapvető attribútumait (rendszám, típus, bérleti díj).

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
        self.foglalt = False

        

# self, rendszam, tipus, berleti_dij