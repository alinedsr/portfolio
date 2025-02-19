## **Tupla Nomeada**
Cria tuplas com nomes para os campos, tornando-as mais legíveis.

```python
from collections import namedtuple

Pessoa = namedtuple("Pessoa", ["nome", "idade", "cidade"])
p1 = Pessoa("Alice", 25, "São Paulo")

print(p1.nome)
print(p1.idade)
print(p1.cidade)

```
##### 🖥️ Saída esperada:

```console
$ python script.py
Alice
25
São Paulo
```

---