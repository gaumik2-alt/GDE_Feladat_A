

class Kolcsonzo:
    def __init__(self, neve):
        self._neve = neve
        self._autok = []
        self._berles = []

    @property
    def neve(self):
        return self._neve
    
    @property
    def autok(self):
        return self._autok
        # for auto in self._autok:
        #    print(f"Rendszám: {auto.rendszam} , Státusz: {auto.status}")

    def szabad_autok(self):
        for auto in self.osszes_auto:
            if auto.foglalt == False:  
                print(auto)

    @autok.setter
    def autok(self, uj_auto):
        self._autok.append(uj_auto)

 
    def kiberel_rendszam(self, rendszam):
        for auto in self._autok:
            if auto.rendszam == rendszam:
                auto.kiberel_auto()

    def visszaad_rendszam(self, rendszam):
        for auto in self._autok:
            if auto.rendszam == rendszam:
                auto.visszaad_auto()