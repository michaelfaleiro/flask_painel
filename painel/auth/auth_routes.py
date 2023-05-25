from painel import app, db, bcrypt
from flask import render_template, request, redirect, url_for
from painel.auth.models import User
from painel.auth.forms import FormCreate, FormLogin
from flask_login import login_required, login_user, logout_user, current_user


@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if request.method == 'POST':
        if form_login.validate_on_submit():
            usuario = User.query.filter_by(email=form_login.email.data).first()
            if usuario and bcrypt.check_password_hash(usuario.password, form_login.password.data):
                login_user(usuario)
                return redirect(url_for('home'))
    return render_template('auth/login.html', form=form_login)


@app.route('/auth/new', methods=['POST', 'GET'])
def new():
    form_create = FormCreate()
    if request.method == 'POST':
        password_hash = bcrypt.generate_password_hash(
            form_create.password.data).decode('utf8')
        usuario = User(first_name=form_create.first_name.data,
                       last_name=form_create.last_name.data, email=form_create.email.data, password=password_hash)
        db.session.add(usuario)
        db.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('login'))

    return render_template('auth/newuser.html', form=form_create)


@app.route('/auth/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
