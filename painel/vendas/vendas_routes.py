from flask import render_template, request, redirect
from flask_login import login_required
from painel import app, db
from painel.vendas.forms import FormNovaVenda
from .models import Vendas


@app.route('/vendas')
@login_required
def homevendas():
    vendas = Vendas.query.all()
    return render_template('vendas/homevendas.html', card=vendas)


@app.route('/novavenda', methods=['GET', 'POST'])
@login_required
def novavenda():
    form = FormNovaVenda()
    if request.method == 'POST':
        if form.validate_on_submit():
            venda = Vendas(nome=form.nome.data,
                           carro=form.carro.data,
                           placa=form.placa.data,
                           chassi=form.chassi.data
                           )
            db.session.add(venda)
            db.session.commit()
            print(venda)
            return redirect('vendas')
    vendas = Vendas.query.all()
    return render_template('vendas/homevendas.html', form=form, card=vendas)
