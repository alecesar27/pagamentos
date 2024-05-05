from webhook  import app, database
from webhook.models import Usuario,Cliente,Curso,Pagamento,Cliente_Curso

def limpar_banco():
  with app.app_context():
   database.drop_all()
   database.create_all()

#usuario = Usuario(username="alecesar27",email="alecesar27@yahoo.com.br",senha='123456',token='uhdfaAADF123')



def carregar_cursos():
   with app.app_context():
      curso1 = Curso(nome="Python Impressionador")
      curso2 = Curso(nome="JavaScript Impressionador")
      curso3 = Curso(nome="Excel Impressionador")
      curso4 = Curso(nome="PowerBI Impressionador")
      curso5 = Curso(nome="Power Point Impressionador")

      database.session.add(curso1)
      database.session.add(curso2)
      database.session.add(curso3)
      database.session.add(curso4)
      database.session.add(curso5)
      database.session.commit()

def carregar_clientes():
  with app.app_context():
    cliente1 = Cliente(nome="Monteiro da Paixão Santana",email="monteiro@gmail.com")
    cliente2 = Cliente(nome="Biribiri da Paixão Silva", email="biribiri@gmail.com")
    cliente3 = Cliente(nome="Esplanada da Paixão Souza", email="explanada@gmail.com")
    cliente4 = Cliente(nome="Militão da Paixão Pereira", email="militao@gmail.com")
    cliente5 = Cliente(nome="Milindro da Paixão Filho", email="milindro@gmail.com")
    cliente6 = Cliente(nome="Mariana Dantas Souza", email="mariana@gmail.com")
    cliente7 = Cliente(nome="Euripes dos Santos Conceição", email="euripeds@gmail.com")
    cliente8 = Cliente(nome="Doralice Matias Santos", email="doralice@gmail.com")
    cliente9 = Cliente(nome="Jurema de oliveira", email="jurema@gmail.com")
    cliente10 = Cliente(nome="Elimateia de Jesus", email="elimateia@gmail.com")
    cliente11 = Cliente(nome="Ernesto Sampaio", email="ernesto@gmail.com")
    cliente12 = Cliente(nome="Bartolomeu Sampaio da Silva", email="bartolomeu@gmail.com")
    cliente13 = Cliente(nome="Edna Santana do Carmo Santos", email="edna@gmail.com")
    cliente14 = Cliente(nome="Expedito Vieira Santos", email="expedito@gmail.com")
    cliente15 = Cliente(nome="Alex Cesar dos Santos", email="alex@gmail.com")
    cliente16 = Cliente(nome="Tereza Paim do Carmo", email="tereza@gmail.com")
    cliente17 = Cliente(nome="Antonio Peixoto da Paixão", email="antonio@gmail.com")
    cliente18 = Cliente(nome="Tiago da Paixão do Carmo", email="tiago@gmail.com")
    cliente19 = Cliente(nome="Experidião Dantas da Silva", email="experidiao@gmail.com")
    cliente20 = Cliente(nome="Alan Santana do Carmo Santos", email="alan@gmail.com")

    database.session.add(cliente1)
    database.session.add(cliente2)
    database.session.add(cliente3)
    database.session.add(cliente4)
    database.session.add(cliente5)
    database.session.add(cliente6)
    database.session.add(cliente7)
    database.session.add(cliente8)
    database.session.add(cliente9)
    database.session.add(cliente10)
    database.session.add(cliente11)
    database.session.add(cliente12)
    database.session.add(cliente13)
    database.session.add(cliente14)
    database.session.add(cliente15)
    database.session.add(cliente16)
    database.session.add(cliente17)
    database.session.add(cliente18)
    database.session.add(cliente19)
    database.session.add(cliente20)
    database.session.commit()

  def consultar_usuarios():
    with app.app_context():
      usuarios =Usuario.query.all()
    return usuarios

  def consultar_clientes():
    with app.app_context():
      clientes =Cliente.query.all()
    return clientes

  def consultar_cursos():
    with app.app_context():
      cursos =Curso.query.all()
    return cursos

def carregar_cliente_curso():
  with app.app_context():
    cliente_curso1 = Cliente_Curso(id_curso=Curso.query.filter_by(id=1).first().id,
                              id_cliente=Cliente.query.filter_by(id=1).first().id)
    cliente_curso2 = Cliente_Curso(id_curso=Curso.query.filter_by(id=2).first().id,
                              id_cliente=Cliente.query.filter_by(id=2).first().id)

    cliente_curso3 = Cliente_Curso(id_curso=Curso.query.filter_by(id=3).first().id,
                              id_cliente=Cliente.query.filter_by(id=3).first().id)

    cliente_curso4 = Cliente_Curso(id_curso=Curso.query.filter_by(id=4).first().id,
                              id_cliente=Cliente.query.filter_by(id=4).first().id)

    cliente_curso5 = Cliente_Curso(id_curso=Curso.query.filter_by(id=5).first().id,
                              id_cliente=Cliente.query.filter_by(id=5).first().id)

    cliente_curso6 = Cliente_Curso(id_curso=Curso.query.filter_by(id=1).first().id,
                              id_cliente=Cliente.query.filter_by(id=1).first().id)

    cliente_curso7 = Cliente_Curso(id_curso=Curso.query.filter_by(id=2).first().id,
                              id_cliente=Cliente.query.filter_by(id=2).first().id)

    cliente_curso8 = Cliente_Curso(id_curso=Curso.query.filter_by(id=3).first().id,
                              id_cliente=Cliente.query.filter_by(id=3).first().id)

    cliente_curso9 = Cliente_Curso(id_curso=Curso.query.filter_by(id=4).first().id,
                              id_cliente=Cliente.query.filter_by(id=4).first().id)

    cliente_curso10 = Cliente_Curso(id_curso=Curso.query.filter_by(id=5).first().id,
                              id_cliente=Cliente.query.filter_by(id=5).first().id)

    cliente_curso11 = Cliente_Curso(id_curso=Curso.query.filter_by(id=1).first().id,
                              id_cliente=Cliente.query.filter_by(id=1).first().id)

    cliente_curso12 = Cliente_Curso(id_curso=Curso.query.filter_by(id=2).first().id,
                              id_cliente=Cliente.query.filter_by(id=2).first().id)

    cliente_curso13 = Cliente_Curso(id_curso=Curso.query.filter_by(id=3).first().id,
                              id_cliente=Cliente.query.filter_by(id=3).first().id)

    cliente_curso14 = Cliente_Curso(id_curso=Curso.query.filter_by(id=4).first().id,
                              id_cliente=Cliente.query.filter_by(id=4).first().id)

    cliente_curso15 = Cliente_Curso(id_curso=Curso.query.filter_by(id=5).first().id,
                              id_cliente=Cliente.query.filter_by(id=5).first().id)

    cliente_curso16 = Cliente_Curso(id_curso=Curso.query.filter_by(id=1).first().id,
                              id_cliente=Cliente.query.filter_by(id=1).first().id)

    cliente_curso17 = Cliente_Curso(id_curso=Curso.query.filter_by(id=1).first().id,
                              id_cliente=Cliente.query.filter_by(id=1).first().id)

    cliente_curso18 = Cliente_Curso(id_curso=Curso.query.filter_by(id=1).first().id,
                              id_cliente=Cliente.query.filter_by(id=1).first().id)
    cliente_curso19 = Cliente_Curso(id_curso=Curso.query.filter_by(id=1).first().id,
                              id_cliente=Cliente.query.filter_by(id=1).first().id)

    cliente_curso20 = Cliente_Curso(id_curso=Curso.query.filter_by(id=1).first().id,
                              id_cliente=Cliente.query.filter_by(id=1).first().id)

    database.session.add(cliente_curso1)
    database.session.add(cliente_curso2)
    database.session.add(cliente_curso3)
    database.session.add(cliente_curso4)
    database.session.add(cliente_curso5)
    database.session.add(cliente_curso6)
    database.session.add(cliente_curso7)
    database.session.add(cliente_curso7)
    database.session.add(cliente_curso8)
    database.session.add(cliente_curso9)
    database.session.add(cliente_curso10)
    database.session.add(cliente_curso11)
    database.session.add(cliente_curso12)
    database.session.add(cliente_curso13)
    database.session.add(cliente_curso14)
    database.session.add(cliente_curso15)
    database.session.add(cliente_curso16)
    database.session.add(cliente_curso17)
    database.session.add(cliente_curso18)
    database.session.add(cliente_curso19)
    database.session.add(cliente_curso20)
    database.session.commit()
#Descomentar um de cada vez e executar na ordem
#limpar_banco()
#carregar_cursos()
#carregar_clientes()
#carregar_cliente_curso()

with app.app_context():
  lista_cliente_curso= Cliente_Curso.query.all()
  lista_curso   = Curso.query.all()
  lista_cliente = Cliente.query.all()
  lista_usuario = Usuario.query.all()
  lista_pagamentos = Pagamento.query.all()
  print(lista_cliente_curso)
  print(lista_cliente)
  print(lista_curso)
  print(lista_usuario)
  print(lista_pagamentos)
