import pandas as pd
import datetime

class Planilhas():
    def __init__(self, dados):
        self.dados = dados

    def transforma_em_planilha(self):
        try:
            df = pd.DataFrame(self.dados)
            data_hoje = datetime.datetime.now().strftime("%Y-%m-%d")

            nome_arquivo = f"Extract_{data_hoje}.xlsx"

            df.to_excel(nome_arquivo, index=False)

            print(f"Arquivo criado com sucesso: {nome_arquivo}")

        except Exception as ex:
            print(ex)