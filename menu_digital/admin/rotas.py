from flask import render_template, session, request, redirect, url_for, flash
from menu_digital import app, db
from .models import User, Reparticao, Cardapio
from .forms import Registro, Login_form
from menu_digital import app, db, bcrypt
import os


# Rotas de Administrativas
@app.route("/gestor")
def gestor():
    if 'username' not in session:
        flash(f'Favor realizar seu login primeiro!!!')
        return redirect(url_for('login'))

    reparticoes = Reparticao.query.all()
    cardapios = Cardapio.query.all()
    return render_template('gestor.html', title='Pagina Administrativa', reparticoes=reparticoes, cardapios=cardapios)

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Rotas de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_form(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['username'] = form.username.data
            flash(f'Olá {form.username.data} você está logado', 'success')
            return redirect(request.args.get('next') or url_for('gestor'))
        else:
            flash('NÃO FOI POSSÍVEL LOGAR')
    return render_template('/login.html', form=form, title='Pagina Login')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = Registro(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Obrigado {form.username.data} por se registrar', 'success')
        return redirect(url_for('login'))
    return render_template('registrar.html', form=form, title="Pagina de registros")







