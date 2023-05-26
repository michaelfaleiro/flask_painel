from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class FormNovaVenda(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    carro = StringField('Carro', validators=[DataRequired()])
    placa = StringField('Placa')
    chassi = StringField('Chassi')
    botao_salvar = SubmitField('Salvar')
