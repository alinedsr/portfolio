## **Escrevendo em um Arquivo CSV**
O `csv.writer` permite escrever dados em um arquivo CSV linha por linha.

```python
import csv

# Criando e escrevendo em um arquivo CSV
with open("dados.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    
    # Escrevendo o cabeçalho
    escritor.writerow(["Nome", "Idade", "Cidade"])
    
    # Escrevendo algumas linhas de dados
    escritor.writerow(["Alice", 25, "São Paulo"])
    escritor.writerow(["Bob", 30, "Rio de Janeiro"])
    escritor.writerow(["Charlie", 22, "Belo Horizonte"])

print("Arquivo CSV criado com sucesso!")

```
##### 🖥️ Saída esperada:

```console
$ python script.py
Arquivo CSV criado com sucesso!
```
##### 📂 Conteúdo do dados.csv:
```console
Nome,Idade,Cidade
Alice,25,São Paulo
Bob,30,Rio de Janeiro
Charlie,22,Belo Horizonte
```
---