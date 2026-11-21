class Transport:
    def harakatlanish(self):
        print("Transport harakatlanmoqda.")


class Mashina(Transport):
    def harakatlanish(self):
        print("Mashina yolda harakatlanmoqda.")


class Velosiped(Transport):
    def harakatlanish(self):
        print("Velosiped pedal aylanishi bilan yurmoqda.")


class Poyezd(Transport):
    def harakatlanish(self):
        print("Poyezd relslar bo'ylab taqir-tuqur harakatlanmoqda.")


transportlar = [
    Mashina(),
    Velosiped(),
    Poyezd(),
    Mashina(),
    Velosiped(),
]

for t in transportlar:
    t.harakatlanish()