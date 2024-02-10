import pandas as pd # Esta biblioteca permite ler e escrever dados em vários formatos sendo por isso útil na realização deste TPC1

def processar_dataset(arquivo):

    # Dicionário de dados a serem processados
    dados = {
        'modalidades': set(),
        'aptos': 0,
        'inaptos': 0,
        'idade': {}
    }

    # Lê o arquivo CSV
    df = pd.read_csv(arquivo)

    # Calcula o número de atletas federados e não federados
    for index, linha in df.iterrows():
        modalidade = linha['modalidade']
        idade = linha['idade']
        aptidao = linha['resultado']

        dados['modalidades'].add(modalidade)

        if aptidao:  # Se o valor do "resultado" for True
            dados['aptos'] += 1
        else:
            dados['inaptos'] += 1

    # Obtem a menor e a maior idade dos atletas para auxiliar na criaçao dos intervalos
    menor_idade = df['idade'].min()
    maior_idade = df['idade'].max()

    # Calcula os intervalos de idade
    intervalo = 5
    for i in range(menor_idade, maior_idade + 1, intervalo):
        faixa_etaria = f'[{i}-{i+intervalo-1}]'
        dados['idade'][faixa_etaria] = 0

    for index, linha in df.iterrows():
        modalidade = linha['modalidade']
        idade = linha['idade']
        aptidao = linha['resultado']

        dados['modalidades'].add(modalidade)

        if aptidao: # Se a aptidao for true
            dados['aptos'] += 1
        else:
            dados['inaptos'] += 1

        # As idades sao percorridas no dicionario e é verificado se a idade de cada atleta está dentro das faixas etárias, atualizando assim a contagem de atletas
        for faixa_etaria in dados['idade']:
            faixa_min, faixa_max = map(int, faixa_etaria.strip('[]').split('-'))
            if faixa_min <= idade <= faixa_max:
                dados['idade'][faixa_etaria] += 1

    modalidades_ordenadas = sorted(list(dados['modalidades']))

    # Calclua a percentagem dos atletas aptos e inaptos
    total_atletas = dados['aptos'] + dados['inaptos']
    percent_aptos = (dados['aptos'] / total_atletas) * 100
    percent_inaptos = (dados['inaptos'] / total_atletas) * 100

    print("Lista alfabeticamente ordenada das modalidades desportivas:")
    for modalidade in modalidades_ordenadas:
        print(modalidade)
    
    print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
    print(f"Aptos: {percent_aptos:.2f}%")
    print(f"Inaptos: {percent_inaptos:.2f}%")
    
    print("\nDistribuição de atletas por faixa etária:")
    for faixa_etaria, count in dados['idade'].items():
        print(f"{faixa_etaria}: {count}")

# Chama a função para processar o dataset com o caminho para o arquivo emd.csv
processar_dataset('C:\\Users\\marga\\OneDrive\\Ambiente de Trabalho\\emd.csv')

