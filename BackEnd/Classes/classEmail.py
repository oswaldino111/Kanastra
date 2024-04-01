# -*- coding: utf-8 -*-
import smtplib
from email.message import EmailMessage
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class Email:

    def __init__(self, destinatario: str):
        self.destinatario = destinatario #Trocar para um email pessoal para ver ele chegar
        self.login = config["EMAIL"]["LOGIN"]           # Recomendo trocar a conta pois o outlook bloqueia depois de poucos testes
        self.password = config["EMAIL"]["PASSWORD"]     # 
        self.file_name = f'boleto-santander-{destinatario.replace(".", "_")}.pdf'
        self.msg = None


    def __criando_mensagem(self):
        """
            ### Cria o conteúdo da mensagem
            Args:
                None
            Retorno:
                None
        """
        self.msg = EmailMessage()
        self.msg['From'] = self.login
        self.msg['To'] = self.destinatario
        self.msg['Subject'] = "Boleto Kanastra"
        self.msg.set_content("Segue em anexo o boleto, Abs.")

        with open(self.file_name, "rb") as f:
            file_data = f.read()
            file_name = f.name
            self.msg.add_attachment(file_data, maintype='application', subtype = 'octet-stream', filename=file_name)



    def __enviar_email(self):
        """
            ### Envia o email usando o processo do smtplib
            Args:
                None
            Retorno:
                None
        """
        server = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        server.ehlo()
        server.starttls()
        server.login(self.login, self.password)
        server.sendmail(self.login, self.destinatario, self.msg.as_string())
        server.quit()


    def main(self):
        """
            ### Processo main para envio de email
            Args:
                None
            Retorno:
                None
        """
        self.__criando_mensagem()
        self.__enviar_email()
        return "200"