# encoding: utf-8
import os
import assets
import smtplib
from email import encoders
from src.config.config import Config
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
from pathlib import Path
from typing import List
from src.util.util import *


class Mailer:

    def __init__(self, ):

        self.__host = Config.get('mailer', 'server')
        self.__port = Config.get('mailer', 'port')
        self.__ttls = Config.get('mailer', 'ttls') == 'true'
        self.__status = Config.get('mailer', 'status')
        #
        self.__user = Config.get('mailer', 'login')
        self.__pass = Config.get('mailer', 'password')
        self.__from = Config.get('mailer', 'from')

    def enviar_email_notificacao(self, cc: List[str] = None, nome: str = '', grupo: str = ''):

        if self.__status == False:
            return

        reports = get_info('reports', grupo)

        assunto = Config.get('email', grupo, 'assunto')
        to = [Config.get('email', grupo, 'email')]
        conteudo = Config.get('email', grupo, 'conteudo')

        # Cria o cabecalho da mensagem
        if cc is None:
            cc = []
        msg = MIMEMultipart('related; charset=utf-8')
        msg['Subject'] = f'{assunto}'
        msg['From'] = self.__from
        msg['To'] = ','.join(to)
        msg['Cc'] = ','.join(cc)

        # Carrega o arquivo de template
        template = str(Path(assets.__path__[0]) / 'email_notificacao.html')
        msg.attach(self.__carregar_template(template, nome, conteudo))
        for i in reports:
            msg.attach(self.__carregar_anexo(i))
            os.remove(i)
            print('removeu')

        # Envia o email
        self.__enviar_email(to + cc, msg)

    def __enviar_email(self, to_addrs: List[str], message):
        if self.__ttls:
            with smtplib.SMTP(self.__host, self.__port) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.__from, self.__pass)
                smtp.sendmail(self.__from, to_addrs, message.as_string())
                smtp.close()
        else:
            server = smtplib.SMTP(self.__host, self.__port)
            server.connect(self.__host, self.__port)
            server.ehlo()
            server.login(self.__user, self.__pass)
            server.sendmail(self.__from, to_addrs, message.as_string())
            server.quit()

    def __carregar_template(self, template: str, nome: str, conteudo: str) -> MIMEMultipart:
        with open(template, 'r', encoding='utf-8') as file:
            content = ''.join(file.readlines())
            content = content.replace('{nome}', nome)
            content = content.replace('{conteudo}', conteudo)

            text = MIMEMultipart('alternative')
            text.attach(MIMEText(content.encode('utf-8'), 'html', 'utf-8'))
            return text

    def __carregar_anexo(self, anexo):
        with open(anexo, 'rb') as file:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(file.read())

            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f"attachment; filename={basename(Path(anexo))}")
            return attachment