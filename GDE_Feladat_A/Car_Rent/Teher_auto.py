# Teherauto: A teherautók specifikus attribútumait tartalmazó osztály.

from Auto import Auto

class teher_auto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super().__init__(rendszam, tipus, berleti_dij)
        self._tonna = [""]


    @property
    def rendszam(self):
        return self._rendszam

    @property
    def tipus(self):
        return self._tipus

    @property
    def berleti_dij(self):
        return self._berleti_dij

    @property
    def tonna(self):
        return self._tonna
    
    @property
    def status(self):
        return self._foglalt
    
    def kiberel_auto(self):
        if not self._foglalt:
            self._foglalt = True
            print(f"A(z) {self.rendszam} rendszámú személyautó kibérelve.")
        else:
            print("Hiba: ez az autó már foglalt!")

    def visszaad_auto(self):
        if self._foglalt:
            self._foglalt = False
            print(f"A(z) {self.rendszam} rendszámú személyautó visszaadva.")
        else:
            print("Hiba: ez az autó nem foglalt!")
    

    #def info(self) -> str:
    #    return f"Teherautó: {self.tipus} ({self.rendszam}), {self.berleti_dij} Ft/nap, súlykorlát: {self.tonna} tonna"

