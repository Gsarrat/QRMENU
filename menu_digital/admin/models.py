from menu_digital import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=False, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    user_perm = db.Column(db.String(40), unique=False, nullable=False, default='Padrao')

    def __repr__(self):
        return '<User %r>' % self.username
    
class Reparticao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reparticao = db.Column(db.String(40), unique=False, nullable=False)

class Cardapio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ativo = db.Column(db.Boolean, nullable=False)
    reparticao_id = db.Column(db.Integer, db.ForeignKey('reparticao.id'), nullable=False)
    reparticao = db.relationship('Reparticao')
    nome = db.Column(db.String(40), unique=False, nullable=False)
    descricao = db.Column(db.String(180), unique=False, nullable=True)
    valor = db.Column(db.Float(precision=2), nullable=False)
    imagem = 'photo'


with app.app_context():

    db.create_all()