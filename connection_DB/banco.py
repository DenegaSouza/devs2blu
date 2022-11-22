import psycopg2


try: 
    conn = psycopg2.connect(host = "localhost", port = "5450", database = "postgres", user="denega", password = "123456")
    print("CONECTADO COM SUCESSO")
except:
    print("não deu")
    
if conn is not None:
    print("CONEXÃO ESTÁVEL")

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_pessoa(
        id INTEGER PRIMARY KEY,
        nome VARCHAR(20),
        sobrenome VARCHAR(20)
        )
        """)
    conn.commit()
    cursor.close()
    conn.close()