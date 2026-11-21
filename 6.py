class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh


class Talaba(Inson):
    def __init__(self, ism, yosh, universitet, baho):
        super().__init__(ism, yosh)
        self.universitet = universitet
        self.baho = baho

    def natija(self):
        if 86 <= self.baho <= 100:
            daraja = "A'lo"
        elif 71 <= self.baho <= 85:
            daraja = "Yaxshi"
        elif 56 <= self.baho <= 70:
            daraja = "Qoniqarli"
        else:
            daraja = "Qoniqarsiz"
        print(f"{self.ism} ({self.universitet}, {self.baho} ball) — {daraja}")


talaba1 = Talaba("Madina", 19, "TATU", 92)
talaba2 = Talaba("Sardor", 20, "O'zMU", 78)
talaba3 = Talaba("Temur", 18, "ADU", 64)
talaba4 = Talaba("Zarina", 19, "Farg'ona politexnika", 49)

talaba1.natija()
talaba2.natija()
talaba3.natija()
talaba4.natija()