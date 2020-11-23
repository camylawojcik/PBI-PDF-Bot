from time import sleep
from src.download.baixar_reports import *
from src.mailer.mailer import *


def executarExportacao(grupo:str):

    download = DownloadPDF()
    download.downloadReports(grupo)

    email = Mailer()
    email.enviar_email_notificacao(nome='', grupo=grupo)


if __name__ == '__main__':

    grupos_envio = ['grupo2']

    for i in grupos_envio:
        executarExportacao(i)
