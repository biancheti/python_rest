from flask import Flask, jsonify, request


from cadastro_autor import (alterar_autor_db, consultar_autor_por_id_db,
                            deletar_autor_db, inserir_autor_db, listar_autores)
from cadastro_livro import (alterar, consultar, consultar_por_id, deletar,
                            inserir)
from cadastro_usuario import (alterar_usuario_db, consultar_usuario_por_id_db,
                              deletar_usuario_db, inserir_usuario_db,
                              listar_usuarios, verificar_login)


from cadastro_editora import inserir_editora_db

from conexao import conecta_db

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'designcursos' #Use uma chave segura em produção
jwt = JWTManager(app)


@app.route("/livros/<int:id>", methods=["GET"])
@jwt_required()
def get_livro(id):
   conexao = conecta_db()
   livros = consultar_por_id(conexao,id)
   return jsonify(livros)

@app.route("/livros", methods=["POST"])
@jwt_required()
def inserir_livro():
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    id_editora=data["id_editora"]
    id_autor=data["id_autor"]
    inserir(conexao,nome,id_editora,id_autor)
    return jsonify(data)

@app.route("/livros/<int:id>", methods=["PUT"])
@jwt_required()
def alterar_livro(id):
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    alterar(conexao,int(id),nome)
    return jsonify(data)


@app.route("/livros/<int:id>", methods=["DELETE"])
@jwt_required()
def excluir_livro(id):
    conexao = conecta_db()
    deletar(conexao,id)
    return jsonify({"message": "Livro deletado com sucesso!" })


@app.route("/livros", methods=["GET"])
@jwt_required()
def listar_todos():
    conexao = conecta_db()
    livros = consultar(conexao)
    return jsonify(livros)

@app.route("/autores", methods=["GET"])
@jwt_required()
def listar_todos_autores():
    conexao = conecta_db()
    autores = listar_autores(conexao)
    return jsonify(autores)


@app.route("/autores", methods=["POST"])
@jwt_required()
def inserir_autor():
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    inserir_autor_db(conexao,nome)
    return jsonify(data)

@app.route("/autores/<int:id>", methods=["PUT"])
@jwt_required()
def update_autor(id):
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    alterar_autor_db(conexao,int(id),nome)
    return jsonify(data)


@app.route("/autores/<int:id>", methods=["DELETE"])
@jwt_required()
def excluir_autor(id):
    conexao = conecta_db()
    deletar_autor_db(conexao,id)
    return jsonify({"message": "Autor deletado com sucesso!" })


@app.route("/autores/<int:id>", methods=["GET"])
@jwt_required()
def consultar_autor_por_id(id):
    conexao = conecta_db()
    autor = consultar_autor_por_id_db(conexao,id)
    return jsonify(autor)


@app.route("/usuarios", methods=["GET"])
@jwt_required()
def listar_todos_usuarios():
    conexao = conecta_db()
    usuarios = listar_usuarios(conexao)
    return jsonify(usuarios)


@app.route("/usuarios", methods=["POST"])
@jwt_required()
def inserir_usuario():
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    inserir_usuario_db(conexao,login,senha)
    return jsonify(data)

@app.route("/usuarios/<int:id>", methods=["PUT"])
@jwt_required()
def update_usuario(id):
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    alterar_usuario_db(conexao,int(id),login,senha)
    return jsonify(data)


@app.route("/usuarios/<int:id>", methods=["DELETE"])
@jwt_required()
def excluir_usuario(id):
    conexao = conecta_db()
    deletar_usuario_db(conexao,id)
    return jsonify({"message": "Usuário deletado com sucesso!" })


@app.route("/usuarios/<int:id>", methods=["GET"])
@jwt_required()
def consultar_usuario_por_id(id):
    conexao = conecta_db()
    autor = consultar_usuario_por_id_db(conexao,id)
    return jsonify(autor)


@app.route("/autenticar", methods=["POST"])
@jwt_required()
def autenticar():
    print("Teste autenticar")
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    print(login)
    print(senha)
    resultado = verificar_login(conexao,login,senha)
    return jsonify({"message": resultado })


@app.route("/editoras", methods=["POST"])
@jwt_required()
def inserir_editora():
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    inserir_editora_db(conexao,nome)
    return jsonify(data)

@app.route('/login', methods = ['POST'])
def login():

    if not request.is_json:
        return jsonify({"msg": "Json inválido!"}), 400
    
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    #Verificar se os dados do json estão no formato válido
    if not username or not password: 
        return jsonify({"msg": "Usuário e senha incompleto!"}), 400
    
    conexao = conecta_db()
    validar_login = verificar_login(conexao, username, password)
    
    #Verificar se o usuário existe e senha está correta
    if validar_login:
        access_token = create_access_token(identity = username)
        return jsonify(access_token = access_token), 200
    else: 
        return jsonify({"msg": "Usuario e senhas inválidos!"}), 401

@app.route('/url-protegida', methods = ['GET'])
@jwt_required()
def url_protegida():
    current_user = get_jwt_identity()
    return jsonify({"msg": "Protegida " + current_user}), 200

if __name__ == "__main__":
    app.run(debug=True)