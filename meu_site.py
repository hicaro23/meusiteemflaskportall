from flask import Flask, render_template

app = Flask(__name__)

#cria a 1º pagina do soite
#route -> nomedosite.com/caminho
#funcao -> o que voce quer exibir na página

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    #return nome_usuario
    return render_template("usuarios.html",nome_usuario = nome_usuario)

#colocar site no ar
if __name__ == "__master__":
    app.run(debug=True)