## **Criando um Argumento de Flag**
Cria uma opção booleana para ativar/desativar um recurso.

```python
import argparse

parser = argparse.ArgumentParser(description="Modo detalhado ativado.")
parser.add_argument("--verbose", action="store_true", help="Ativa o modo detalhado")

args = parser.parse_args()

if args.verbose:
    print("Modo detalhado ativado!")
else:
    print("Modo normal.")

```
##### 🖥️ Saídas esperadas:

###### 💠 Sem Flag:

```console
$ python script.py
Modo normal.
```

###### 💠 Com Flag:

```console
$ python script.py --verbose
Modo detalhado ativado!
```

---