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

hissi = Hissi(0, 10)

hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(hissi.alin_kerros)
