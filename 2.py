class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh


class Oqituvchi(Xodim):
    def __init__(self, ism, maosh, fan):
        super().__init__(ism, maosh)
        self.fan = fan

    def malumot(self):
        print(f"O'qituvchi: {self.ism} | Fan: {self.fan} | Maosh: {self.maosh}")


class Farrosh(Xodim):
    def __init__(self, ism, maosh, qavat):
        super().__init__(ism, maosh)
        self.qavat = qavat

    def malumot(self):
        print(f"Farrosh: {self.ism} | Qavat: {self.qavat} | Maosh: {self.maosh}")


oqituvchi1 = Oqituvchi("Aziza", 4500000, "Informatika")
oqituvchi2 = Oqituvchi("Jasur", 5000000, "Matematika")
farrosh1 = Farrosh("Dilbar", 2500000, 1)
farrosh2 = Farrosh("Karima", 2500000, 2)

oqituvchi1.malumot()
oqituvchi2.malumot()
farrosh1.malumot()
farrosh2.malumot()