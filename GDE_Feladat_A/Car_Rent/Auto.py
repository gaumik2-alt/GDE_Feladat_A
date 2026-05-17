#•	Auto (absztrakt osztály): Definiálja az autó alapvető attribútumait (rendszám, típus, bérleti díj).

from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self._rendszam = rendszam      # non publik
        self._tipus = tipus
        self._berleti_dij = berleti_dij
        self._foglalt = False
    
    def __str__(self):
        if self._foglalt:
            statusz_szoveg = "Foglalt"
        else:
            statusz_szoveg = "Szabad"
        return f"Rendszám: {self._rendszam:<9} | Típus: {self._tipus:<16} | Ár: {self._berleti_dij:<10} Ft/nap | Státusz: {statusz_szoveg}"