# Személyauto: A személyautók specifikus attribútumait tartalmazó osztály.

from Auto import Auto

class szemely_auto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super.__init__(rendszam, tipus, berleti_dij)
        self.extra = [""]


    def info(self) -> str:
        return f"Személyautó: {self.tipus} ({self.rendszam}), {self.berleti_dij} Ft/nap, ülések: {self.extra}"
