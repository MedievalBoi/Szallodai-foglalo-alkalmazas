from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def szobatipus(self):
        pass

class EgyagyasSzoba(Szoba):
    def szobatipus(self):
        return "Egyágyas szoba"

class KetagyasSzoba(Szoba):
    def szobatipus(self):
        return "Kétágyas szoba"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = {}

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum, nev):
        talalat = False
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                talalat = True
                if szobaszam not in self.foglalasok:
                    self.foglalasok[szobaszam] = {}
                if datum in self.foglalasok[szobaszam]:
                    print("Ez a szoba már foglalt ezen a napon!")
                    return
                self.foglalasok[szobaszam][datum] = nev
                print("Sikeres foglalás!")
                return
        if not talalat:
            print("Nincs ilyen szobaszám!")
            print("Elérhető szobaszámok:")
            for szoba in self.szobak:
                print(szoba.szobaszam)

    def lemondas(self, szobaszam, datum):
        if szobaszam in self.foglalasok and datum in self.foglalasok[szobaszam]:
            del self.foglalasok[szobaszam][datum]
            print("Sikeres lemondás!")
        else:
            print("Nem található ilyen foglalás!")

    def FoglalasokListazasa(self):
        print("Foglalások:")
        for szobaszam, foglalasok in self.foglalasok.items():
            print(f"Szoba: {szobaszam}")
            for datum, nev in foglalasok.items():
                ar = self.szoba_ar(szobaszam)
                print(f"\tDátum: {datum}\n\tFoglaló: {nev}\n\tÁr: {ar} Ft")
            print()

    def SzobaInformaciok(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return print(f"Szoba száma: {szoba.szobaszam}, Ár: {szoba.ar}")

    def szoba_ar(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.ar

def main():
    szalloda = Szalloda("Czellcorp Szálloda")

    for i in range(100, 200):
        szalloda.szoba_hozzaadasa(EgyagyasSzoba(f"{i}", f"{5640}"))
    for j in range(200, 300):
        szalloda.szoba_hozzaadasa(KetagyasSzoba(f"{j}", f"{8590}"))

    szalloda.foglalas("101", "2024. 04. 15.", "Mekk Mester")
    szalloda.foglalas("102", "2024. 04. 16.", "Teszt Elek")
    szalloda.foglalas("201", "2024. 04. 17.", "Wincs Eszter")
    szalloda.foglalas("101", "2024. 04. 17.", "Bud Spencer")
    szalloda.foglalas("102", "2024. 04. 17.", "Terence Hill")

    while True:
        print("\nCzellCorp Szálloda")
        print("\nVálasztható műveletet:")
        print("1. Szoba foglalása")
        print("2. Szoba lemondása")
        print("3. Foglalások listázása")
        print("4. Szobaszámok & áruk")
        print("5. Kilépés")

        valasztas = input("\nKérem, válasszon: ")

        if valasztas == "1":
            szobaszam = input("Add meg a foglalni kívánt szoba számát: ")
            datum = input("Add meg a foglalás dátumát (Év. Hónap. Nap. (1234. 12. 12.) formátumban): ")
            nev = input("Add meg a foglaló nevét: ")
            szalloda.foglalas(szobaszam, datum, nev)
        elif valasztas == "2":
            szobaszam = input("Add meg a lemondani kívánt foglalás szoba számát: ")
            datum = input("Add meg a lemondani kívánt foglalás dátumát (Év. Hónap. Nap. (1234. 12. 12.) formátumban): ")
            szalloda.lemondas(szobaszam, datum)
        elif valasztas == "3":
            szalloda.FoglalasokListazasa()
        elif valasztas == "4":
            MelySzoba=input("Egy- vagy kétágyas szobákat szeretne látni? ")
            if MelySzoba == "1":
                print("Egyágyas szobák:")
                for i in range(100, 200):
                    szalloda.SzobaInformaciok(f"{i}")
            elif MelySzoba == "2":
                print("Kétágyas szobák:")
                for j in range(200, 300):
                    szalloda.SzobaInformaciok(f"{j}")
            else:
                print("Helytelen bevitel")
        elif valasztas == "5":
            print("\nKöszönjük foglalását!")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
