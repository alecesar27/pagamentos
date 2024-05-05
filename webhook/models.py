from webhook import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return  Usuario.query.get(int(id_usuario))
    


class Usuario(database.Model,UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    token = database.Column(database.String, nullable=False)


    def get_token(self):
      return 'uhdfaAADF123'

class Cliente(database.Model,UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False)
    ativo = database.Column(database.Boolean, nullable=False,default=False)


class Pagamento(database.Model):
     id = database.Column(database.Integer, primary_key=True)
     status = database.Column(database.String, nullable=False)
     valor  = database.Column(database.Float, nullable=False)
     forma = database.Column(database.String, nullable=False)
     id_cliente = database.Column(database.Integer, database.ForeignKey('cliente.id'), nullable=False)
     cliente = database.relationship('Cliente', backref='cliente', lazy=True)


class Curso(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)



class Cliente_Curso(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_curso = database.Column(database.Integer, database.ForeignKey('curso.id'), nullable=False)
    id_cliente = database.Column(database.Integer, database.ForeignKey('cliente.id'), nullable=False)
    curso = database.relationship('Curso', backref='curso', lazy=True)
    aluno = database.relationship('Cliente', backref='aluno', lazy=True)
