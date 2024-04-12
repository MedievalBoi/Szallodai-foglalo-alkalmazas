from abc import ABC, abstractmethod
from datetime import datetime

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
            for datum, nev in foglalasok.items():
                print(f"Szoba: {szobaszam}, Dátum: {datum}, Foglaló: {nev}")

    def SzobaInformaciok(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return print(f"Szoba száma: {szoba.szobaszam}, Ár: {szoba.ar}")

def main():
    szalloda = Szalloda("Czellcorp Szálloda")

    for i in range(100, 200):
        szalloda.szoba_hozzaadasa(EgyagyasSzoba(f"{i}", 5000))
    for j in range(200, 300):
        szalloda.szoba_hozzaadasa(KetagyasSzoba(f"{j}", 8000))

    szalloda.foglalas("101", "2024. 04. 15.", "Mekk Mester")
    szalloda.foglalas("102", "2024. 04. 16.", "Teszt Elek")
    szalloda.foglalas("201", "2024. 04. 17.", "Wincs Eszter")
    szalloda.foglalas("101", "2024. 04. 17.", "Bud Spencer")
    szalloda.foglalas("102", "2024. 04. 17.", "Terence Hill")

    while True:
        print("\nVálasztható műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Szobák száma (árral)")
        print("5. Kilépés")

        valasztas = input("Kérem, válasszon: ")

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
            print("Egyágyas szobák:")
            for i in range(100, 200):
                szalloda.SzobaInformaciok(f"{i}")
            print("Kétágyas szobák:")
            for j in range(200, 300):
                szalloda.SzobaInformaciok(f"{j}")
        elif valasztas == "5":
            print("\nKöszönjük foglalását!")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
