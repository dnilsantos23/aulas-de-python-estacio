#
import sqlite3 as conector

 # Abertura de conexão
conexao = conector.connect("URL SQLite")

 # Aquisição de um cursor
cursor = conexao.cursor()

 # Execução comandos: SELECT..CREATE...INSERT..UPDATE..DELETE
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)")
cursor.execute("INSERT INTO clientes (nome, idade) VALUES ('João', 30)")
cursor.fetchall()

 # Efetivação do comando
conexao.commit()
  
 # Fechamento das conexões
cursor.close()
conexao.close()