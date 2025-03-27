class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" {self.sivumäärä} sivua, {self.kirjoittaja}.")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" {self.päätoimittaja}.")

aku = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_no6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku.tulosta_tiedot()
hytti_no6.tulosta_tiedot()