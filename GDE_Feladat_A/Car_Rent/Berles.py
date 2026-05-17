

class Berles:
    def __init__(self, rendszam, datum):
        self._rendszam = rendszam
        self._datum = datum

    @property
    def rendszam(self):
        return self._rendszam
    
    @property
    def datum(self):
        return self._datum
    