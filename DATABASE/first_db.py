# Este código é um exemplo de como criar um banco de dados SQLite, criar uma tabela e inserir dados nela.
import sqlite3 as conector

try:
    # Abertura de conexão
    conexao = conector.connect("./banco_de_dados.db")

    # Aquisição de um cursor
    cursor = conexao.cursor()

    # Execução comandos: SELECT..CREATE...INSERT..UPDATE..DELETE
    comando =  '''CREATE TABLE IF NOT EXISTS Pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf));'''
    # Efetivação do comando
    cursor.execute(comando)

    # Inserção de dados na tabela
    '''
    comando = INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES
                (12345678900, 'João', '1990-01-01', 1),
                (98765432100, 'Maria', '1985-05-15', 0),
                (45678912300, 'José', '1992-10-20', 1);
    '''
    comando = '''CREATE TABLE Marca (
                    id INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    sigla CHARACTER(2) NOT NULL,
                    PRIMARY KEY (id));'''

    comando = ''' CREATE TABLE Veiculo (
            placa CHARACTER(7) NOT NULL,
            ano INTEGER NOT NULL,
            cor TEXT NOT NULL,
            proprietario INTEGER NOT NULL,
            marca INTEGER NOT NULL,
            PRIMARY KEY (placa),
            FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
            FOREIGN KEY(marca) REFERENCES Marca(id));'''
    
    #ADICIONANDO DADOS A TABELA VEICULO
    comando = ''' ALTER TABLE Veiculo ADD motor REAL; '''
    
    comando = ''' DROP TABLE IF EXISTS Veiculo;'''
    
    comando = '''CREATE TABLE Veiculo (
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    motor REAL NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) REFERENCES Marca(id));'''
    
    # Efetivação do comando
    cursor.execute(comando)
    conexao.commit()
    print("Dados inseridos com sucesso!")
except conector.DatabaseError as erro:
    print("Erro de banco de dados: ", erro)      
finally:
    if conexao:
        cursor.close()
        conexao.close()

