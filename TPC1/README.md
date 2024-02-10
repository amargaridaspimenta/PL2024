# Descrição do TPC1
Este projeto contém uma função chamada `processar_dataset` que é responsável por processar um conjunto de dados de atletas relacionados às modalidades, às idades e aptidão dos mesmos.
Para além disso, são utilizados outros métodos auxiliares que promovem alcançar o resultado desejado como por exemplo, obter as maior e menor idades de modo a criar
faixas etárias relistas e com cálculos corretos tendo em conta o ficheiro fornecido.

De modo a facilitar a leitura dos dados, recorri á biblioteca `pandas` pois considero que facilita o processo de leitura dos dados.

# Função 'processar_dataset'
A função `processar_dataset` recebe o caminho para um arquivo CSV que contém os dados dos atletas. Esta lê o arquivo, ordena alfabeticamente as modalidades, distribui
o número de atletas pelas suas respetivas faixas etárias e calcula a percentagem dos atletas aptos e inaptos.

# Parâmetros da função 'processar_dataset'
- `arquivo`: Caminho para o arquivo CSV que contém os dados dos atletas, neste caso o arquivo 'emd.csv'.

# Output
A função `processar_dataset` imprime os resultados pedidos, sendo eles:
- Uma lista ordenada alfabeticamente das modalidades desportivas;
- As percentagens dos atletas aptos e inaptos;
- Distribuição dos atletas por faixa etária;

# Informações
Após o programa ser executado com sucesso, é produzido um arquivo `informacoes.txt` onde é possível verificar o resultado obtido a partir dos dados do ficheiro fornecido.
