# -*- coding: utf-8 -*-
from pyboleto.bank.bradesco import BoletoBradesco
from pyboleto.pdf import BoletoPDF
import datetime


class Boletos:

    def __init__(self, file: dict):
        self.name =  file.get("name")
        self.governmentId = file.get("governmentId")
        self.email = file.get("email")
        self.debtAmount =  file.get("debtAmount")
        self.debtDueDate = file.get("debtDueDate")
        self.debtID = file.get("debtID")


    def __criando_boleto(self):
        """
            ### Responsável por gerar um boleto em python
            ArgS:
                None
            Retorno:
                None
        """
        d = BoletoBradesco()
        d.carteira = '06'  # Contrato firmado com o Banco Bradesco
        d.cedente = 'Kanastra'
        d.cedente_documento = "000.000.000-00"
        d.cedente_endereco = "Rua Testes n 12"
        d.agencia_cedente = '0000-0'
        d.conta_cedente = '00000-0'
        vencimento = self.debtDueDate.split("-")
        d.data_vencimento = datetime.date(int(vencimento[0]), int(vencimento[1]), int(vencimento[2]))
        d.data_documento = datetime.date.today()
        d.data_processamento = datetime.date.today()

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% após o vencimento",
            "- Receber até 10 dias após o vencimento",
            ]
        d.demonstrativo = [
            "- Serviço Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = float(self.debtAmount)

        d.nosso_numero = "1112011668"
        d.numero_documento = "1112011668"
        d.sacado = [
            self.name,
            f"Rua Teste, 00/0000 - Cidade - \
            Governo {self.governmentId}\
            Id de debito {self.debtID}\
            Cep. 00000-000",
            ""
        ]
        boleto_PDF = BoletoPDF(f'boleto-santander-{self.email.replace(".", "_")}.pdf')
        boleto_PDF.drawBoleto(d)
        boleto_PDF.nextPage()
        boleto_PDF.save()


    def main(self):
        """
            ### Classe main de processamento dos boletos
            Args:
                None
            Return:
                Status de retorno para o app
        """
        self.__criando_boleto()
        return "200"