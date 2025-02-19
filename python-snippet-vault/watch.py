from livereload import Server, shell
import os

# Garante que a pasta _build/html/ existe antes de rodar
if not os.path.exists("_build/html"):
    print("⚠️ Erro: A pasta _build/html não foi encontrada. Rode 'jupyter-book build .' primeiro.")
    exit(1)

# Função para rebuildar o Jupyter Book
def build():
    shell("jupyter-book build .")()

# Configura o LiveReload
server = Server()

# Monitora mudanças e rebuilda automaticamente
server.watch("content/**/*.md", build)
server.watch("_toc.yml", build)
server.watch("_config.yml", build)

# Serve os arquivos HTML gerados e atualiza automaticamente no navegador
server.serve(port=8000, root="_build/html", open_url_delay=1)
