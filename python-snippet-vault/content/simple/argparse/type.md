## **Definir o Tipo do Argumento**
Força um argumento a ser um número inteiro.

```python
import argparse

parser = argparse.ArgumentParser(description="Calculadora simples.")
parser.add_argument("numero", type=int, help="Número a ser dobrado")

args = parser.parse_args()

print(f"O dobro de {args.numero} é {args.numero * 2}")

```
##### 🖥️ Saída esperada:

```console
$ python script.py 5
O dobro de 5 é 10
```

---