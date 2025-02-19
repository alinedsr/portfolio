## **Definir um Valor Padrão**
Permite um argumento opcional com um valor padrão.

```python
import argparse

parser = argparse.ArgumentParser(description="Saudação com valor padrão.")
parser.add_argument("--nome", default="Mundo", help="Nome do usuário")

args = parser.parse_args()

print(f"Olá, {args.nome}!")

```
##### 🖥️ Saídas esperadas:

###### 💠 Sem argumento:
```console
$ python script.py
Olá, Mundo!
```
###### 💠 Com argumento:
```console
$ python script.py --nome Alice
Olá, Alice!
```

---