from conexao import conecta_db

def listar_editoras(conexao):
    editoras = []
    cursor = conexao.cursor()
    cursor.execute("select id,nome from editora")
    registros = cursor.fetchall()
    for registro in registros:
        item = {
            "id": registro[0],
            "nome": registro[1]
        }
        editoras.append(item)
    return editoras

def inserir_editora_db(conexao, nome):
    cursor = conexao.cursor()
    cursor.execute("insert into editora (nome)  values ('" + nome + "')")
    conexao.commit()

def alterar_editora_db(conexao, id, nome):
    cursor = conexao.cursor()
    sql_update = "update editora set nome = %s where id = %s"
    dados = (nome, id)
    cursor.execute(sql_update, dados)
    conexao.commit()

def deletar_editora_db(conexao, id):
    cursor = conexao.cursor()
    sql_delete = "delete from editora where id  = %s"
    cursor.execute(sql_delete,[id])
    conexao.commit()

def consultar_editora_por_id_db(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("select id,nome from editora where id = %s", [id])
    registro = cursor.fetchone()
    item = {
        "id": registro[0],
        "nome": registro[1]
        }
    return item