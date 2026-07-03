from markitdown import MarkItDown
import os

md = MarkItDown()
arquivo_entrada = "empresa_oeste.pdf"
arquivo_saida = r"C:\Users\aluis\OneDrive\Documentos\tiolu\resultado_pdf.md"

print(f"Processando {arquivo_entrada}...")
resultado = md.convert_local(arquivo_entrada)

with open(arquivo_saida, "w", encoding="utf-8") as f:
    f.write(resultado.text_content)
    
print(f"Sucesso! Arquivo salvo em {arquivo_saida}")

# o comando para rodar é: uv run main.py

# Teste lalalala pra ver o github!