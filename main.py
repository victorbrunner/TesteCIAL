from Service.scraping_publilegal import ScrapingPublilegal
from Service.planilhas import Planilhas

try:
    url = 'https://publilegal.diariodenoticias.com.br/'

    scraping_publilegal = ScrapingPublilegal(url=url)

    dados = scraping_publilegal.get_dados_pagina()

    dados = scraping_publilegal.manipulando_dados(dados=dados)

    dados = scraping_publilegal.get_cnpjs(dados)

    Planilhas(dados=dados).transforma_em_planilha()

except Exception as ex:
    print(ex)
