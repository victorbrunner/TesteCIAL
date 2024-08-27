from Service.scraping_publilegal import ScrapingPublilegal

try:
    url = 'https://publilegal.diariodenoticias.com.br/'

    scraping_publilegal = ScrapingPublilegal(url=url)

    scraping_publilegal.get_pagina_principal()
except Exception as ex:
    print(ex)
