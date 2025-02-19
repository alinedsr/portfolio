## **Combinar Múltiplos Dicionários**
Garante que a ordem de inserção das chaves seja preservada.

```python
from collections import ChainMap

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

cm = ChainMap(d1, d2)

print(cm["a"])  # Pega de d1
print(cm["b"])  # Usa o primeiro 'b' encontrado (d1)
print(cm["c"])  # Pega de d2

```
##### 🖥️ Saída esperada:

```console
$ python script.py
1
2
4
```

---