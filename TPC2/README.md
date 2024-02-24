# Conversor de Markdown para *HTML*
O programa desenvolvido neste TPC2 permite converter texto formatado em *Markdown* para **HTML**. 
Este pode ser executado via linha de comando, aceitando como argumento o texto em *Markdown* ou o caminho para um arquivo *Markdown*.

## Funcionalidades
# 1. Conversão de Formatação de Texto
Cabeçalhos: Transforma os cabeçalhos Markdown (usando #, ##, ###, etc.) em tags *HTML* correspondentes, como "h1", "h2", "h3", etc.

**Negrito**: Converte texto envolto em ** para a tag *HTML* "strong".

**Itálico**: Converte texto envolto em * para a tag *HTML* "em".

**Citação em Bloco**: Converte linhas que começam com > para a tag *HTML* "blockquote".

**Lista Ordenada**: Transforma os elementos de listas ordenadas em tags *HTML* "ol".

**Lista Não Ordenada**: Transforma os elementos de listas não ordenadas em tags *HTML* "ul".

**Código**: Converte texto envolto por ` para a tag *HTML* "code".

**Linha Horizontal**: Converte sequências de --- em uma linha para a tag *HTML* "hr".

**Link**: Converte links Markdown texto para a tag *HTML* "a".

**Imagem**: Converte imagens Markdown texto para a tag *HTML* "img".

# 2. Verificação e Conversão de Arquivos
O script verifica se o argumento fornecido é um arquivo existente.

Se for um arquivo, ele lê o conteúdo do arquivo Markdown, converte para *HTML* e escreve em um novo arquivo chamado output.*html*.

Se for um texto fornecido diretamente como argumento, ele converte o texto Markdown para *HTML* e imprime na tela.

# 3. Modo de Utilização
python3 tpc2_pl.py <"MarkdownText"/MarkdownFile.md>
O *<"MarkdownText"/MarkdownFile.md>* pode ser um texto entre aspas duplas ou o caminho para um arquivo *Markdown*.