####################################################
# Desenvolvido por maicon ribeiro
# inicio 27/04/2024
# fim 27/04/2024
#
# esse arquivo contém as funções necessárias para buscar dados do ipea
# A API em questão pode ser vista em: https://www.luanborelli.net/ipeadatapy/docs/index.html
# diferente das outras bases de dados, nesse caso usarei a api ipeadatapy invés de fazer leitura de um arquivo baixado no site

# Por motivos desconhecidos o site do IPEA esteve indisponível no dia 26/04/2024 e retornou apenas na noite do dia 27.
# Se essas falhas no funcionamento forem frequentes, a busca de dados pela API torna-se inviável. Nesse caso, mantive para fins de exemplificação da forma de buscar dados


import conexao
import math
import pandas as pd
import ipeadatapy


def criaTabela():
    # Função para a criação da tabela dos dados do ipea
    # Os campos dessa tabela foram definidos a partir de uma análise dos dados disponibilizados pela ipeadatapy
    # A API retorna informações sobre uma série de dados. Isso é, devolve por exemplo informações sobre IPVA em várias datas
    # Sempre que invocamos a api ela nos retorna várias linhas contendo informações sobre a série buscada
    # Decidi adicionar colunas para cada tipo de informação obtida (ICMS,IPVA,IR...)
    # Parâmetros    - Nenhum
    # Retorno       - Nenhum
    queryCriaTabela = """
        
        CREATE TABLE IF NOT EXISTS public.ipea (
            id int4 DEFAULT nextval('sqipea'::regclass) NULL,
            "data" date NOT NULL,
            dia int2 NOT NULL,
            mes int2 NOT NULL,
            ano int2 NOT NULL,
            ir numeric NULL,
            icms numeric NULL,
            ie numeric NULL,
            ii numeric NULL,
            iof numeric NULL,
            ipi numeric NULL,
            ipva numeric NULL,
            itr numeric NULL,
            orad numeric NULL,
            CONSTRAINT ipea_data_pk UNIQUE (data),
            CONSTRAINT ipea_pk UNIQUE (id)
        );
    """
    conexao.consulta(queryCriaTabela,False)
    limpaTabela = "TRUNCATE TABLE public.ipea"
    conexao.consulta(limpaTabela,False)
    print("Tabela criada com sucesso")


def retornaNomeColuna(nomeSerie):
    # recebe o nome da série definida pela API e retorna o nome do campo do banco de dados
    # Cada série de dados possui prefixo e sufixo igual. Para simplificar, vamos desprezar essa parte
    # Exemplo: CONFAZ12_IPVAPA12 - Desprezamos o prefixo até o '_' e os últimos 4 dígitos também. Permanecendo assim apenas o 'IPVA'

    # parametro: nomeSerie (string) Nome da série de dados definidos na API
    # retorno: serie (string) Nome da série sem conter prefixo e sufixo

    serie = nomeSerie.split("_") # dividindo a string em array com base no símbolo '_'
    serie = serie[1] #pegando apenas a parte final
    serie = serie.replace("PA12","") # substituindo o sufixo PA12 por nada - Esse método replace era poderia ser utilizado para resolver tudo. Escolhi usar dois diferentes apenas para 'testar' as diferentes funções
    return serie
    


def buscaDados():

    # Função para a inserção dos dados do arquivo do IPEA no banco de dados
    # Busca pela API os dados das séries definidas, interpreta, organiza e insere os dados no banco de dados
    # 
    # Depende de    - Tabela criada pela função criaTabela()
    # Parâmetros    - Nenhum
    # Retorno       - Nenhum

    quantidade_inserida = 0

    #analisei as séries disponibilizadas pelo IPEA buscando aquelas que possivelmente terão alguma relação com os dados com os quais estou lidando
    #nesse momento, é ainda impossível saber com exatidão se esses dados serão "decisivos" na minha análise de dados. só a própria análise responderá essa questão

    #definindo as séries de dados a serem buscados
    series = []
    series.append("CONFAZ12_IRPA12")    # Imposto sobre a renda (IR) - Pará (PA)
    series.append("CONFAZ12_ICMSPA12")  # Imposto sobre a circulação de mercadorias (ICMS) - Pará (PA)  
    series.append("CONFAZ12_IEPA12")    # Imposto sobre a exportação (IE) - Pará (PA)  
    series.append("CONFAZ12_IIPA12")    # Imposto sobre a importação (II) - Pará (PA)
    series.append("CONFAZ12_IOFPA12")   # Imposto sobre operações financeiras (IOF) - Pará (PA)
    series.append("CONFAZ12_IPIPA12")   # Imposto sobre produtos industrializados (IPI) - Pará (PA) 
    series.append("CONFAZ12_IPVAPA12")  # Imposto sobre a propriedade de veículos automotores (IPVA) - Pará (PA)  
    series.append("CONFAZ12_ITRPA12")   # Imposto sobre a propriedade territorial rural (ITR) - Pará (PA)
    series.append("CONFAZ12_ORADPA12")  # Outras receitas administradas - Pará (PA)
    

    #buscando os dados
    for serie in series: #percorrendo as séries definidas acima
        dadosDestaSerie = ipeadatapy.timeseries(serie) #Buscando os dados dessa série
        
        nomeColuna = retornaNomeColuna(serie)
        
        for linha in dadosDestaSerie.itertuples(): #percorrendo as linhas retornadas
            
            linha = list(linha)
            
            data = "{}-{}-{}".format(linha[5],linha[4],linha[3]) #tratando a data


            queryInsertUpdate = """

                INSERT INTO
                    public.ipea
                    (
                        id,
                        data,
                        dia,
                        mes,
                        ano,
                        """+nomeColuna+"""
                    )
                    VALUES
                    (
                        nextval('auto_increment'::regclass),
                        '"""+data+"""',
                        '"""+str(linha[3])+"""',
                        '"""+str(linha[4])+"""',
                        '"""+str(linha[5])+"""',
                        '"""+str(linha[6])+"""'
                    )
                ON CONFLICT (data)
                DO UPDATE SET
                    """+nomeColuna+""" = '"""+str(linha[6])+"""'
                WHERE
                ipea.data = '"""+data+"""';



            """
            
            if not math.isnan(linha[6]): #desprezando linhas sem informação útil
                conexao.consulta(queryInsertUpdate, False)
                quantidade_inserida = quantidade_inserida+1
    print(f"{quantidade_inserida} dados(s) inserido(s)")
    return 0