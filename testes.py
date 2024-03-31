# -*- coding: utf-8 -*-


class Testes:

    def __init__(self):
        self.url = "http://127.0.0.1:5000/send_emails"
        self.csv = None
        self.headers = {
            "content-type": "application/json",
            "token": "TESTEKANASTRA"
        }


    def __ler_csv(self):
        """
            ### Vai ler arquivo csv para testar a api a parte do front
            Args:
                None
            Retorno:
                None
        """
        import pandas as pd
        dados = pd.read_csv(r"C:\Users\oswal\Downloads\Desafio Kanastra\input.csv", sep=",")
        self.csv = dados


    def __disparo_linha(self):
        """
            ### Realiza o disparo de cada linha como requisição no python
            Args:
                None
            Retorno:
                None
        """
        for index, linha in self.csv.iterrows():

            print(linha)

            dados = {
                "name": linha["name"],
                "governmentId": linha["governmentId"],
                "email": linha["email"],
                "debtAmount": linha["debtAmount"],
                "debtDueDate": linha["debtDueDate"],
                "debtID": linha["debtId"],
            }

            self.__testa_envio_csv(dados)

            break


    def __testa_envio_csv(self, dados: dict):
        """
            ### Realiza o envio de solicitaçoes para o server local
            Args:
                Json com os dados da linha
        """
        import requests #Carga somente para este teste

        print(dados)

        try:
            requests.post(self.url, json=dados, headers=self.headers, timeout=0.01)
        except:
            pass
        return "200"



    def main(self):
        self.__ler_csv()
        self.__disparo_linha()


if __name__ == "__main__":
    teste = Testes()

    teste.main()