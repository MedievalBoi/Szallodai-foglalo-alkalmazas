from abc import ABC, abstractmethod
from datetime import datetime
import random

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    # @abstractmethod
    # def szobatipus(self):
    #     pass

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
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if szobaszam not in self.foglalasok:
                    self.foglalasok[szobaszam] = {}
                if datum in self.foglalasok[szobaszam]:
                    print("Ez a szoba már foglalt ezen a napon!")
                    return
                self.foglalasok[szobaszam][datum] = nev
                print("Sikeres foglalás!")
                return
        print("Nincs ilyen szobaszám!")

    def lemondas(self, szobaszam, datum):
        if szobaszam in self.foglalasok and datum in self.foglalasok[szobaszam]:
            del self.foglalasok[szobaszam][datum]
            print("Sikeres lemondás!")
        else:
            print("Nem található ilyen foglalás!")

    def foglalasok_listazasa(self):
        print("Foglalások:")
        for szobaszam, foglalasok in self.foglalasok.items():
            for datum, nev in foglalasok.items():
                print(f"Szoba: {szobaszam}, Dátum: {datum}, Foglaló: {nev}")

def main():
    szalloda = Szalloda("Czellcorp Szálloda")

    for i in range(3):
        szalloda.szoba_hozzaadasa(EgyagyasSzoba(f"{random.randint(1,50)}", 5000))
        szalloda.foglalas(f"{random.randint(1,50)}", "2024-04-15", "Steinberg")
        szalloda.foglalas(f"{random.randint(1,50)}", "2024-04-16", "Steinberg")
        szalloda.foglalas(f"{random.randint(1,50)}", "2024-04-17", "Steinberg")
        szalloda.foglalas(f"{random.randint(1,50)}", "2024-04-18", "Steinberg")
        szalloda.foglalas(f"{random.randint(1,50)}", "2024-04-19", "Steinberg")

    for i in range(3):
        szalloda.szoba_hozzaadasa(EgyagyasSzoba(f"{random.randint(51,100)}", 7500))
        szalloda.foglalas(f"{random.randint(51,100)}", "2024-03-15", "Steinberg")
        szalloda.foglalas(f"{random.randint(51,100)}", "2024-03-16", "Steinberg")
        szalloda.foglalas(f"{random.randint(51,100)}", "2024-03-17", "Steinberg")
        szalloda.foglalas(f"{random.randint(51,100)}", "2024-03-18", "Steinberg")
        szalloda.foglalas(f"{random.randint(51,100)}", "2024-03-19", "Steinberg")

    # szalloda.foglalas("11")
    # szalloda.foglalas("22", "2024-04-16", "Mason")
    # szalloda.foglalas("69", "2024-04-17", "Banános Joe")
    # szalloda.foglalas("75", "2024-04-17", "Wilbur Walsh")
    # szalloda.foglalas("88", "2024-04-17", "Matthew Kirby")
    # szalloda.foglalas("44", "2024-04-17", "David Speed")

    while True:
        print("\nVálasztható műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Kérem, válasszon: ")

        if valasztas == "1":
            szobaszam = input("Add meg a foglalni kívánt szoba számát: ")
            datum = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            nev = input("Add meg a foglaló nevét: ")
            szalloda.foglalas(szobaszam, datum, nev)
        elif valasztas == "2":
            szobaszam = input("Add meg a lemondani kívánt foglalás szoba számát: ")
            datum = input("Add meg a lemondani kívánt foglalás dátumát (YYYY-MM-DD formátumban): ")
            szalloda.lemondas(szobaszam, datum)
        elif valasztas == "3":
            szalloda.foglalasok_listazasa()
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
