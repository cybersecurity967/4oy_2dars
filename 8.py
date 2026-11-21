class FilmKutubxonasi:
    def __init__(self, nom, filmlar=None):
        self.nom = nom
        self.filmlar = list(filmlar) if filmlar is not None else []

    def film_qosh(self, film):
        self.filmlar.append(film)

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, index):
        return self.filmlar[index]

    def __contains__(self, film):
        return film in self.filmlar


kutubxona1 = FilmKutubxonasi("Kino Olami")
kutubxona1.film_qosh("Inception")
kutubxona1.film_qosh("Interstellar")
kutubxona1.film_qosh("The Matrix")

kutubxona2 = FilmKutubxonasi("Klassika", ["Fight Club", "Pulp Fiction", "Gladiator"])

print(f"{kutubxona1.nom}dagi filmlar soni:", len(kutubxona1))
print("1-indeksdagi film:", kutubxona1[1])
print("'Inception' bormi?:", "Inception" in kutubxona1)
print("'Avatar' bormi?:", "Avatar" in kutubxona1)

print(f"\n{kutubxona2.nom}dagi filmlar soni:", len(kutubxona2))
print("0-indeksdagi film:", kutubxona2[0])
print("'Gladiator' bormi?:", "Gladiator" in kutubxona2)