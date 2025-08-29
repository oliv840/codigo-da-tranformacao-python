from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# ==========================================================
# Projeto: Código da Transformação
# Estrutura Unificada em um Único Script
# ==========================================================
# Este arquivo contém todos os módulos do projeto, desde
# conceitos básicos até a API com Flask e SQLite.
# ==========================================================

# ==========================================================
# Módulo 01 - Introdução
# ==========================================================
def mostrar_introducao():
    print("🚀 Bem-vindo(a) ao projeto Código da Transformação!")
    print("Este é o Módulo 01, onde damos início à nossa jornada.")


# ==========================================================
# Módulo 02 - Lógica de Programação
# ==========================================================
def verificar_par_ou_impar(numero: int) -> str:
    if numero % 2 == 0:
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."


def calcular_fatorial(n: int) -> int:
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# ==========================================================
# Módulo 03 - Estruturas de Dados
# ==========================================================
def manipular_lista():
    numeros = [1, 2, 3, 4, 5]
    numeros.append(6)
    for n in numeros:
        print(f"Número: {n}")


def manipular_dicionario():
    pessoa = {"nome": "Nathalia", "idade": 25, "cidade": "São Paulo"}
    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")


def manipular_conjunto():
    conjunto_a = {1, 2, 3, 4}
    conjunto_b = {3, 4, 5, 6}
    uniao = conjunto_a | conjunto_b
    intersecao = conjunto_a & conjunto_b
    print(f"União: {uniao}")
    print(f"Interseção: {intersecao}")


# ==========================================================
# Módulo 13 - API com Flask e SQLite
# ==========================================================
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}


with app.app_context():
    db.create_all()


# Rotas da API
@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"mensagem": "Olá, seja bem-vindo(a) à API do projeto Código da Transformação!"})


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")

    novo_usuario = Usuario(nome=nome, email=email)
    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso.",
        "usuario": novo_usuario.to_dict()
    })


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios])


# ==========================================================
# Execução do Projeto
# ==========================================================
if __name__ == "__main__":
    # Teste dos módulos básicos
    mostrar_introducao()
    print(verificar_par_ou_impar(7))
    print(f"Fatorial de 5: {calcular_fatorial(5)}")
    manipular_lista()
    manipular_dicionario()
    manipular_conjunto()

    # Inicialização do servidor Flask
    print("\n🚀 Servidor Flask rodando em: http://127.0.0.1:5000")
    app.run(debug=True)
