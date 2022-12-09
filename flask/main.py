from flask import Flask, render_template, request, redirect
from pessoa import Pessoa

app = Flask(__name__)

pessoa1 = Pessoa('Everton', '32', '1.82')
pessoa2 = Pessoa('Denega', '43', '1.75')
pessoa3 = Pessoa('Souza', '17', '1.60')

lista = [pessoa1, pessoa2, pessoa3]

@app.route("/")
def inicio():    
    return render_template('index.html', titulo='LISTA DE PESSOAS', pessoas=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='CADASTRO DE PESSOA')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']
    
    nova_lista = Pessoa(nome, idade, altura)

    lista.append(nova_lista)
    return redirect('/')

app.run(debug=True)