from wtforms import Form, BooleanField, StringField, PasswordField, validators


class Registro(Form):
    username = StringField('Usuario:', [validators.Length(min=4, max=25)])
    password = PasswordField('Senha:', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='as senhas sao diferentes')
    ])
    confirm = PasswordField('repete a senha')

class Login_form(Form):
    username = StringField('Usuario:', [validators.Length(min=4, max=25)])
    password = PasswordField('Senha:', [validators.DataRequired()])
                                        