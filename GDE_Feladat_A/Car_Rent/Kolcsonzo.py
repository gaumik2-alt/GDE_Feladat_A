class kolcsonzo:
    def __init__(self, neve, cime):
        self._neve = neve
        self._cime = cime
        self._autok = []

    @property
    def neve(self):
        return self._neve
    
    @property
    def cime(self):
        return self._cime
    
    @property
    def autok(self):
        for auto in self._autok:
            print(f"Bérelhető járművek: {autok._autok}")

    
