import os

class Files:

    @staticmethod
    def remove_file(file_name):
        """
            ### Deleta arquivos
            Args:
                None
            Retorno:
                literal string
        """
        os.remove(f'boleto-santander-{file_name.replace(".", "_")}.pdf')

        return "200"