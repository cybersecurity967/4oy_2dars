class Karta:
    def __init__(self, egasi, raqam_oxiri, balans):
        self.egasi = egasi
        self.raqam_oxiri = str(raqam_oxiri)
        self.balans = balans

    def __str__(self):
        return f"Karta (**{self.raqam_oxiri}) | Egasi: {self.egasi} | Balans: {self.balans:,} so‘m"

    def __gt__(self, other):
        if isinstance(other, Karta):
            return self.balans > other.balans
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Karta):
            return self.balans < other.balans
        return NotImplemented


karta1 = Karta("Ilyosbek", "4821", 3200000)
karta2 = Karta("Javohir", "9014", 5400000)
karta3 = Karta("Malika", "1177", 1800000)

print(karta1)
print(karta2)
print(karta3)

if karta2 > karta1:
    print(f"{karta2.egasi} kartasida mablag' ko'proq.")
elif karta1 > karta2:
    print(f"{karta1.egasi} kartasida mablag' ko'proq.")
else:
    print("Ikkala kartada balans teng.")

print("karta3 balansi karta1 dan kammi?:", karta3 < karta1)