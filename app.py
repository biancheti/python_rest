from flask import Flask, jsonify, request
from conexao import conecta_db
from cadastro_livro import inserir, alterar, consultar, consultar_por_id, deletar, inserir
from cadastro_autor import listar_autores

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

if __name__ == '__main__':
    app.run(debug=True)