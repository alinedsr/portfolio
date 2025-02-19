## **Definir Quantidade de Argumentos**
Permite múltiplos valores para um argumento.

```python
import argparse

parser = argparse.ArgumentParser(description="Soma de múltiplos números.")
parser.add_argument("numeros", type=int, nargs="+", help="Números para somar")

args = parser.parse_args()

print(f"Soma: {sum(args.numeros)}")

```
##### 🖥️ Saída esperada:

```console
$ python script.py 1 2 3 4 5
Soma: 15
```

---