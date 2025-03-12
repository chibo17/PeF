# Vaje 04 - uporaba dinamičnih podatkovnih struktur

 1. Izraz: $$(15+4)*(36/6)−8∗3*(48-8)−10+7$$
    zapišite v postfiksi (obratni poljski) notaciji in zapišite zaporedje stanja sklada, ki bi ta izraz izračunal.

    Ali lahko ta izraz v postfiksni obliki preoblikujete tako, da bodo najprej zapisana vsa števila, nato pa vsi operatorji, npr., `1 2 3 + *` ?

 3. Iz C datoteke izpišite vse ujemajoče pare zavitih oklepajev. Za vsak par izpišite vrstico in stolpec v kateri se nahaja.

    ```c
    #include <stdio.h>

    int main() {
        printf("Hello, World!\n");
        return 0;
    }
    ```
    Izpišete:
    ```
    {: 3 12 }: 6,1
    ```
    Predklepaj se torej pojavil v 3. vrstici in 12. stolpcu, pripadajoči zaklepaj pa v 6. vrstici v 1. stolpcu.

    Vsak tak par naj bo izpisan v svoji vrstici, zaporedje teh parov pa ni pomembno.

    Testni program imate med viri v datoteki v04-program.c.

4. Napišite funkcijo (v razred LinkedList):
```python
def add_second(self, x)
```
ki v seznam vedno doda na drugo mesto. 