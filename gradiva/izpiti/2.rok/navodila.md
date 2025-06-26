V datoteki kalup.py imate podan razred, ki implementira povezani seznam (LinkedList).

Napišite funkcije (v tem razredu):

1. unzip - ki iz enega povezanega seznama elementov `a b c d e f ...` vrne dva povezana seznama elementov `a c e ...` in `b d f ...`.

**Primer:** Če imate seznam:
`7 5 3 8 4 6, kot rezultat dobite dva seznama, 
`7,3,4` in `5,8,6`

Preverite, če funkcija deluje na seznamih sode, lihe dolžine.



2. Funkcijo `takeout(f)`, ki ima kot parameter funkcijo $f$. Ta funkcija sprejme kot parameter eno število in vrača ´True` ali `False.


**Primer:** na seznamu
`9 4 7 5 3 33 67 2`

pokličemo `takeout(f)`, kjer je
```python
def f(n):
    return n%3 == 0
```

Kot rezultat dobimo `9 3 33`.


3. Funkcijo `subsets(n)`, ki vam izpiše vse neprazne podmnožice podanega seznama, katerih vsota je  enaka `n`.

**Primer:** Če imate podan linearni seznam:
    `0 90 100 114 97 118 111 32 80 101 70 33`

in ˙n=643`, so pomnožice, ki se seštejejo v 643 enake:
```
[114, 97, 118, 111, 32, 101, 70]
[0, 114, 97, 118, 111, 32, 101, 70]
[90, 114, 97, 118, 111, 80, 33]
[0, 90, 114, 97, 118, 111, 80, 33]
[100, 114, 97, 118, 80, 101, 33]
[0, 100, 114, 97, 118, 80, 101, 33]
[100, 114, 97, 118, 111, 70, 33]
[0, 100, 114, 97, 118, 111, 70, 33]
```

Uporabite funkcije, ki smo jih na predavanjih implementirali za generiranje terk.
