# Vaje 01 - preizkusimo teren
Ogreli se bomo s par enostavnimi programerskimi nalogami (1-3), razlaga Collatzove domneve sledi na tabli.
Nato sledi eksperimentalna naloga (4),

 1. V datoteki v01-stevila.txt je 100000 celih števil. Preberi datoteko in izpiši koliko je v njej števil, ki so manjša od 100000.

 2. problem Collatzove domneve. Ugotovi, katero število med 1 in 1000000000 potrebuje največ korakov, da doseže 1.

 3. v datoteki v01-slovar.txt je seznam slovenskih besed. Preberi datoteko in povej katera beseda ima največ soglasnikov? Katera beseda ima največjo razliko med številom soglasnikov in samoglasnikov?

 4. Podano imate funkcijo v pythonu:
 ```python
    def f(lst):
    d = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] == lst[j] and lst[i] not in d:
                d.append(lst[i])
    return d
 ```
 - Razmislite, kaj ta funkcija počne? A bi znali zapisati specifikacijo te funkcije ?

 - Narišite krivuljo (podobno kot smo naredili na predavanjih), ki bo pokazala, kako se spreminja čas izvajanja (v povprečju), ko se vhodni seznam povečuje.