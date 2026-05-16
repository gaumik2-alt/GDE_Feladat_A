# Teherauto: A teherautók specifikus attribútumait tartalmazó osztály.

from Auto import Auto

class teher_auto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super().__init__(rendszam, tipus, berleti_dij)
        self.tonna = [""]


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
    def status(self):
        return self._foglalt
    
    def kiberel_auto(self):
        # Egyelőre csak ennyit csinál, hogy ne kapj hibát
        print(f"A(z) {self.rendszam} rendszámú személyautó kibérelve.") 
        return True

    def visszaad_auto(self):
        print(f"A(z) {self.rendszam} rendszámú személyautó visszaadva.")
        return True
    

    #def info(self) -> str:
    #    return f"Teherautó: {self.tipus} ({self.rendszam}), {self.berleti_dij} Ft/nap, súlykorlát: {self.tonna} tonna"

