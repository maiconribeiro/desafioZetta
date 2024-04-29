####################################################
# Desenvolvido por maicon ribeiro
# inicio 26/04/2024
# fim 27/04/2024
#
# Esse arquivo contém as funções necessárias para tratar os dados disponibilizados pelo mapBiomas
# Esses dados são disponibilizados no seguinte endereço: https://brasil.mapbiomas.org/colecoes-mapbiomas/


import conexao
import math
import pandas as pd


def criaTabela():
    # Função para a criação da tabela dos dados do mapbiomas
    # Os campos dessa tabela foram definidos a partir de uma análise dos dados disponibilizados pelo mapbiomas
    # O nome dos campos também foram trocados a partir de uma análise do significado de cada coluna do arquivo
    # Parâmetros    - Nenhum
    # Retorno       - Nenhum
    queryCriaTabela = """
        CREATE TABLE IF NOT EXISTS public.mapbiomas (
            id int4 NOT NULL,
            feature_id int4 NOT NULL,
            bioma varchar NULL,
            estado varchar(100) NOT NULL,
            id_vegetacao int4 NULL,
            vegetacao varchar(100) NOT NULL,
            legenda_uso_terra int4 NOT NULL,
            id_uso_terra_1 int4 NOT NULL,
            id_uso_terra_2 int4 NOT NULL,
            id_uso_terra_3 int4 NOT NULL,
            id_uso_terra_4 int4 NOT NULL,
            uso_terra_0 varchar(100) NOT NULL,
            uso_terra_1 varchar(100) NOT NULL,
            uso_terra_2 varchar(100) NOT NULL,
            uso_terra_3 varchar(100) NOT NULL,
            uso_terra_4 varchar(100) NOT NULL,
            cor varchar(100) NOT NULL,
            ano date NOT NULL,
            area_desmatada numeric NULL,
            CONSTRAINT mapbiomas_pk PRIMARY KEY (id)
        );
    """
    conexao.consulta(queryCriaTabela,False)
    limpaTabela = "TRUNCATE TABLE public.mapbiomas"
    conexao.consulta(limpaTabela,False)
    print("Tabela criada com sucesso")





def anoMapbiomas(coluna):
    # Esta função serve para calcular o ano de um determinado lançamento na tabela
    # Cada coluna (a partir da 17) corresponde a um ano - Estabeleci uma equação para calcular o ano com base na coluna 'atual'
    # 17 = 1986
    # 18 = 1987
    # 19 = 1988
    #  ...
    # 52 = 2021
    # 53 = 2022
    # não precisava de uma função só pra isso, mas foi uma forma de organizar o raciocínio
    return 1986+(coluna-17)

def buscaDados():
    # Função para a inserção dos dados do arquivo do mapBiomas no banco de dados
    # Abre, interpreta, organiza e insere os dados do arquivo xlsx
    # 
    # Depende de    - Tabela criada pela função criaTabela()
    # Parâmetros    - Nenhum
    # Retorno       - Nenhum


    quantidade_inserida = 0
    
    arquivo = "./Dados/mapbiomas/biomas.xlsx"
    # # carregando especificamente a aba com as informações do bioma por estado
    dadosxlsx = pd.read_excel(arquivo,sheet_name="STATE_BIOME") #como a planilha contém várias abas, filtrei somente a desejada
    # #filtrando apenas o estado do pará
    dadosxlsx = (dadosxlsx.loc[dadosxlsx['STATE']=='Pará'])

    for linhas in dadosxlsx.itertuples(index=False):
        essaLinha = list(linhas)
        #como a estrutura desse arquivo coloca os itens nas colunas (e não nas linhas como é costumeiro),
        #faremos uma inserção para cada ano dessa linha (entre 1986 e 2022)

        for i in range(17,54): #percorrendo os itens da coluna 17 até a última (ano a ano)
            
            ano = anoMapbiomas(i)#calculando o ano
            ano = "{}-01-01".format(ano)

            queryInsercao = """
                INSERT INTO public.mapbiomas
                    (
                        id,
                        feature_id,
                        bioma,
                        estado,
                        id_vegetacao,
                        vegetacao,
                        legenda_uso_terra,
                        id_uso_terra_1,
                        id_uso_terra_2,
                        id_uso_terra_3,
                        id_uso_terra_4,
                        uso_terra_0,
                        uso_terra_1,
                        uso_terra_2,
                        uso_terra_3,
                        uso_terra_4,
                        cor,
                        ano,
                        area_desmatada)
                    VALUES(
                        nextval('auto_increment'::regclass),
                        '"""+str(essaLinha[0])+"""',
                        '"""+str(essaLinha[1])+"""',
                        '"""+str(essaLinha[2])+"""',
                        '"""+str(essaLinha[4])+"""',
                        '"""+str(essaLinha[5])+"""',
                        '"""+str(essaLinha[6])+"""',
                        '"""+str(essaLinha[7])+"""',
                        '"""+str(essaLinha[8])+"""',
                        '"""+str(essaLinha[9])+"""',
                        '"""+str(essaLinha[10])+"""',
                        '"""+str(essaLinha[11])+"""',
                        '"""+str(essaLinha[12])+"""',
                        '"""+str(essaLinha[13])+"""',
                        '"""+str(essaLinha[14])+"""',
                        '"""+str(essaLinha[15])+"""',
                        '"""+str(essaLinha[16])+"""',
                        '"""+ano+"""',
                        '"""+str(essaLinha[i])+"""'
                    );
            """
            if not math.isnan(essaLinha[i]):
                #ignorando linhas onde não há valor de desmatamento
                conexao.consulta(queryInsercao, False)
                quantidade_inserida = quantidade_inserida+1
    
    print(f"{quantidade_inserida} linha(s) inserida(s)")
    return 0