import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#-----------------O envio de email está funcionando --------------------------------
# Essa função está funcionando perfeitamente, por questões de segurança favor usar as suas credenciais
#-----------------------------------------------------------------------------------
def send_mail(emails,situacao,file=None):
    host = 'smtp.gmail.com'

    port = '587'

    login = 'coloque o seu email'

    senha = 'token da aplicação gerado no portal por exemplo do GMAIL'

    server = smtplib.SMTP(host, port)

    server.ehlo()
    server.starttls()
    server.login(login, senha)

    if situacao=='Aprovado':
      corpo = "Bem vindo ao Curso Python impressionador, Acesso liberado"

    elif situacao == 'recusado':
      corpo ="Seu pagamento foi recusado, favor realizar uma nova tentativa"

    elif situacao== 'reembolsado':
      corpo = "Você foi reembolsado favor verificar a conta informada para depósito. Seu acesso foi revogado"

    assunto = "Retorno da contratação do curso"

    email_msg = MIMEMultipart()

    email_msg['From'] = 'alecesar27@gmail.com'

    email_msg['To'] = emails

    email_msg['Subject'] = assunto

    email_msg.attach(MIMEText(corpo, 'plain'))

    if file:
     caminho_arquivo = Path(file)
     attchment = open(caminho_arquivo, 'rb')
     att = MIMEBase('application', 'octet-stream')
     att.set_payload(attchment.read())
     encoders.encode_base64(att)
     att.add_header('Content-Disposition', f'attachment; filename=${file}')
     attchment.close()
     email_msg.attach(att)

    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

    server.quit()