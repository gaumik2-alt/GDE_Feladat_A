import os                       # Terminál törlés (cls)
from datetime import datetime   # dátumformátum ellenőrzés


from Kolcsonzo import Kolcsonzo
from Szemely_auto import szemely_auto
from Teher_auto import teher_auto
from Berles import Berles

def kepernyo_torles():
    # Windows-on a 'cls', Linuxon/Mac-en/Git Bash-en a 'clear' parancsot futtatja le
    os.system('cls' if os.name == 'nt' else 'clear')


class Foglalas:
    def __init__(self):
        self._kolcsonzo = Kolcsonzo("Négykerék")
        self._adatok()

    def _adatok(self):
        self._kolcsonzo.autok.append(szemely_auto("ABC-001", "Toyota Yaris", "5000"))
        self._kolcsonzo.autok.append(szemely_auto("ABC-002","Audi A4", "8000"))
        self._kolcsonzo.autok.append(szemely_auto("ABC-003","Mercedes C250", "15000"))
        self._kolcsonzo.autok.append(teher_auto("ABC-011","IFA 4x4","10600"))
        self._kolcsonzo.autok.append(teher_auto("ABC-012","MAN", "12400"))
        
        # Előre beállított bérlés az Audi A4-eshez
        alap_auto = self._kolcsonzo.autok[1] 
        alap_auto._foglalt = True
        alap_berles = Berles(alap_auto, "2026-06-01")
        self._kolcsonzo._berles.append(alap_berles)

    def funkciok (self):
        while True:
            print(f" -- Autókölcsönző rendszer menü --")
            print("1. Járművek listázása")
            print("2. Jármű foglalása")
            print("3. Foglalás törlése")
            print("4. Aktuális bérlések")
            print("5. Kilépés")

            menu = input("Válassz a fenti menűpontokból:")

            if menu == "1":
                kepernyo_torles()
                print("--- Járművek listája ---")
                #self._kolcsonzo.autok
                for auto in self._kolcsonzo.autok:
                    print(auto)
                input("\nNyomj Entert a visszatéréshez...")
                kepernyo_torles()

            elif menu == "2":
                kepernyo_torles()
                print("--- Bérelhető Járművek listája ---")
                for auto in self._kolcsonzo.autok:
                    if auto._foglalt == False:
                        print(auto)
                rendszam = input("Add meg a foglalni kívánt jármű rendszámát (pl.:ABC-001):")
                datum = input("Add meg a bérlés dátumát (éééé-hh-nn, pl. 2026-05-20): ")
                try:
                    érvényes_datum = datetime.strptime(datum, "%Y-%m-%d")
                
                    talalt_auto = None
                    for auto in self._kolcsonzo.autok:
                        if auto.rendszam == rendszam and not auto._foglalt:
                            talalt_auto = auto
                            print(f"megtalalt {talalt_auto}")
                            self._kolcsonzo.kiberel_rendszam(rendszam)
                            uj_berles = Berles(talalt_auto, datum)
                            self._kolcsonzo._berles.append(uj_berles)
                except ValueError:
                    print("\nHiba: Érvénytelen dátum formátum! Kérlek, használj éééé-hh-nn formátumot (pl. 2026-05-20).")

                input("\nNyomj Entert a visszatéréshez...")
                kepernyo_torles()
            elif menu == "3":
                kepernyo_torles()
                rendszam = input("Add meg a törlendő foglalásban érintett jármű rendszámát (pl.:ABC-001):")
                talalt_berles = None
        
                for berles in self._kolcsonzo._berles:
                    if berles.auto.rendszam == rendszam:
                        talalt_berles = berles
                if talalt_berles:
                    self._kolcsonzo.visszaad_rendszam(rendszam)
                    self._kolcsonzo._berles.remove(talalt_berles)
                else:
                    print(f"\nHiba: Nem található aktív foglalás a(z) {rendszam} rendszámú járműre!")

            elif menu == "4":
                kepernyo_torles()
                print("--- Aktuális bérlések listája ---\n")
                if not self._kolcsonzo._berles:
                    print("Jelenleg nincs egyetlen aktív bérlés sem a rendszerben.")
                else:
                    for berles in self._kolcsonzo._berles:
                        print(berles)
                
                input("\nNyomj Entert a visszatéréshez...")
                kepernyo_torles()
            elif menu == "5":
                kepernyo_torles()
                print("--- Sikeres kilépés ---")
                break


foglalasok = Foglalas()
foglalasok.funkciok()
