import conexao

def dadosSocioEconomicos():
    queryBusca = """
        SELECT
            ibge.cidade,
            ibge.pib,
            ibge.pib_per_capita,
            ipea.ano,
            ipea.ir,
            ipea.icms,
            ipea.ie,
            ipea.ii,
            ipea.iof,
            ipea.ipi,
            ipea.ipva,
            ipea.itr,
            ipea.orad
        FROM
            public.ibge
        INNER JOIN
            (
                SELECT
                    ipea.ano,
                    AVG(ipea.ir) as ir,
                    AVG(ipea.icms) as icms,
                    AVG(ipea.ie) as ie,
                    AVG(ipea.ii) as ii,
                    AVG(ipea.iof) as iof,
                    AVG(ipea.ipi) as ipi,
                    AVG(ipea.ipva) as ipva,
                    AVG(ipea.itr) as itr,
                    AVG(ipea.orad) as orad
                FROM
                    public.ipea
                GROUP BY
                    ipea.ano
                ORDER BY
                    ipea.ano
            ) as ipea
            ON ipea.ano = EXTRACT(YEAR FROM ibge.ano)
        ORDER BY
            ibge.cidade, ibge.ano
    """
    dados = conexao.consulta(queryBusca)
    return dados



def dadosPibIr(dadosSocio):
    arrayPib = []
    arrayIR = []
    for linha in dadosSocio:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[4]))
        arrayIR.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayIR)

    return arrayRetorno
    
def dadosPibIcms(dadosSocio):
    arrayPib = []
    arrayIcms = []
    for linha in dadosSocio:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[5]))
        arrayIcms.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayIcms)

    return arrayRetorno


def dadosPibIE(dadosSocio):
    arrayPib = []
    arrayIE = []
    for linha in dadosSocio:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[6]))
        arrayIE.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayIE)

    return arrayRetorno


def dadosPibII(dadosSocio):
    arrayPib = []
    arrayII = []
    for linha in dadosSocio:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[7]))
        arrayII.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayII)

    return arrayRetorno


def dadosPibIof(dadosSocio):
    arrayPib = []
    arrayIof = []
    for linha in dadosSocio:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[8]))
        arrayIof.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayIof)

    return arrayRetorno

def dadosPibIpi(dadosSocio):
    arrayPib = []
    arrayIpi = []
    for linha in dadosSocio:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[9]))
        arrayIpi.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayIpi)

    return arrayRetorno

def dadosPibIpva(dadosSocio):
    arrayPib = []
    arrayIpva = []
    for linha in dadosSocio:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[10]))
        arrayIpva.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayIpva)

    return arrayRetorno


def dadosPibItr(dadosSocio):
    arrayPib = []
    arrayItr = []
    for linha in dadosSocio:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[11]))
        arrayItr.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayItr)

    return arrayRetorno


def dadosPibOrad(dadosSocio):
    arrayPib = []
    arrayOrad = []
    for linha in dadosSocio:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[12]))
        arrayOrad.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayOrad)

    return arrayRetorno



def dadosDesmatamento():
    queryBusca = """
        SELECT
            EXTRACT(YEAR FROM mapbiomas.ano) as ano,
            AVG(mapbiomas.area_desmatada) as area_desmatada,
            ibge.pib,
            ibge.pib_per_capita
        FROM
            mapbiomas
        INNER JOIN
            (
                SELECT
                    EXTRACT(YEAR FROM ibge.ano) as ano,
                    AVG(pib) as pib,
                    AVG(pib_per_capita) as pib_per_capita
                FROM
                    public.ibge
                GROUP BY
                    EXTRACT(YEAR FROM ibge.ano)
            ) as ibge
            ON ibge.ano = EXTRACT(YEAR FROM mapbiomas.ano)
        GROUP BY
            EXTRACT(YEAR FROM mapbiomas.ano), ibge.pib, ibge.pib_per_capita
        ORDER BY
            EXTRACT(YEAR FROM mapbiomas.ano)

        """
    dados = conexao.consulta(queryBusca)
    return dados

def dadosPibDesmatamento(dadosDesmatamento):
    arrayPib = []
    arrayDesmatamento = []
    for linha in dadosDesmatamento:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[2]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayDesmatamento.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayDesmatamento)
    return arrayRetorno



def dadosPibPercapitaDesmatamento(dadosDesmatamento):
    arrayPib = []
    arrayDesmatamento = []
    for linha in dadosDesmatamento:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[3]))
        arrayPib.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayDesmatamento.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayPib)
    arrayRetorno.append(arrayDesmatamento)
    return arrayRetorno


def dadosDesmatamentoAnual(dadosDesmatamento):
    arrayAnos = []
    arrayDesmatamento = []
    for linha in dadosDesmatamento:
        linha = list(linha)
        arrayTemp = []
        arrayTemp.append(float(linha[0]))
        arrayAnos.append(arrayTemp)

        arrayTemp = []
        arrayTemp.append(float(linha[1]))
        arrayDesmatamento.append(arrayTemp)
    
    arrayRetorno = []
    arrayRetorno.append(arrayAnos)
    arrayRetorno.append(arrayDesmatamento)
    return arrayRetorno
