class Kitob:
    def __init__(self, nom, muallif, sahifa_soni):
        self.nom = nom
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def malumot(self):
        print(f"Kitob: {self.nom} | Muallif: {self.muallif} | Sahifalar: {self.sahifa_soni}")


class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, sahifa_soni, format_turi, fayl_hajmi):
        super().__init__(nom, muallif, sahifa_soni)
        self.format_turi = format_turi
        self.fayl_hajmi = fayl_hajmi

    def malumot(self):
        super().malumot()
        print(f"  Format: {self.format_turi.upper()} | Hajmi: {self.fayl_hajmi} MB")


k1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 320)
k2 = Kitob("Python asoslari", "Muallif", 250)
ek1 = ElektronKitob("Clean Code", "Robert Martin", 464, "pdf", 12.5)
ek2 = ElektronKitob("Fluent Python", "Luciano Ramalho", 792, "epub", 8.4)

k1.malumot()
k2.malumot()
ek1.malumot()
ek2.malumot()