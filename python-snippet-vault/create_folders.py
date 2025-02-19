import os

# Diretório onde os arquivos Markdown estão armazenados
root_dir = "C:/dev/portfolio/python-snippet-vault/content"

# Percorre todos os arquivos do projeto
for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(subdir, file)
            try:
                # Lê o conteúdo garantindo UTF-8
                with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()

                # Remove caracteres ocultos e substituições inesperadas
                clean_content = content.replace("�", "").replace("\r", "").strip()

                # Escreve o conteúdo de volta no arquivo com UTF-8 limpo
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(clean_content)

                print(f"✅ Arquivo corrigido: {file_path}")

            except Exception as e:
                print(f"❌ Erro ao processar {file_path}: {e}")
