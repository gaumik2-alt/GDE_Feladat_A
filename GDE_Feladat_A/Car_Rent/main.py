import os


from Kolcsonzo import Kolcsonzo
from Szemely_auto import szemely_auto
from Teher_auto import teher_auto


def kepernyo_torles():
    # Windows-on a 'cls', Linuxon/Mac-en/Git Bash-en a 'clear' parancsot futtatja le
    os.system('cls' if os.name == 'nt' else 'clear')


class Foglalas:
    def __init__(self):
        self._kolcsonzo = Kolcsonzo("Négykerék")
        self._adatok()


    def _adatok(self):
        self._kolcsonzo.autok = szemely_auto("ABC-001", "Toyota Yaris", "5000")
        self._kolcsonzo.autok = szemely_auto("ABC-002","Audi A4", "8000")
        self._kolcsonzo.autok = szemely_auto("ABC-003","Mercedes C250", "15000")
        self._kolcsonzo.autok = teher_auto("ABC-011","IFA 4x4","10600")
        self._kolcsonzo.autok = teher_auto("ABC-012","MAN", "12400")

    def funkciok (self):
        while True:
            print(f" -- Autókölcsönző rendszer menü --")
            print("1. Autók listázása")
            print("2. Autó foglalása")
            print("3. Foglalás törlése")
            print("4. Kilépés")

            menu = input("Válassz a fenti menűpontokból:")

            if menu == "1":
                kepernyo_torles()
                print("--- Bérelhető autók listája ---")
                self._kolcsonzo.autok
            elif menu == "2":
                kepernyo_torles()
                rendszam = input("Add meg a rendszámot:")
                self._kolcsonzo.kiberel_rendszam(rendszam)
            elif menu == "3":
                kepernyo_torles()
                rendszam = input("Add meg a rendszámot:")
                self._kolcsonzo.visszaad_rendszam(rendszam)
            elif menu == "4":
                break



foglalasok = Foglalas()
foglalasok.funkciok()