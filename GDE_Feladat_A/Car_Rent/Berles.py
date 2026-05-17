    

class Berles:
    def __init__(self, auto, datum):
        self._auto = auto      # Non-publik: eltároljuk a konkrét autó objektumot
        self._datum = datum    # Non-publik: pl. "2026-05-20" vagy egy dátum objektum

    @property
    def auto(self):
        return self._auto

    @property
    def datum(self):
        return self._datum

    def __str__(self):
        # Amikor kilistázzuk a foglalásokat, így fog szépen megjelenni:
        return f"Dátum: {self._datum} | {self._auto}"