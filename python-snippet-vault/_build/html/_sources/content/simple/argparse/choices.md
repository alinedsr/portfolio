## **Restringir Valores**
Limita as opções disponíveis para um argumento.

```python
import argparse

parser = argparse.ArgumentParser(description="Escolha uma operação matemática.")
parser.add_argument("operacao", choices=["soma", "subtracao"], help="Escolha entre soma ou subtracao")
parser.add_argument("a", type=int, help="Primeiro número")
parser.add_argument("b", type=int, help="Segundo número")

args = parser.parse_args()

if args.operacao == "soma":
    print(f"Resultado: {args.a + args.b}")
else:
    print(f"Resultado: {args.a - args.b}")

```
##### 🖥️ Saídas esperadas:

###### 💠 Valor válido:

```console
$ python script.py soma 5 3
Resultado: 8
```

###### 💠 Valor inválido:

```console
$ python script.py multiplicacao 5 3
error: argument operacao: invalid choice: 'multiplicacao' (choose from 'soma', 'subtracao')
```

---