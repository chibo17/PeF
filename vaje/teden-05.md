# Seznami (že spet) in razpršene tabele

1. Napišite sledeče funkcije (v razredu LinkedList):
    - map(self, f), ki vsak element seznama (self) spremeni s funkcijo f
    - double(self), ki spremeni seznam tako, da vsak element trenutnega seznama podvoji. Npr. če imamo seznam 1,2,3,4, potem dobimo seznam 1,1,2,2,3,3,4,4
    - halve(self), ki iz trenutnega seznama odstrani vsak drugi element. Iz seznama z elementi 1,2,3,4 tako nastane seznam 1,3 

Vse tri funkcije zapišite na dva načina: 1) z uporabo rekurzije in 2) brez uporabe rekurzije.

2. Podan je niz "perica reže raci rep". Vsak znak si lahko predstavljamo kot število - recimo, da je to zaporedna številka tega znaka v slovenski abecedi. Presledek pa ima vrednost 0. Denimo, da lahko iz vsakega niza dobimo število tako, da seštejemo vrednosti znakov v tem nizu.
    Preslikajte zgoraj podani niz z
    - metodo deljenja,
    - metodo množenja 
Ciljna tabela naj bo velika 31.

Ali lahko najdete dve slovenski besedi, ki se s to metodo preslikata v isto število.


3. Med viri imate podano datoteko v01-slovar.txt s seznamom slovenskih besed. Shranite vse besede v razpršeno tabelo, kjer trke razrešujete z veriženjem. Za obe razprševalni funkciji (metoda množenja in metoda deljenja) izmerite, koliko je:
-  **povprečna dolžina seznamov** v tabeli in
- **največja dolžina seznamov** v tabeli.