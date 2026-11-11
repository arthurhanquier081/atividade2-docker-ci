from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def inicio():
    return jsonify(mensagem="Ola! A aplicacao esta rodando dentro de um conteiner Docker.")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/soma")
def soma():
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
    except (KeyError, ValueError):
        return jsonify(erro="Informe a e b como numeros inteiros. Exemplo: /soma?a=2&b=3"), 400
    return jsonify(a=a, b=b, resultado=a - b)


if __name__ == "__main__":
    # host="0.0.0.0" faz a aplicação aceitar conexões vindas de fora do contêiner.
    app.run(host="0.0.0.0", port=8000)