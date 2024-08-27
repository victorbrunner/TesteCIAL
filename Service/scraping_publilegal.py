import os
import re
import time
import requests
from Service.planilhas import Planilhas
from playwright.sync_api import Page, expect, sync_playwright
from PyPDF2 import PdfReader

class ScrapingPublilegal():
    def __init__(self, url):
        self.url = url
        self.dados = []

    def get_cnpjs(self, dados):
        try:
            for dado in dados:
                bytes_pdf = requests.get(dado['link_balanco']).content

                time.sleep(5)

                with open('pdf_extracao.pdf', 'wb') as arquivo:
                    arquivo.write(bytes_pdf)

                with open('pdf_extracao.pdf', 'rb') as pdf_file:
                    reader = PdfReader(pdf_file)
                    page = reader.pages[0]  # Assumindo que o CNPJ está na primeira página

                    texto = page.extract_text()

                    # REGEX para encontrar o CNPJ
                    pattern = r"CNPJ/MF nº (\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})"
                    match = re.search(pattern, texto)

                    if match:
                        cnpj = match.group(1)
                    else:
                        cnpj = ''

                dado['cnpj'] = cnpj

                os.remove('pdf_extracao.pdf')

            return dados
        except Exception as ex:
            print(ex)

    def manipulando_dados(self, dados):
        try:
            # Iterando sobre os dados ao contrário para remover todos dados que nao contem informações.
            for i in reversed(range(len(dados))):
                if dados[i]['empresa'] == '':
                    del dados[i]

            # Removendo duplicacao de emrpesas
            empresas_vistas = set()
            dados_final = []

            for dado in dados:
                empresa = dado['empresa']
                if empresa not in empresas_vistas:
                    empresas_vistas.add(empresa)
                    dados_final.append(dado)

            return dados_final
        except Exception as ex:
            print(ex)

    def get_dados_pagina(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto(self.url)

            page.wait_for_load_state('load')

            page.get_by_text(text='Balanço', exact=True).click()

            time.sleep(10)

            div_parente = page.locator(".jet-listing-grid__items.grid-col-desk-1.grid-col-tablet-1.grid-col-mobile-1.jet-listing-grid--237")
            divs_filhas = div_parente.locator("div").all()

            for div_filha in divs_filhas:
                print(div_filha.inner_text())
                dados_pagina = self.get_informacoes_pagina(div_filha=div_filha)
                self.dados.append(dados_pagina)

            return self.dados

    def get_informacoes_pagina(self, div_filha):
        try:
            # Pegando dados da página
            print(f'\n\nDados pagina: {div_filha.inner_text()}')
            textos = div_filha.inner_text()

            pattern_empresa = r"Empresa:\n(.*)\nData:"
            pattern_data = r"Data:\n(.*)\nSeção:"
            pattern_secao = r"Seção:\n(.*)\nDisponível:"

            match_empresa = re.search(pattern_empresa, textos)
            match_data = re.search(pattern_data, textos)
            match_secao = re.search(pattern_secao, textos)

            if match_empresa and match_data and match_secao:
                empresa = match_empresa.group(1).strip()
                data = match_data.group(1).strip()
                secao = match_secao.group(1).strip()

                # Pegando link do balanço
                link_balanco = div_filha.get_by_role('button').first.get_attribute('href')
            else:
                empresa = ''
                data = ''
                secao = ''
                link_balanco = ''
                print('Dados nao encontrados')

            return {'empresa': empresa, 'data': data, 'secao': secao, 'link_balanco': link_balanco}
        except Exception as ex:
            print(ex)