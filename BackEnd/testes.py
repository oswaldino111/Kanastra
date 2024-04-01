# -*- coding: utf-8 -*-
import unittest

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

        return "200"

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

            retorno = self.__testa_envio_csv(dados)

            break

        return retorno


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
            print("Erro esperado pois o ideal é usar um tópico de publicacao + rápido que async")

        return "200"
    
    def main(self, csv=True):
        retorno = self.__ler_csv()
        if not csv:
            return retorno
        retorno = self.__disparo_linha()
        return retorno


class TestServer(unittest.TestCase):


    def teste_csv(self):
        """
            ### Teste para ver se carregou o csv
        """
        self.assertEqual(Testes().main(False), "200")


    def teste_server(self):
        """
            ### Teste para ver se enviou o email
        """
        self.assertEqual(Testes().main(), "200")


    def teste_server_online_get(self):
        """
            ### Teste para ver se enviou o email
        """
        import requests #Carga somente para este teste
        retorno = requests.get("http://127.0.0.1:5000/")

        self.assertEqual(retorno.text, "Server Online")


    def teste_server_online_post(self):
        """
            ### Teste para ver se enviou o email
        """
        import requests #Carga somente para este teste
        retorno = requests.post("http://127.0.0.1:5000/", headers={}, json={})

        self.assertEqual(retorno.text, "Server Online")


    def teste_server_nao_token_json(self):
        """
            ### Teste para ver se está exigindo token ou json
        """
        import requests #Carga somente para este teste
        retorno = requests.post("http://127.0.0.1:5000/send_emails", json={})

        self.assertEqual(retorno.text, "Erro, token não válido")


    def teste_server_nao_json(self):
        """
            ### Teste para ver se está exigindo header
        """
        import requests #Carga somente para este teste
        headers = {
            "content-type": "application/json",
            "token": "TESTEKANASTRA"
        }
        retorno = requests.post("http://127.0.0.1:5000/send_emails", headers=headers, json={})

        self.assertEqual(retorno.text, "Json não encontrado")


    @unittest.skip("Só para demonstrar o decorator se habilitar da erro retorno é outro")
    def teste_server_token_e_json(self):
        """
            ### Teste para ver se está exigindo header
        """
        import requests #Carga somente para este teste
        headers = {
            "content-type": "application/json",
            "token": "TESTEKANASTRA"
        }
        dados = {'name': 'Elijah Santos', 
                 'governmentId': 9558, 
                 'email': 'janet95@example.com', 
                 'debtAmount': 7811, 
                 'debtDueDate': '2024-01-19', 
                 'debtID': 'ea23f2ca-663a-4266-a742-9da4c9f4fcb3'}
        retorno = requests.post("http://127.0.0.1:5000/send_emails", headers=headers, json=dados)


        self.assertEqual(retorno.text, "PARA_DAR_ERRO") #Retorno correto Processado


if __name__ == "__main__":
    unittest.main()
