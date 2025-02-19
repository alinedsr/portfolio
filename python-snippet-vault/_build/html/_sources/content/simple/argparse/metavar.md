## **Melhorar a Ajuda do Comando**
Personaliza a exibição dos argumentos na ajuda do script.

```python
import argparse

parser = argparse.ArgumentParser(description="Exemplo de metavar.")
parser.add_argument("arquivo", metavar="ARQUIVO", help="Nome do arquivo a ser processado")

args = parser.parse_args()

print(f"Processando o arquivo: {args.arquivo}")

```
##### 🖥️ Saídas esperadas:

###### 💠 Com metavar:

```console
$ python script.py --help
usage: script.py ARQUIVO
```

###### 💠 Sem metavar:

```console
usage: script.py arquivo
```

---