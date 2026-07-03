Na prática você vai abrir a pasta do projeto no VSCODE,

rodar esse comando de ativação do ambiente virtual:

.venv\Scripts\activate

E depois rodar o codigo com:

uv run main.py


obviamente alterando o caminho dos arquivos nos respectivos paths do codigo.

=)


COMANDOS DE GITHUB - 90% das vezes vc vai executar esses 4 comandos em sequencia:
atenção para adicionar os arquivos SIGILIOSOS e que vc nao quer expor online no arquivo .gitignore (O DA RAIZ DO PROJETO)

1) VERIFICAR O STATUS ATUAL DOS ARQUIVOS
git status

2) ADICIONAR ARQUIVOS PARA O STATUS STAGED
git add .

3) COMMITAR
git commit -m "descricao do commit feito"

4) ENVIAR DE FATO PARA O GITHUB
git push