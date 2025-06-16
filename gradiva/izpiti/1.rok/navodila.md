V datoteki kalup.py imate podan razred sklad  (`Stack`) in pa uporabo sklada za izračun postfiksnega izraza s funkcijo `compute`, ki smo jo definirali na vajah.


1. Funkcija `compute` predpostavlja, da ste podali na vhod povsem pravilno formatiran izraz. Kaj pa če temu ni tako? Zapišite nekaj primerov napačno podanih izrazov in zapišite popravljeno različico te funkcije, ki bo ujela vsaj dve od možnih vrst napak.

2. V funkcijo `compute` dodajte operator `min`, ki najprej iz sklada vzame število $k$, potem pa vzame še $k$ števil iz sklada izmed katerih izračuna minimum. Ta minimum potisne nazaj na sklad.

**Primer:** rezultat spodnjega izraza:
`7 5 3 8 4 min `

je `3` (na skladu ostane zgolj 3)

rezultat izraza:
`7 5 3 8 2 min + + ` pa je 15

3. V funkcijo `compute` dodajte operator `dedup`, ki najprej iz sklada vzame število $k$, potem pa vzame še $k$ števil iz sklada in odstrani duplikate. Na skladu naj bodo elementi v enakem vrstnem redu kot pred odstranjevanjem duplikatov. Izmed enakih elementov pa pustite na skladu prvo pojavitev.


**Primer:** Za izraz:
`1 5 1 3 1 7 5 dedup`
dobimo stanje na skladu (vrh sklada je na desni):
`1 5 3 1 7`


4. Števila na skladu lahko  interpretiramo kot kode za znake po ASCII kodiranju. Implementirajte operator `print`, ki bo vzela števila iz sklada (dokler ni število enako 0 - konec niza) jih pretvoril v znake (funkcija `chr`) in izpisala rezultat.

**Primer:** izraz:
    `0 90 100 114 97 118 111 32 80 101 70 33 print`

izpiše:
`Zdravo PeF!`

