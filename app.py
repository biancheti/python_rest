from flask import Flask, jsonify, request
from conexao import conecta_db

from cadastro_autor import listar_autores, inserir_autor_db, alterar_autor_db, deletar_autor_db, consultar_autor_por_id_db
from cadastro_editora import listar_editoras, inserir_editora_db, alterar_editora_db, deletar_editora_db, consultar_editora_por_id_db
from cadastro_livro import (alterar, consultar, consultar_por_id, deletar, inserir)
from cadastro_usuario import (listar_usuarios, inserir_usuario_db, alterar_usuario_db, deletar_usuario_db, consultar_usuario_por_id, verificar_login)

app = Flask(__name__)

@app.route("/livros/<int:id>", methods=["GET"])
def get_livro(id):
   conexao = conecta_db()
   livros = consultar_por_id(conexao,id)
   return jsonify(livros)

@app.route("/livros", methods=["POST"])
def inserir_livro():
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    inserir(conexao,nome)
    return jsonify(data)

@app.route("/livros/<int:id>", methods=["PUT"])
def alterar_livro(id):
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    alterar(conexao,int(id),nome)
    return jsonify(data)


@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    conexao = conecta_db()
    deletar(conexao,id)
    return jsonify({"message": "Livro deletado com sucesso" })


@app.route("/livros", methods=["GET"])
def listar_todos():
    conexao = conecta_db()
    livros = consultar(conexao)
    return jsonify(livros)

@app.route("/autores", methods=["GET"])
def listar_todos_autores():
    conexao = conecta_db()
    autores = listar_autores(conexao)
    return jsonify(autores)

@app.route("/autores", methods=["POST"])
def inserir_autor():
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    inserir_autor_db(conexao, nome)
    print(nome)
    return jsonify(data)

@app.route("/autores/<int:id>", methods=["PUT"])
def alterar_autor(id):
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    alterar_autor_db(conexao, int(id), nome)
    return jsonify(data)

@app.route("/autores/<int:id>", methods=["DELETE"])
def deletar_autor(id):
    conexao = conecta_db() 
    deletar_autor_db(conexao, id)
    return jsonify({"message": "autor deletado com sucesso" })

@app.route("/autores/<int:id>", methods=["GET"])
def consultar_autor(id):
   conexao = conecta_db()
   autor = consultar_autor_por_id_db(conexao,id)
   return jsonify(autor)

@app.route("/editoras", methods=["GET"])
def listar_todos_editoras():
    conexao = conecta_db()
    editoras = listar_editoras(conexao)
    return jsonify(editoras)

@app.route("/editoras", methods=["POST"])
def inserir_editora():
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    inserir_editora_db(conexao, nome)
    print(nome)
    return jsonify(data)

@app.route("/editoras/<int:id>", methods=["PUT"])
def alterar_editora(id):
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    alterar_editora_db(conexao, int(id), nome)
    return jsonify(data)

@app.route("/editoras/<int:id>", methods=["DELETE"])
def deletar_editora(id):
    conexao = conecta_db() 
    deletar_editora_db(conexao, id)
    return jsonify({"message": "Editora deletada com sucesso!" })

@app.route("/editoras/<int:id>", methods=["GET"])
def consultar_editora(id):
   conexao = conecta_db()
   autor = consultar_editora_por_id_db(conexao,id)
   return jsonify(autor)

@app.route("/usuarios", methods=["GET"])
def listar_todos_usuarios():
    conexao = conecta_db()
    usuarios = listar_usuarios(conexao)
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    inserir_usuario_db(conexao, login, senha)
    return jsonify(data)

@app.route("/usuarios/<int:id>", methods=["PUT"])
def alterar_usuario(id):
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    alterar_usuario_db(conexao, int(id), nome)
    return jsonify(data)

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    conexao = conecta_db() 
    deletar_usuario_db(conexao, id)
    return jsonify({"message": "autor deletado com sucesso" })

@app.route("/usuarios/<int:id>", methods=["GET"])
def consultar_usuario(id):
   conexao = conecta_db()
   usuario = consultar_usuario_por_id(conexao, id)
   return jsonify(usuario)


@app.route("/autenticar", methods=["POST"])
def autenticar_login():
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    resultado = verificar_login(conexao, login, senha)
    print(login, senha)
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)