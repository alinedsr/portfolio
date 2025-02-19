## **Lendo CSV como Dicionário**
O `csv.DictReader` permite ler arquivos CSV diretamente em formato de dicionário.

```python
import csv

# Lendo arquivo CSV como dicionário
with open("dados_dict.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)

```
##### 🖥️ Saída esperada:

```console
$ python script.py
{'Nome': 'Alice', 'Idade': '25', 'Cidade': 'São Paulo'}
{'Nome': 'Bob', 'Idade': '30', 'Cidade': 'Rio de Janeiro'}
{'Nome': 'Charlie', 'Idade': '22', 'Cidade': 'Belo Horizonte'}
```

---