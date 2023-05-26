from flask import render_template
from flask_login import login_required
from painel import app, db
from painel.vendas.forms import FormNovaVenda


@app.route('/novavenda')
@login_required
def novavenda():
    form = FormNovaVenda()
    return render_template('vendas/homevendas.html', form=form)
