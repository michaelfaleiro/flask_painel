from flask import render_template
from flask_login import current_user, login_required
from painel import app


@app.route('/')
@login_required
def home():
    return render_template('home/home.html', usuario=current_user)


@app.route('/vendas')
@login_required
def homevendas():
    return render_template('vendas/homevendas.html')
