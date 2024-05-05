import requests
from webhook.models import Cliente,Pagamento
from webhook  import app, database,EnviarEmail
import time

def load_webhooks():



    lista_webhook={
           'https://webhook.site/9b033056-0430-4b99-8794-0847df9321a7',
           'https://webhook.site/1671cbb7-571c-4bf1-9ced-8d1b96f0e70e',
           'https://webhook.site/331a2300-d4d3-4d5f-ad11-d6692df251f8',
           'https://webhook.site/5f8cc72a-a1ed-4fdf-bd59-89f870acc959',
           'https://webhook.site/08461a3d-c722-4656-8ac2-83402da1a481',
           'https://webhook.site/7f318c14-7081-4a82-b58a-0ec44b930ef6',
           'https://webhook.site/ddc59004-d38e-4cb5-9bbd-788f78e8a266',
           'https://webhook.site/79c7db55-81db-4cdb-bf31-ae4738538916',
           'https://webhook.site/57e881fd-e09e-4fd4-91b5-9adb16dfbedc',
           'https://webhook.site/3eefd42d-5ad5-4b78-90b9-c6dd72e82d15',
           'https://webhook.site/7e7ff582-a95c-4fc8-a461-135c75df29ce',
           'https://webhook.site/55eccfee-a1d3-4cc7-92c7-5de8e935670d',
           'https://webhook.site/a2ee0b8b-63fc-430b-9f41-7aae69c061fa',
           'https://webhook.site/7fa6000e-caa5-47ca-bdb9-62302eba017c',
           'https://webhook.site/e0e93bf2-0fe0-45a9-8486-5c2c929802ff',
           'https://webhook.site/aed14b9e-9b62-4962-9142-5fb573087f3f',
           'https://webhook.site/354f0eac-3c05-49d8-9c43-bf3d49270c44',
           'https://webhook.site/e887c64d-242a-4bdd-a816-ea4377942fa1',
           'https://webhook.site/d102502b-82c0-46b6-a35e-28632c3ce55f',
           'https://webhook.site/3ea934fd-1a1f-4348-8f9e-ebef7945ff10',
            }
    return lista_webhook

def processar_pagamento(lista):
     with app.app_context():
       for item in lista:
          webhook = requests.get(item)
          retorno = webhook.json()
          print(retorno)
          time.sleep(60)
          if retorno['status'] == 'aprovado':
            id_cliente = Cliente.query.filter_by(email=retorno['email']).first().id
            cliente = Cliente.query.filter_by(email = retorno['email']).update({'ativo':True})
            database.session.commit()
            #EnviarEmail.send_mail(retorno['email'],retorno['status'])
            print("Bem vindo ao Curso Python impressionador, Acesso liberado")

            if cliente:
               pagamento = Pagamento(status=retorno['status'],valor=retorno['valor'],
                                           forma=retorno['forma_pagamento'],id_cliente=int(id_cliente))
               database.session.add(pagamento)
               database.session.commit()

            elif retorno['status'] == 'recusado':
               id_cliente = Cliente.query.filter_by(email=retorno['email']).first().id
               pagamento = Pagamento(status=retorno['status'],valor=retorno['valor'],
                             forma=retorno['forma_pagamento'],id_cliente=int(id_cliente))
               database.session.add(pagamento)
               database.session.commit()
               #EnviarEmail.send_mail(retorno['email'], retorno['status'])
               print('Seu pagamento foi recusado, favor realizar uma nova tentativa')

            elif retorno['status'] == 'reembolsado':
              id_cliente = Cliente.query.filter_by(email=retorno['email']).first().id
              pagamento = Pagamento(status=retorno['status'], valor=retorno['valor'],
                                         forma=retorno['forma_pagamento'], id_cliente=int(id_cliente))
              database.session.add(pagamento)
              cliente = Cliente.query.filter_by(email = retorno['email']).update({'ativo':False})

              database.session.commit()
              #EnviarEmail.send_mail(retorno['email'], retorno['status'])
              print("Você foi reembolsado favor verificar a conta informada para depósito. Seu acesso foi revogado")

       #chamada da função para consultar os webhooks e realizar as operações
       # Favor acessar a o arquivo testes.py para limpar o banco
       processar_pagamento(load_webhooks())