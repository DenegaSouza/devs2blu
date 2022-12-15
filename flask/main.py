from flask import Flask, render_template, request, redirect, session, url_for, flash
from models.pessoa import Pessoa
from models.usuario import Usuario
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '123'
app.config["SESSION_PERMANENT"] = False

#string conexao
app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "denega",
    senha = "123456",
    servidor = "localhost:5450",
    database = "postgres"
)

usuario1 = Usuario('admin','admin','123')

usuarios = {usuario1.nickname: usuario1,}

db = SQLAlchemy(app)

class Pessoa(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(15), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    altura = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):    
    id = db.Column(db.Integer, autoincrement=True)
    nome = db.Column(db.String(15), nullable=False)
    nickname = db.Column(db.String(10), unique=True, primary_key=True)
    senha = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

lista = Pessoa.query.order_by(Pessoa.id).first()

@app.route('/')
def inicio():        
    return render_template('login.html', titulo='Login Usuário')
    

@app.route('/listar')
def listar():
    lista = Pessoa.query.order_by(Pessoa.id)
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login')
    return render_template('listar.html', titulo='LISTA DE PESSOAS', pessoas=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login')
    return render_template('novo.html', titulo='CADASTRO DE PESSOA')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']
    
    nova_lista = Pessoa(nome=nome, idade=idade, altura=altura)
    
    db.session.add(nova_lista)
    db.session.commit()
    
    return redirect('/listar')

@app.route('/login', methods=['GET', 'POST'])
def login():
    proximo = request.args.get('proximo')
    return render_template('login.html', titulo='Login Usuario', proximo=proximo)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]

        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname

            flash('BEM VINDO ' + usuario.nickname)
            proxima_pagina = request.form['proximo']
            return redirect(proxima_pagina)
        else:
            flash('Usuario ou senha inválidos')
            return redirect(url_for('login'))
    else:
        flash('Usuario ou senha inválidos')
        return redirect(url_for('login'))

    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Você foi desconectado.')
      
    return redirect(url_for('login'))



@app.route('/<int:id>/editar/', methods=('GET', 'POST'))
def editar(id):
    pessoa = Pessoa.query.get_or_404(id)

    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        altura = request.form['altura']

        pessoa.nome = nome
        pessoa.idade = idade
        pessoa.altura = altura


        db.session.add(pessoa)
        db.session.commit()

        return redirect(url_for('listar'))
    return render_template('editar.html', pessoa=pessoa)


@app.post('/<int:id>/deletar/')
def deletar(id):
    pessoa = Pessoa.query.get_or_404(id)
    db.session.delete(pessoa)
    db.session.commit()
    return redirect(url_for('listar'))

app.run(debug=True)