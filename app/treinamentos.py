#####################################################################################
# Esse script foi criado para buscar e treinar redes neurais com os dados levantados
# 
# 
# Desenvolvido por Maicon Ribeiro
# Abril de 2024

from treinamento import funcoesDados
from treinamento import funcoesRna
from datetime import datetime
import time


pathRelativo = "app/resultados/" #local para salvar as imagens


print("######## Dados socioeconômicos")
dadosSocio = funcoesDados.dadosSocioEconomicos()
print("PIB X Imposto de renda")
pib_ir = funcoesDados.dadosPibIr(dadosSocio)

descricao = "pibXir_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.treinamento(pib_ir[0],pib_ir[1],'Produto Interno Bruto', 'Imposto de Renda',nomeArquivo,'PIB x IR', "barras")


print("PIB X ICMS")
pib_icms = funcoesDados.dadosPibIcms(dadosSocio)
descricao = "pibXicms_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.treinamento(pib_icms[0],pib_icms[1],'Produto Interno Bruto', 'ICMS',nomeArquivo,'PIB x ICMS', "barras")



print("PIB X Imposto sobre Exportação")
pib_ie = funcoesDados.dadosPibIE(dadosSocio)
descricao = "pibXie_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.treinamento(pib_ie[0],pib_ie[1],'Produto Interno Bruto', 'IE',nomeArquivo,'PIB x Imposto sobre Exportação', "barras")





print("PIB x Imposto sobre Importação")
pib_ii = funcoesDados.dadosPibII(dadosSocio)
descricao = "pibXii_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.treinamento(pib_ii[0],pib_ii[1],'Produto Interno Bruto', 'II',nomeArquivo,'PIB x Imposto sobre Importação', "barras")





print("PIB X Imposto sobre Operações Financeiras")
pib_iof = funcoesDados.dadosPibIof(dadosSocio)
descricao = "pibXiof_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.treinamento(pib_iof[0],pib_iof[1],'Produto Interno Bruto', 'IOF',nomeArquivo,'PIB x Imposto sobre Operações Financeiras', "barras")





print("PIB X Imposto sobre Produtos Industrializados")
pib_ipi = funcoesDados.dadosPibIpi(dadosSocio)
descricao = "pibXipi_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.treinamento(pib_ipi[0],pib_ipi[1],'Produto Interno Bruto', 'IPI',nomeArquivo,'PIB x Imposto sobre Produtos Industrializados', "barras")





print("PIB X IPVA")
pib_ipva = funcoesDados.dadosPibIpva(dadosSocio)
descricao = "pibXipva_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.treinamento(pib_ipva[0],pib_ipva[1],'Produto Interno Bruto', 'IPVA',nomeArquivo,'PIB x IPVA', "barras")





print("PIB X Imposto sobre a propriedade de território rural")
pib_itr = funcoesDados.dadosPibItr(dadosSocio)
descricao = "pibXitr_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.treinamento(pib_itr[0],pib_itr[1],'Produto Interno Bruto', 'ITR',nomeArquivo,'PIB x Imposto sobre a propriedade de território rural', "barras")





print("PIB X Outras Receitas Administradas")
pib_orad = funcoesDados.dadosPibOrad(dadosSocio)
descricao = "pibXorad_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.treinamento(pib_orad[0],pib_orad[1],'Produto Interno Bruto', 'ORA',nomeArquivo,'PIB x Outras Receitas Administradas', "barras")






print("######## Dados de desmatamento")
dadosDesmatamento = funcoesDados.dadosDesmatamento()
print("PIB X Desmatamento")
pib_desmatamento = funcoesDados.dadosPibDesmatamento(dadosDesmatamento)
descricao = "pibXdesmatamento_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.treinamento(pib_desmatamento[0],pib_desmatamento[1],'Produto Interno Bruto', 'Desmatamento', nomeArquivo,'PIB x Área desmatada', "barras")
funcoesRna.graficoComPrevisao(pib_desmatamento[0],pib_desmatamento[1],'PIB', 'Desmatamento', 'Tempo decorrido', nomeArquivo, 'PIB X Área desmatada', 'PIB - Desmatamento', 'Tempo decorrido')

print("PIB per capita X Desmatamento")
pibPercapita_desmatamento = funcoesDados.dadosPibPercapitaDesmatamento(dadosDesmatamento)
descricao = "pibPercapitaXdesmatamento_"
horaAtual = datetime.now().strftime("%H:%M:%S")
nomeArquivo = "{}{}{}.png".format(pathRelativo,descricao,horaAtual)
funcoesRna.graficoComPrevisao(pibPercapita_desmatamento[0],pibPercapita_desmatamento[1],'PIB Per capita', 'Desmatamento', 'Tempo decorrido', nomeArquivo, 'PIB Per Capita X Área desmatada', 'PIB Per Capita - Desmatamento', 'Tempo decorrido')
