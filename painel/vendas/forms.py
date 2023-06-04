from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired


class FormNovaVenda(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    carro = StringField('Carro', validators=[DataRequired()])
    placa = StringField('Placa')
    chassi = StringField('Chassi')
    botao_salvar = SubmitField('Salvar')


class Form_Produto(FlaskForm):
    quantidade = IntegerField('Quant', validators=[DataRequired()])
    sku = StringField('Sku', validators=[DataRequired()])
    produto = StringField('Produto', validators=[
                          DataRequired()])
    preco = DecimalField('Preco', validators=[DataRequired()])
    botao_adicionar = SubmitField('Adicionar')
