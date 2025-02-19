## **Contagem de Elementos**
`Counter` é uma subclasse de `dict` usada para contar elementos de uma sequência.  

```python
from collections import Counter

texto = "banana"
contador = Counter(texto)

print(contador)  # Conta a frequência de cada caractere
print(contador.most_common(1))  # Mostra o item mais comum
print(contador["a"])  # Frequência da letra 'a

```
##### 🖥️ Saída esperada:

```console
$ python script.py
Counter({'a': 3, 'n': 2, 'b': 1})
[('a', 3)]
3
```

---