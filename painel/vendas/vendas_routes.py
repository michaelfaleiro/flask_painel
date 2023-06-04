from flask import render_template, request, redirect, url_for
from flask_login import login_required
from painel import app, db
from painel.vendas.forms import FormNovaVenda, Form_Produto
from .models import Vendas, Produtos_Vendas


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
                           chassi=form.chassi.data,
                           )
            db.session.add(venda)
            db.session.commit()
            return redirect('vendas')
    vendas = Vendas.query.all()
    return render_template('vendas/homevendas.html', form=form, card=vendas)


@app.route('/venda/<item_id>', methods=['GET', 'POST'])
@login_required
def venda(item_id):
    form = Form_Produto()
    venda = Vendas.query.get(item_id)
    return render_template('vendas/editvenda.html', venda=venda, form=form)


@app.route('/venda/<venda_id>/produto', methods=['GET', 'POST'])
@login_required
def adicionar_produto(venda_id):
    form = Form_Produto()
    if request.method == 'POST':
        if form.validate_on_submit():
            produto = Produtos_Vendas(
                quantidade=form.quantidade.data, sku=form.sku.data, produto=form.produto.data, preco=form.preco.data, id_venda=venda_id)
            db.session.add(produto)
            db.session.commit()
            return redirect(f'/venda/{venda_id}')


@app.route('/venda/<venda_id>/<produto_id>/delete', methods=['POST', 'GET'])
@login_required
def excluir_produto(produto_id, venda_id):
    produto = Produtos_Vendas.query.get(produto_id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(f"/venda/{venda_id}")
