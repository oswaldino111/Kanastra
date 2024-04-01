# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_cors import CORS, cross_origin
from Classes import classBoleto, classEmail, deleteFiles
import traceback

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=['POST', 'GET'])
def home_page():
   return "Server Online"


@app.route("/send_emails", methods=['POST'])
def sendEmails():
    try:

        if request.method != 'POST':
            return "200"

        dados = request.get_json()

        if request.headers.get('token') != "TESTEKANASTRA":

          return "Erro, token não válido"

        if dados:
            print(dados)
            processa_arquivos = classBoleto.Boletos(dados)
            retorno = processa_arquivos.main()
            classEmail.Email(dados.get("email")).main()
            #deleteFiles.Files.remove_file(dados.get("email"))
            return "Processado"
        else:

          return "Json não encontrado"
    except:
       print(traceback.format_exc()) 
       return "Json não encontrado"

if __name__ == "__main__":
  app.run(debug=True)