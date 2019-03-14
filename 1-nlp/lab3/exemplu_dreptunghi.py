###############################################################################
# Exemplu de fișier cu clase.
###############################################################################

class Dreptunghi:
    """O clasă care memorează un dreptunghi format din caractere"""
    # atribute de clasă (statice)
    liniiSeparatoare = True
    simbolSeparator = "-"
    dimLinieSeparatoare = 15

    def __init__(self, inaltime, latime, simbolContinut, simbolContur = None):
        # atribute de instanță
        self.inaltime = inaltime
        self.latime = latime
        self.simbolContinut = simbolContinut
        self.simbolContur = "#" if simbolContur is None else simbolContur

    def arie(self):
        return self.inaltime*self.latime

    @classmethod
    def afisSimbolContur(cls):
        print('Simbol separator: ' + cls.simbolSeparator)

    @classmethod
    def afisNumeClasa(cls):
        print('Nume clasa:\n' + cls.__name__)

    @classmethod
    def afisDoc(cls):
        print('Informatii clasa:\n' + cls.__doc__)

    @staticmethod
    def afisLinie(n, simbol):
        print(n*simbol)

    # operatori
    def __eq__(self, dr):
        return (self.inaltime == dr.inaltime and self.latime == dr.latime)

    def __lt__(self, dr):
        return self.arie() < dr.arie()

    def __lte__(self, dr):
        return self.arie() <= dr.arie()

    def __gt__(self, dr):
        return self.arie() > dr.arie()

    # definesc ce va returna repr(obiect)
    def __repr__(self):
        sir = "Prop. clasa:\n"
        for (k, v) in self.__class__.__dict__.items():
            sir += "{} = {}\n".format(k, v)
            sir = "Prop. instanta:\n"
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return(sir)

    # definesc ce va returna str(obiect)
    def __str__(self):
        sir = self.simbolContur*self.latime + "\n"
        for i in range(self.inaltime - 2):
            sir += self.simbolContur + self.simbolContinut * (self.latime - 2) + \
                self.SimbolContur + "\n"
            sir += self.simbolContur*self.inaltime+"\n"
            return(sir)

    def afis(self):
        if (self.liniiSeparatoare):
            self.afisLinie(self.dimLinieSeparatoare, self.simbolSeparator)
            print(d)
        if (self.liniiSeparatoare):
            self.afisLinie(self.dimLinieSeparatoare, self.simbolSeparator)

class Secventa:
    secventa = 0
    def __init__(self):
        self.secventa += 1

class HartaJoc(Dreptunghi, Secventa):
    simbolObstacol = "@"
    __matrice__ = []
    def __init__(self, nume, inaltime, latime, simbolContinut, simbolContur = None):
        Dreptunghi.__init__(self, inaltime, latime, simbolContinut, simbolContur)
        Secventa.__init__(self)
        sirDr = str(self)
        __matrice__ = [[] for i in range(inaltime)]
        self.nume = nume

    def afis(self):
        if (self.liniiSeparatoare):
            self.afisLinie(self.dimLinieSeparatoare, self.simbolSeparator)
        for linie in __matrice__:
            print(linie.join())
        if (self.liniiSeparatoare):
            self.afisLinie(self.dimLinieSeparatoare, self.simbolSeparator)


if __name__ == "__main__":
    dl = Dreptunghi(5, 10, '.')
    print("Am creat dreptunghiul")

    print("Ce afișează print(dl):")
    print(dl)

    print("Ce afișează print(str(dl))")
    print(repr(dl))

    d2 = Dreptunghi(4, 4, '.')
    Dreptunghi.afisSimbolContur()
    Dreptunghi.afisNumeClasa()
    Dreptunghi.afisDoc()

    print("Am creat harta h = HartaJoc('campie', 5, 10, '.')")
    h = HartaJoc('campie', 5, 10, '.')

    print("Ce afișează print(h):")
    print(h)

    print("Ce afișează print(repr(h))")
    print(repr(h))
