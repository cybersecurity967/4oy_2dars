class Telefon:
    def __init__(self, brend, model, narx):
        self.brend = brend
        self.model = model
        self.narx = narx

    def __str__(self):
        narx_format = f"{self.narx:,}".replace(",", " ")
        return f"{self.brend} {self.model} — {narx_format} so‘m"

    def __eq__(self, other):
        if isinstance(other, Telefon):
            return self.narx == other.narx
        return False


t1 = Telefon("Samsung", "A54", 4500000)
t2 = Telefon("Redmi", "Note 13", 4500000)
t3 = Telefon("iPhone", "15", 11500000)

print(t1)
print(t2)
print(t3)
print("t1 va t2 narxi tengmi?:", t1 == t2)
print("t1 va t3 narxi tengmi?:", t1 == t3)