from conexao import conecta_db

def consultar(conexao):
    livros = []
    cursor = conexao.cursor()
    cursor.execute("select id,nome from livro")
    registros = cursor.fetchall()
    print('-------------------------------')
    for registro in registros:
        item = {
        "id": registro[0],
        "nome": registro[1]
        }
        livros.append(item)
    return livros


def inserir(conexao, nome):
    cursor = conexao.cursor()

    sql_insert = "insert into livro (nome) values ('"+ nome +  "')"
    cursor.execute(sql_insert)
    conexao.commit()

def alterar(conexao, id, nome):
    cursor = conexao.cursor()

    sql_update = "update livro set nome = %s where id = %s"
    dados = (nome, id)
    cursor.execute(sql_update, dados)
    conexao.commit()

def consultar_por_id(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("select id,nome from livro where id = " +id)
    registro = cursor.fetchone()
    item = {
        "id": registro[0],
        "nome": registro[1]
        }
    return item

def deletar(conexao, id):
    cursor = conexao.cursor()

    sql_delete = "delete from livro where id =  %s"
    cursor.execute(sql_delete, [id])
    conexao.commit()