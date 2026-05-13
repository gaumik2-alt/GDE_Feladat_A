#•	Auto (absztrakt osztály): Definiálja az autó alapvető attribútumait (rendszám, típus, bérleti díj).

from abc import ABC
from datetime import date


class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self._rendszam = rendszam      # non publik
        self._tipus = tipus
        self._berleti_dij = berleti_dij
        self.foglalt = False

    @abstractmethod    
    def kiberel_auto(self):    # ki van adva
        pass
    
    @abstractmethod    
    def visszaad_auto(self):    # nincs kiadva
        pass
    


    @property
    def rendszam(self) -> str:
        return self._rendszam

    @property
    def tipus(self) -> str:
        return self._tipus

    @property
    def berleti_dij(self) -> int:
        return self._berleti_dij

    @abstractmethod
    def info(self) -> str:
        pass
