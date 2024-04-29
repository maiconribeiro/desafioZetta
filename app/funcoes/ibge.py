####################################################
# Desenvolvido por maicon ribeiro
# inicio 26/04/2024
# fim 27/04/2024
#
# Esse arquivo contém as funções necessárias para tratar os dados disponibilizados pelo IBGE
# Esses dados são disponibilizados no seguinte endereço: https://ftp.ibge.gov.br/Pib_Municipios/2019/base/base_de_dados_2010_2019_xls.zip
#

import conexao
import math
import pandas as pd


def criaTabela():
    # Função para a criação da tabela dos dados do IBGE
    # Os campos dessa tabela foram definidos a partir de uma análise dos dados disponibilizados pelo ibge
    # NESSE caso, escolhi tratar especificamente dos dados do PIB dos municípios do pará
    # Parâmetros    - Nenhum
    # Retorno       - Nenhum
    cria_tabela = """
        CREATE TABLE IF NOT EXISTS public.ibge (
            id int4 NOT NULL,
            ano date NOT NULL,
            codigo_regiao int4 NOT NULL,
            nome_regiao varchar(50) NOT NULL,
            sigla_estado varchar(2) NOT NULL,
            regiao_metropolitana varchar(200) NOT NULL,
            codigo_mesorregiao int4 NOT NULL,
            mesoregiao varchar(50) NOT NULL,
            codigo_microrregiao int4 NOT NULL,
            microrregiao varchar(200) NOT NULL,
            codigo_regiao_imediata int4 NOT NULL,
            regiao_imediata varchar(200) NOT NULL,
            codigo_municipio_polo int4 NOT NULL,
            municipio_polo varchar(200) NOT NULL,
            codigo_municipio_intermediario int4 NOT NULL,
            municipio_intermediario varchar(200) NOT NULL,
            codigo_concentracao_urbana int4 NOT NULL,
            concentracao_urbana varchar(200) NOT NULL,
            tipo_concentracao_urbana varchar(200) NOT NULL,
            codigo_arranjo_populacional int4 NOT NULL,
            arranjo_populacional varchar(200) NOT NULL,
            hierarquia_urbana varchar(200) NOT NULL,
            categoria_hierarquia_urbana varchar(200) NOT NULL,
            codigo_regiao_rural int4 NOT NULL,
            regiao_rural varchar(200) NOT NULL,
            tipo_regiao_rural varchar(200) NOT NULL,
            amazonia_legal public.mood NOT NULL,
            semiarido public.mood NOT NULL,
            valor_agropecuaria numeric NOT NULL,
            valor_industria numeric NOT NULL,
            valor_impostos numeric NOT NULL,
            pib numeric NOT NULL,
            pib_per_capita numeric NOT NULL,
            atividades_rentaveis_1 varchar(200) NOT NULL,
            atividades_rentaveis_2 varchar(200) NOT NULL,
            atividades_rentaveis_3 varchar(200) NOT NULL,
            CONSTRAINT ibge_pk PRIMARY KEY (id)
        );"""
    conexao.consulta(cria_tabela,False)
    limpaTabela = "TRUNCATE TABLE public.ibge"
    conexao.consulta(limpaTabela,False)
    print("Tabela criada com sucesso")


def buscaDados():
    # Função para a inserção dos dados do arquivo do IBGE no banco de dados
    # Abre, interpreta, organiza e insere os dados do arquivo xls
    # 
    # Depende de    - Tabela criada pela função criaTabela()
    # Parâmetros    - Nenhum
    # Retorno       - Nenhum


    arquivo_ibge = "Dados/ibge/pib_municipios.xls"
    # carregando especificamente a aba com as informações do bioma por estado
    dadosIbge = pd.read_excel(arquivo_ibge)
    #filtrando apenas o estado do pará
    dadosIbge = ((dadosIbge.loc[dadosIbge['Nome da Unidade da Federação']=='Pará']))

    quantidade_inserida = 0 #contador de linhas inseridas
     
    for row in dadosIbge.itertuples(index=False):
        essaLinha = list(row)
        dataEvento = "{}-01-01".format(essaLinha[0])

        essaLinha[7] = essaLinha[7].replace("'", "") #removendo caracteres especiais no nome da cidade


        if not type(essaLinha[8]) is str:
            if( math.isnan(essaLinha[8])):
                essaLinha[8] = '0'
        if( math.isnan(essaLinha[19])):
            essaLinha[19] = '0'
        if( math.isnan(essaLinha[22])):
            essaLinha[22] = '0'
        else:
            essaLinha[22] = int(essaLinha[22])
        if not type(essaLinha[23]) is str:
            if(math.isnan(essaLinha[23])):
                essaLinha[23] = '0'
            else:
                essaLinha[23] = int(essaLinha[23])
        

        if(essaLinha[29] == 'Não'):
            essaLinha[29] = 'Nao' #removendo acentuação
        if(essaLinha[30] == 'Não'):
            essaLinha[30] = 'Nao' #removendo acentuação
        if(essaLinha[31] == 'Não'):
            essaLinha[31] = 'Nao' #removendo acentuação

        insercao = """
            INSERT INTO public.ibge
            (
                id,
                ano,
                codigo_regiao,
                nome_regiao,
                sigla_estado,
                estado,
                codigo_cidade,
                cidade,
                regiao_metropolitana,
                codigo_mesorregiao,
                mesoregiao,
                codigo_microrregiao,
                microrregiao,
                codigo_regiao_imediata,
                regiao_imediata,
                codigo_municipio_polo,
                municipio_polo,
                codigo_municipio_intermediario,
                municipio_intermediario,
                codigo_concentracao_urbana,
                concentracao_urbana,
                tipo_concentracao_urbana,
                codigo_arranjo_populacional,
                arranjo_populacional,
                hierarquia_urbana,
                categoria_hierarquia_urbana,
                codigo_regiao_rural,
                regiao_rural,
                tipo_regiao_rural,
                amazonia_legal,
                semiarido,
                valor_agropecuaria,
                valor_industria,
                valor_servicos,
                valor_administracao,
                valor_bruto_total,
                valor_impostos,
                pib,
                pib_per_capita,
                atividades_rentaveis_1,
                atividades_rentaveis_2,
                atividades_rentaveis_3)
            VALUES
                (
                    nextval('auto_increment'::regclass),
                    '"""+dataEvento+"""',
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
                    '0',
                    '"""+str(essaLinha[15])+"""',
                    '"""+str(essaLinha[16])+"""',
                    '"""+str(essaLinha[17])+"""',
                    '"""+str(int(essaLinha[19]))+"""',
                    '"""+str(essaLinha[20])+"""',
                    '"""+str(essaLinha[21])+"""',
                    '"""+str(essaLinha[22])+"""',
                    '"""+str(essaLinha[23])+"""',
                    '"""+str(essaLinha[24])+"""',
                    '"""+str(essaLinha[25])+"""',
                    '"""+str(essaLinha[26])+"""',
                    '"""+str(essaLinha[27])+"""',
                    '"""+str(essaLinha[28])+"""',
                    '"""+str(essaLinha[29])+"""',
                    '"""+str(essaLinha[30])+"""',
                    '"""+str(essaLinha[32])+"""',
                    '"""+str(essaLinha[33])+"""',
                    '"""+str(essaLinha[34])+"""',
                    '"""+str(essaLinha[35])+"""',
                    '"""+str(essaLinha[36])+"""',
                    '"""+str(essaLinha[37])+"""',
                    '"""+str(essaLinha[38])+"""',
                    '"""+str(essaLinha[39])+"""',
                    '"""+str(essaLinha[40])+"""',
                    '"""+str(essaLinha[41])+"""',
                    '"""+str(essaLinha[42])+"""');
        """
        conexao.consulta(insercao, False)
        quantidade_inserida = quantidade_inserida+1
    print(f"{quantidade_inserida} linha(s) inserida(s)")
        