##############################################################################
# Esse script tem intenção de conectar ao banco de dados
import psycopg2
from psycopg2 import sql

from sqlite3 import OperationalError
from sqlite3 import Error

def consulta(query, retornarLinhas = True):
    try:
        # Conectando: Docker
        connection = psycopg2.connect(
            host='db',
            database='desafioZetta',
            user='postgres',
            password='postgres',
            port='5432'
        )
        # # Conectando: Local
        # connection = psycopg2.connect(
        #     host='localhost',
        #     database='desafioZetta',
        #     user='postgres',
        #     password='postgres',
        #     port='5433'
        # )

        
        cursor = connection.cursor()
        #executando a query 
        cursor.execute(query)
        
        if(retornarLinhas == True):
            #capturando as linhas retornadas
            linhas = cursor.fetchall()
        else:
            linhas = 0
        

        # Commit (confirmar) as alterações (se houver) e fechar a conexão
        connection.commit()
        cursor.close()
        connection.close()
        return linhas

    except OperationalError as e:
        print(f"Erro de conexão: {e}")
    except Error as e:
        print(f"Erro ao executar consulta: {e}")
    # finally:
    #     cursor.close()
    #     connection.close()