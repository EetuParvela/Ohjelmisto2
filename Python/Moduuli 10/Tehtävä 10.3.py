class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin_kerros or kerros > self.ylin_kerros:
            print(f"Virhe: Talossa ei ole kerrosta {kerros}.\n")
            return

        while self.nykyinen_kerros < kerros:
            self.kerros_ylös()

        while self.nykyinen_kerros > kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Saavuit {self.nykyinen_kerros}. kerrokseen.")
        else:
            print("Olet jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Saavuit {self.nykyinen_kerros}. kerrokseen.")
        else:
            print("Olet jo alimmassa kerroksessa.")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.lukumäärä = lukumäärä
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(lukumäärä)]

    def aja_hissiä(self, hissin_numero, kerros):
        if 0 <= hissin_numero < len(self.hissit):
            self.hissit[hissin_numero].siirry_kerrokseen(kerros)
            print(f"Kuljit hissillä numero {hissin_numero + 1}, kerrokseen {kerros}.\n")
        else:
            print(f"Virhe: Hissi {hissin_numero + 1} ei ole olemassa.\n")

    def palohälytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät ensimmäiseen kerrokseen.")
        for hissi in self.hissit:
            hissi.nykyinen_kerros = self.alin_kerros

talo = Talo(0, 10, 4)
talo.aja_hissiä(3, 5)
talo.aja_hissiä(1, 2)

talo.palohälytys()