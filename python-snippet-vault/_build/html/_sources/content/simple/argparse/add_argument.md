## **Criar um Argumento Simples**
Define um argumento obrigatório para o script.

```python
import argparse

parser = argparse.ArgumentParser(description="Exemplo de argumento obrigatório.")
parser.add_argument("nome", help="Nome do usuário")

args = parser.parse_args()

print(f"Olá, {args.nome}!")

```
##### 🖥️ Saída esperada:

```console
$ python script.py Alice
Olá, Alice!
```

---