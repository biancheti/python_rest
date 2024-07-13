import psycopg2


def conecta_db():
    con = psycopg2.connect(host="localhost",
                            database="biblioteca",
                            user="postgres",
                            password="postgres",
                            port=5432)
    return con