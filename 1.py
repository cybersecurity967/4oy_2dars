class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def ovoz(self):
        print(f"{self.nomi} ovoz chiqaryapti.")


class It(Hayvon):
    def qoriqlash(self):
        print(f"{self.nomi} ({self.yoshi} yosh) hovlini qo'riqlayapti.")


class Mushuk(Hayvon):
    def sichqon_tutish(self):
        print(f"{self.nomi} ({self.yoshi} yosh) sichqon tutyapti.")


it1 = It("Rex", 3)
it2 = It("Bobik", 5)
mushuk1 = Mushuk("Mosh", 2)
mushuk2 = Mushuk("Tom", 4)

it1.ovoz()
it1.qoriqlash()
it2.ovoz()
it2.qoriqlash()

mushuk1.ovoz()
mushuk1.sichqon_tutish()
mushuk2.ovoz()
mushuk2.sichqon_tutish()