import re
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

            for div_filha in divs_filhas:
                print(div_filha.inner_text())
                secao = div_filha.locator('.elementor-section elementor-top-section elementor-element elementor-element-471232f elementor-section-content-middle elementor-section-boxed elementor-section-height-default elementor-section-height-default')
                div = secao.locator('.elementor-container elementor-column-gap-custom')
                div2 = div.locator('.elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-c8dea02')
                dados = div2.locator('.elementor-widget-wrap elementor-element-populated')
                razao_social = dados.locator('.elementor-heading-title elementor-size-default').inner_text()
                print('')

            print('')