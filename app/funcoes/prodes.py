####################################################
# Desenvolvido por maicon ribeiro
# inicio 27/04/2024
# fim 27/04/2024
#
# Esse arquivo contém as funções necessárias para tratar os dados disponibilizados pelo prodes
# Esses dados são disponibilizados no seguinte endereço: https://terrabrasilis.dpi.inpe.br/downloads/
# Aqui, lidamos especificamente com dados em formato CSV. O site supracitado nos entrega em um formato diferente.
# Para fins de facilitar o processo, optei por transformá-los em CSV pelo seguinte serviço: https://stable.demo.geonode.org/

#   Assis, L. F. F. G.; Ferreira, K. R.; Vinhas, L.; Maurano, L.; Almeida, C.; Carvalho, A.; Rodrigues, J.; Maciel, A.; Camargo, C.
#   TerraBrasilis: A Spatial Data Analytics Infrastructure for Large-Scale Thematic Mapping. ISPRS International Journal of Geo-Information. 8, 513, 2019. DOI: 10.3390/ijgi8110513  

#   INSTITUTO NACIONAL DE PESQUISAS ESPACIAIS. COORDENAÇÃO GERAL DE OBSERVAÇÃO DA TERRA. PROGRAMA DE MONITORAMENTO DA AMAZÔNIA E DEMAIS BIOMAS.
#   Desmatamento – Amazônia Legal – Disponível em: https://terrabrasilis.dpi.inpe.br/downloads/. Acesso em: 27 abril. 2024.

import conexao
import math
import pandas as pd


def criaTabela():
    # Função para a criação da tabela dos dados do prodes
    # Os campos dessa tabela foram definidos a partir de uma análise dos dados disponibilizados pelo prodes
    # 
    # 
    # Parâmetros    - Nenhum
    # Retorno       - Nenhum
    queryCriaTabela = """
        
        CREATE TABLE IF NOT EXISTS public.prodes (
            id int4 DEFAULT nextval('seqprodes'::regclass) NOT NULL,
            coordenadas polygon NULL,
            fid int4 NOT NULL,
            estado varchar(50) NOT NULL,
            path_row int4 NOT NULL,
            main_class varchar(100) NOT NULL,
            class_name varchar(5) NOT NULL,
            def_cloud int4 NOT NULL,
            julian_day int4 NOT NULL,
            image_date date NOT NULL,
            "year" date NOT NULL,
            area numeric NOT NULL,
            scene_id int4 NOT NULL,
            "source" varchar NOT NULL,
            satelite varchar NOT NULL,
            sensor varchar NOT NULL,
            "uuid" varchar NOT NULL,
            CONSTRAINT prodes_pk PRIMARY KEY (id)

        );
    """
    conexao.consulta(queryCriaTabela,False)
    limpaTabela = "TRUNCATE TABLE public.prodes"
    conexao.consulta(limpaTabela,False)
    print("Tabela criada com sucesso")


def buscaDados():
    # Função para a inserção dos dados do arquivo do prodes no banco de dados
    # Abre, interpreta, organiza e insere os dados do arquivo csv
    # 
    # Depende de    - Tabela criada pela função criaTabela()
    # Parâmetros    - Nenhum
    # Retorno       - Nenhum
    quantidade_inserida = 0
    
    arquivo = "./Dados/prodes/yearly_deforestation.csv" #esse arquivo foi baixado em formato de banco de dados e convertido para CSV
    
    
    dadosCsv = pd.read_csv(arquivo, nrows=100000) #limitando a quantidade de leitura do arquivo em função de limitação de hardware disponível

    # #filtrando apenas o estado do pará
    dadosCsv = dadosCsv[dadosCsv['state']=='PA']
    

    for linha in dadosCsv.itertuples(index=False):

        linha = list(linha)
        
        if linha[3] == "PA":
            linha[3] = "Pará"

        if not type(linha[13]) is str:
            if(math.isnan(linha[13])):
                linha[13] = ""
        
        if not type(linha[14]) is str:
            if(math.isnan(linha[14])):
                linha[14] = ""
        
        if not type(linha[15]) is str:
            if(math.isnan(linha[15])):
                linha[15] = ""
        
        if(math.isnan(linha[7])):
            linha[7] = "0"
        linha[7] = int(linha[7])
        
        
        



        insercao = """
                INSERT INTO public.prodes
                (
                    id,
                    coordenadas,
                    fid,
                    estado,
                    path_row,
                    main_class,
                    class_name,
                    def_cloud,
                    julian_day,
                    image_date,
                    year,
                    area,
                    scene_id,
                    source,
                    satelite,
                    sensor,
                    uuid
                )
                VALUES
                    (
                        nextval('auto_increment'::regclass),
                        '"""+str(linha[1])+"""',
                        '"""+str(linha[2])+"""',
                        '"""+str(linha[3])+"""',
                        '"""+str(linha[4])+"""',
                        '"""+str(linha[5])+"""',
                        '"""+str(linha[6])+"""',
                        '"""+str(linha[7])+"""',
                        '"""+str(linha[8])+"""',
                        '"""+str(linha[9])+"""',
                        '"""+str(linha[10])+"""',
                        '"""+str(linha[11])+"""',
                        '"""+str(linha[12])+"""',
                        '"""+str(linha[13])+"""',
                        '"""+str(linha[14])+"""',
                        '"""+str(linha[15])+"""',
                        '"""+str(linha[16])+"""'

                    );
            """
        
        conexao.consulta(insercao, False)

        quantidade_inserida = quantidade_inserida+1
    print(f"{quantidade_inserida} linha(s) inserida(s)")

    return 0