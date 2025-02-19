## **Dicionário Ordenado**
Garante que a ordem de inserção das chaves seja preservada.

```python
from collections import OrderedDict

d = OrderedDict()
d["nome"] = "Alice"
d["idade"] = 25
d["cidade"] = "São Paulo"

for chave, valor in d.items():
    print(chave, ":", valor)

```
##### 🖥️ Saída esperada:

```console
$ python script.py
nome : Alice
idade : 25
cidade : São Paulo
```

---