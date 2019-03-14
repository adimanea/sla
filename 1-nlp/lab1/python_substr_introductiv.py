######################################################################
# Citește un șir de la tastatură și afișează:
# (a) pe cîte un rînd șirul rotit cu o poziție la stînga;
# (b) șirul rotit la dreapta cu o poziție;
# (c) pe același rînd prima|ultima literă \n primele două|ultimele 2 etc.
######################################################################

sir = input("Introduceți un șir" + "\n")
lungime = len(sir)

print("(a) rotește șirul la stînga cu cîte o poziție")
print("(b) rotește șirul la dreapta cu cîte o poziție")
print("(c) păstrează primele i și ultimele i litere din șir")
opt = input("Opțiune: ")

if str(opt) == "a":
    def Srotire(s, d):
        """ Funcție care rotește șirul s
        la stînga cu d poziții """
        Sfirst = s[0:d]
        Ssecond = s[d:]
        # concatenează
        print(Ssecond + Sfirst)
    for i in range(1, lungime):
        Srotire(sir, i)

if str(opt) == "b":
    def Drotire(s, d):
        """ Funcție care rotește șirul s
        la dreapta cu d poziții """
        Dfirst = s[0: len(s) - d]
        Dsecond = s[len(s) - d:]
        # concatenează
        print(Dsecond + Dfirst)
    for i in range(1, lungime):
        Drotire(sir, i)

if str(opt) == "c":
    for i in range(1, int(lungime/2) + 1):
        print(sir[:i] + "|" + sir[-i:])
        print

print("=====PROGRAM FINALIZAT=====")
