## **Escrevendo CSV com Dicionários**
O `csv.DictWriter` permite escrever arquivos CSV usando dicionários.

```python
import csv

# Criando e escrevendo usando dicionários
with open("dados_dict.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    colunas = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)

    # Escrevendo o cabeçalho
    escritor.writeheader()

    # Escrevendo os dados como dicionário
    escritor.writerow({"Nome": "Alice", "Idade": 25, "Cidade": "São Paulo"})
    escritor.writerow({"Nome": "Bob", "Idade": 30, "Cidade": "Rio de Janeiro"})
    escritor.writerow({"Nome": "Charlie", "Idade": 22, "Cidade": "Belo Horizonte"})

print("Arquivo CSV criado com sucesso usando DictWriter!")

```
##### 🖥️ Saída esperada:

```console
$ python script.py
Arquivo CSV criado com sucesso usando DictWriter!
```
##### 📂 Conteúdo do dados.csv:
```console
Nome,Idade,Cidade
Alice,25,São Paulo
Bob,30,Rio de Janeiro
Charlie,22,Belo Horizonte
```
---