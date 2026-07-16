import sqlite3                   # conexão com sqlite
from sqlite3 import Connection                       

class SqliteConnectionHandle:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"     # string de conexão com o banco que existe no diretório raiz
        self.__conn = None

    def connect(self) -> Connection:      # cria a conexão, a partir da string de conexão
        conn = sqlite3.connect(
            self.__connection_string,
            check_same_thread=False
            ) 
        self.__conn = conn                # retorna a conexão
        return conn

    def get_connection(self) -> Connection:
        return self.__conn

"""
'check_same_thread=False' permite que a mesma conexão SQLite 
seja utilizada por múltiplas threads.
"""    

