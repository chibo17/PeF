Spomnimo se definicije razreda BST, ki predstavlja vozlišče dvojiškega drevesa:
```python
class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```

Kot delovni primer vzemimo spodnje drevo:
![](img\ex_tree1.png)

0. V kalupu imate podano funkcijo `tree_from_list`, kakšen seznam morate podati tej funkciji, da dobite točno tako drevo, kot je na zgornji sliki?

1. napišite funkcijo (v razredu BST) `hide_even`, ki izpiše vse elemente drevesa v vrstnem redu `in order`. Če je število sodo, izpišite samo `_`.

**Primer:** za drevo na sliki dobimo izpis:
`3 _ _ 29 31 35 _ 51`

2. napišite funkcijo (v razredu BST) `hide_right`, ki izpiše vse elemente drevesa v vrstnem redu `in order`. Če se pa število nahaja v desnem poddrevesu (od korena), potem izpišite `_X`, kjer je `X` zadnja števka (enica) v zapisu tega števila.

**Primer:** za drevo na sliki dobimo izpis:
`3 18 22 29 _1 _5 _4 _1`

3. Napišite funkcijo `sum_level(level)`, ki vrne vsoto vseh elementov drevesa, ki so na globini `level`.

**Primer:** za drevo na sliki klic:
    - `sum_level(3)` vrne 35
    - `sum_level(0)` vrne 29
    - `sum_level(1)` vrne 62

