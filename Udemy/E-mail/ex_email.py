

# Eviando E-mails SMTP com Python

import os
from dotenv import load_dotenv 

load_dotenv()

# dados do remetente

remetente = os.getenv('FROM_EMAIL', '')
destinatario = 'davidmaf@gmail.com'

# configurações SMTP

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWD', '')

# Mensagem de texto
import pathlib
import string

caminho_html = pathlib.Path(__file__).parent / 'frase.html'

with open(caminho_html, 'r') as arq:
    texto = arq.read()
    template = string.Template(texto)
    new_texto = template.substitute(nome='David')

# Transformar em MIMEMultipart

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Assunto do E-mail'

corpo_email = MIMEText(new_texto, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Abrindo o Server SMTP

import smtplib

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print("Sucesso")
