from flask import Flask, jsonify, request
from conexao import conecta_db
from cadastro_livro import inserir, alterar, consultar, consultar_por_id, deletar, inserir
from cadastro_autor import listar_autores, inserir_autor_db, alterar_autor_db, deletar_autor_db, consultar_autor_por_id_db

app = Flask(__name__)

@app.route('/livros/<int:id>', methods=['GET'])
def get_livro(id):
    print('ID Livro' + str(id))
    return jsonify("{ 'nome':  'Livro Python 21 dias' }")

@app.route('/livros', methods=['POST'])
def inserir_livro():
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    inserir(conexao, nome)
    return jsonify(data)

@app.route("/livros/<int:id>", methods=["PUT"])
def alterar_livro(id):
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    alterar(conexao, int(id), nome)
    return jsonify(data)

@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    conexao = conecta_db()
    deletar(conexao, id)
    return jsonify({"message": "Livro deletado com sucesso"})

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

@app.route("/autores", methods = ["POST"])
def inserir_autor():
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    inserir_autor_db(conexao, nome)
    return jsonify(data)

@app.route("/autores/<int:id>", methods = ["PUT"])
def update_autor(id):
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    alterar_autor_db(conexao, int(id), nome)
    return jsonify(data)

@app.route("/autores/<int:id>", methods=["DELETE"])
def excluir_autor(id):
    conexao = conecta_db()
    deletar_autor_db(conexao, id)
    return jsonify({"message": "Autor deletado com sucesso!"})

@app.route('/autores/<int:id>', methods=['GET'])
def consultar_autor_por_id(id):
    conexao = conecta_db()
    autor = consultar_autor_por_id_db(conexao, id)
    return jsonify(autor)


if __name__ == '__main__':
    app.run(debug=True)