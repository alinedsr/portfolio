## 🗂️ Listar Arquivos em um Diretório

##### 📌 Código:

```python
import os

class ListarArquivos:
    """
    Classe para listar arquivos em um diretório.
    """

    def __init__(self, diretorio):
        """
        Inicializa a classe com o caminho do diretório.

        :param diretorio: Caminho do diretório a ser listado.
        """
        self.diretorio = diretorio

    def listar(self):
        """
        Lista os arquivos do diretório.

        :return: Lista de arquivos no diretório.
        """
        try:
            # Obtém a lista de arquivos e diretórios no caminho especificado
            itens = os.listdir(self.diretorio)

            # Filtra apenas arquivos, ignorando subdiretórios
            arquivos = [item for item in itens if os.path.isfile(os.path.join(self.diretorio, item))]

            # Imprime os arquivos encontrados
            if arquivos:
                print("Arquivos encontrados:")
                for arquivo in arquivos:
                    print(f"- {arquivo}")
            else:
                print("Nenhum arquivo encontrado no diretório.")

            return arquivos

        except FileNotFoundError:
            print("Erro: O diretório especificado não existe.")
            return []
        except PermissionError:
            print("Erro: Permissão negada para acessar este diretório.")
            return []
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return []

# Obtém o diretório atual
diretorio_atual = os.getcwd()

# Cria uma instância da classe
listador = ListarArquivos(diretorio_atual)

# Chama o método para listar os arquivos
arquivos_encontrados = listador.listar()

```
##### 📌 Saídas esperadas:

###### ✅ Caso o diretório tenha arquivos:

```console
Arquivos encontrados:
- arquivo1.txt
- arquivo2.py
- imagem.png
```
###### ⚠️ Caso o diretório esteja vazio:

```console
Nenhum arquivo encontrado no diretório.
```
###### ❌ Caso o diretório não exista:

```console
Erro: O diretório especificado não existe.
```
###### ❌ Caso não tenha permissão de acesso ao diretório:

```console
Erro: Permissão negada para acessar este diretório.
```
###### ⚠️ Caso ocorra outro erro inesperado (exemplo, erro de sistema):

```console
Erro inesperado: [descrição do erro]
```