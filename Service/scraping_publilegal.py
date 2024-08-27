import re
import time

from playwright.sync_api import Page, expect, sync_playwright

class ScrapingPublilegal():
    def __init__(self, url):
        self.url = url

    def get_pagina_principal(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto(self.url)

            page.wait_for_load_state('load')

            page.get_by_text(text='Balanço', exact=True).click()

            div_parente = page.locator(".jet-listing-grid__items.grid-col-desk-1.grid-col-tablet-1.grid-col-mobile-1.jet-listing-grid--237")
            divs_filhas = div_parente.locator("div").all()

            time.sleep(5)

            for div_filha in divs_filhas:
                dados_pagina = self.get_dados_pagina(div_filha=div_filha)

                print('')

            print('')

    def get_dados_pagina(self, div_filha):
        try:
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
            else:
                empresa = ''
                data = ''
                secao = ''
                print('Dados nao encontrados')

            return {'empresa': empresa, 'data': data, 'secao': secao}
        except Exception as ex:
            print(ex)