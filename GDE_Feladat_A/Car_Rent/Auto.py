#•	Auto (absztrakt osztály): Definiálja az autó alapvető attribútumait (rendszám, típus, bérleti díj).

from abc import ABC

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
        self.foglalt = False

    @abstractmethod    
    def kiad_auto(self):
        pass
    
    @abstractmethod    
    def bead_auto(self):
        pass
    



# self, rendszam, tipus, berleti_dij