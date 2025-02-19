## **Lendo um Arquivo CSV**
O `csv.reader` permite ler os dados de um arquivo CSV linha por linha.

```python
import csv

# Abrindo e lendo o arquivo CSV
with open("dados.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    
    # Convertendo para lista para visualizar melhor
    dados = list(leitor)

# Exibindo os dados lidos
for linha in dados:
    print(linha)

```
##### 🖥️ Saída esperada:

```console
$ python script.py
['Nome', 'Idade', 'Cidade']
['Alice', '25', 'São Paulo']
['Bob', '30', 'Rio de Janeiro']
['Charlie', '22', 'Belo Horizonte']
```

---