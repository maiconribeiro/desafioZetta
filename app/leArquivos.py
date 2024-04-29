##############################################################################
# Esse script foi criado para organizar a chamada dos métodos de cada base de dados utilizada
# 
# 
# Desenvolvido por Maicon Ribeiro
# Abril de 2024

from funcoes import ibge
from funcoes import mapbiomas
from funcoes import prodes
from funcoes import ipea

######################################################################
## IBGE
print("IBGE: ")
ibge.criaTabela()
ibge.buscaDados()

   


######################################################################
## MAPBIOMAS
print("MAPBIOMAS: ")
mapbiomas.criaTabela()
mapbiomas.buscaDados()



######################################################################
## PRODES
print("PRODES: ")
prodes.criaTabela()
prodes.buscaDados()


######################################################################
## IPEA
ipea.criaTabela()
ipea.buscaDados()