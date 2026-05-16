#•	Auto (absztrakt osztály): Definiálja az autó alapvető attribútumait (rendszám, típus, bérleti díj).

from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self._rendszam = rendszam      # non publik
        self._tipus = tipus
        self._berleti_dij = berleti_dij
        self._foglalt = False

    