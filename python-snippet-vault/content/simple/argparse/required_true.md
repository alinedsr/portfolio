## **Tornar Argumentos Obrigatórios**
Define um argumento opcional como obrigatório.

```python
import argparse

parser = argparse.ArgumentParser(description="Nome obrigatório.")
parser.add_argument("--nome", required=True, help="Nome do usuário")

args = parser.parse_args()

print(f"Olá, {args.nome}!")

```
##### 🖥️ Saídas esperadas:

###### 💠 Sem argumento:

```console
$ python script.py
error: the following arguments are required: --nome
```

###### 💠 Com argumento:

```console
$ python script.py --nome Alice
Olá, Alice!
```

---