from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from painel.auth.models import User


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    botao_login = SubmitField('Login')


class FormCreate(FlaskForm):
    first_name = StringField(
        'Nome', validators=[DataRequired(), Length(2, 50)])
    last_name = StringField('Sobrenome', validators=[
                            DataRequired(), Length(2, 50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[
                             DataRequired(), Length(6, 20)])
    password_confirmation = PasswordField('Confirme a senha', validators=[
                                          DataRequired(), EqualTo(password)])
    botao_criar = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = User.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("Email já cadastrado, faça login para continuar")
