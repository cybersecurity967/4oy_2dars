class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx


class Savat:
    def __init__(self, nom, mahsulotlar=None):
        self.nom = nom
        self.mahsulotlar = list(mahsulotlar) if mahsulotlar is not None else []

    def qoshish(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        return sum(m.narx for m in self.mahsulotlar)

    def __str__(self):
        return f"Savat: {self.nom} ({len(self)} ta mahsulot)"


savat1 = Savat("Asosiy savat")
savat1.qoshish(Mahsulot("Mexanik klaviatura", 450000))
savat1.qoshish(Mahsulot("Sichqoncha", 180000))
savat1.qoshish(Mahsulot("Quloqchin", 320000))

savat2 = Savat("Bo'sh savat")

print(savat1)
if savat1:
    print(f"Umumiy narx: {savat1.umumiy_narx():,} so‘m")
else:
    print("Savat bo'sh.")

print(savat2)
if savat2:
    print(f"Umumiy narx: {savat2.umumiy_narx():,} so‘m")
else:
    print("Savat bo'sh.")