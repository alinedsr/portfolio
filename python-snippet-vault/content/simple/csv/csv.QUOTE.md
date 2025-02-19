## **Controlando Aspas nos Arquivos CSV**
O `csv.QUOTE_*` permite controlar o uso de aspas ao escrever arquivos CSV.

```python
import csv

dados = [
    ["Nome", "Profissão", "Salário"],
    ["Alice", "Engenheira", "5000"],
    ["Bob", "Médico", '7500'],
    ['Charlie', 'Desenvolvedor, Freelancer', '6000']
]

# Criando um CSV com aspas ao redor dos valores
with open("dados_aspas.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo, quoting=csv.QUOTE_ALL)
    escritor.writerows(dados)

print("Arquivo CSV com aspas criado!")

```
##### 🖥️ Saída esperada:

```console
$ python script.py
Arquivo CSV com aspas criado!
```
##### 📂 Conteúdo do dados.csv:
```console
"Nome","Profissão","Salário"
"Alice","Engenheira","5000"
"Bob","Médico","7500"
"Charlie","Desenvolvedor, Freelancer","6000"
```
---