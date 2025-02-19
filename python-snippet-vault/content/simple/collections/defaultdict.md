## **Dicionário com Valores Padrão**
`defaultdict` evita erros ao acessar chaves inexistentes, atribuindo um valor padrão automaticamente.

```python
from collections import defaultdict

# Cria um defaultdict com lista como valor padrão
d = defaultdict(list)

d["frutas"].append("banana")
d["frutas"].append("maçã")
d["legumes"].append("cenoura")

print(d["frutas"])
print(d["legumes"])
print(d["nao_existe"])  # Retorna lista vazia ao invés de erro

```
##### 🖥️ Saída esperada:

```console
$ python script.py
['banana', 'maçã']
['cenoura']
[]
```

---