# Sestopanje


### Ne želim
Za majhen nabor učencev bomo ustvarili "konfliktni graf". Vozlišča v grafu so učenci. Povezava med dvema učencema obstaja, če se ne smeta pojaviti v isti skupini (tj. eden od njih ima drugega na seznamu "ne želim z").

Vhodni podatki (učenci in njihove "ne želim z" želje):

**Učenci**: Ana, Bor, Cilka, David, Eva, Filip

**Ne želim z**:
Ana: David, Filip
Bor: Eva
Cilka: Filip
David: Bor, Eva
Eva: Bor, Ana
Filip: Cilka

Napišite sled izvajanja sestopanja pri reševanju problema: Ali je mogoče te otroke razporediti v 2 skupini?

Uporabite tudi rezanje s preverjanjem naprej.


### Barvanje s sestopanjem
Na prejšnjih predavanjih smo implementirali funkcijo `find_coloring(graph,k)`, kjer smo z grobo silo preiskali vsa možna barvanja.

Implementirajte to funkcijo s sestopanjem:

 - najprej naredite  sestopanje brez rezanja
- nato dodajte rezanje s pregledovanjem nazaj
- **dodatno** implementirajte rezanje s pregledovanjem naprej

