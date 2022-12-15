import psycopg2

print("Testando...")

try:
    conn = psycopg2.connect(
    host = "localhost",
    port ="5450",
    database = "postgres", 
    user="denega", password = "123456")
    print('CONECTADO')

except Exception:
    print('VOCE ESTA SEM CONEXAO!')


if conn is not None:
    
    print('Sua Conexao está estabilizada!')

    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE pessoa (id serial, nome VARCHAR(15) NOT NULL, idade int NOT NULL, altura float NOT NULL, PRIMARY KEY(id));')
    print('Sua tabela PESSOA foi criada!')

    cursor.execute('CREATE TABLE usuarios  (id serial, nome VARCHAR(15) NOT NULL, nickname VARCHAR(10) NOT NULL, senha VARCHAR(10)NOT NULL, PRIMARY KEY(nickname) );')
    print('Sua tabela USUARIO foi criada!')

    conn.commit()
    cursor.close()
    conn.close()