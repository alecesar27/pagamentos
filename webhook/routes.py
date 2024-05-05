from flask import render_template, redirect, url_for, flash, request
from webhook import app,database,bcrypt, WebhookController
from webhook.forms import FormLogin, FormCriarConta
from webhook.models import Usuario,Cliente,Pagamento,Cliente_Curso
from flask_login import login_user,logout_user,current_user
from flask import Flask, render_template, request, Response, send_file
import time




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha,form_login.senha.data):
            login_user(usuario,remember=form_login.lembrar_dados.data )
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash(f'Falha no Login.E-mail ou senha incorretos', 'alert-danger')
        
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript= bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data , email=form_criarconta.email.data, senha=senha_cript,token=form_criarconta.token.data)
        database.session.add(usuario)
        database.session.commit()        
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

@app.route('/usuarios')
def usuarios():
    lista_usuarios= Usuario.query.all()
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/clientes')
def clientes():
    lista_clientes= Cliente.query.all()
    return render_template('clientes.html', lista_clientes=lista_clientes)

@app.route('/pagamentos')
def pagamentos():
    lista_pagamentos= Pagamento.query.all()
    return render_template('pagamentos.html', lista_pagamentos=lista_pagamentos)

@app.route('/clientescursos')
def clientescursos():
    lista_clientes_cursos= Cliente_Curso.query.all()
    return render_template('clientes_cursos.html', lista_pagamentos=lista_clientes_cursos)

@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@app.route('/retornos')
def retornos():
    print("Início do programa")
    lista_webhooks = WebhookController.load_webhooks()
    WebhookController.processar_pagamento(lista_webhooks)


@app.route("/pagamento_csv")
def pagamentos_csv():
    csv_data = ""
    lista_pagamentos =Pagamento.query.all()
    for pagamento in lista_pagamentos:
        csv_data += f"Situação :{pagamento.status}\n R$ {pagamento.valor}\nForma: {pagamento.forma}\nNome do Cliente: {pagamento.cliente.nome}\n  ------------------------------------------------------------------------------------------\n"

    response = Response(csv_data, content_type="text/csv")

    response.headers["Content-Disposition"] = "attachment; filename=pagamentos.csv"

    return response

@app.route("/clientes_csv")
def clientes_csv():
    csv_data = ""
    lista_clientes =Cliente.query.all()
    for cliente in lista_clientes:
        csv_data += f'''Nome :{cliente.nome}\n 
                     Email: {cliente.email}\n
                     Situação: { cliente.ativo}
              \n ------------------------------------------------------------------------------------------\n'''

    response = Response(csv_data, content_type="text/csv")

    response.headers["Content-Disposition"] = "attachment; filename=clientes.csv"

    return response

@app.route('/sair')
def sair():
    logout_user()
    flash(f'Logout feito com sucesso', 'alert-success')
    return redirect(url_for('home'))








