## **Lista de Alta Performance**
Permite inserção e remoção eficiente dos dois lados da estrutura.

```python
from collections import deque

fila = deque(["Alice", "Bob", "Charlie"])

fila.append("David")  # Adiciona no final
fila.appendleft("Eve")  # Adiciona no início
print(fila)

fila.pop()  # Remove do final
fila.popleft()  # Remove do início
print(fila)
```
##### 🖥️ Saída esperada:

```console
$ python script.py
deque(['Eve', 'Alice', 'Bob', 'Charlie', 'David'])
deque(['Alice', 'Bob', 'Charlie'])
```

---