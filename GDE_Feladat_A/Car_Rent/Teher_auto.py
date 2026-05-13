# Teherauto: A teherautók specifikus attribútumait tartalmazó osztály.

from Auto import Auto

class teher_auto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super.__init__(rendszam, tipus, berleti_dij)
        self.tonna = [""]


    def info(self) -> str:
        return f"Teherautó: {self.tipus} ({self.rendszam}), {self.berleti_dij} Ft/nap, súlykorlát: {self.tonna} tonna"

