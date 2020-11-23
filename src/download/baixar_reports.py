from time import sleep
from typing import List
from src.util.util import *
from selenium import webdriver
from src.config.config import Config


class DownloadPDF:
    def __init__(self):

        self.__user = Config.get('powerbi', 'user')
        self.__pass = Config.get('powerbi', 'password')
        self.__driver = webdriver.Chrome('C:/Git/rpc/pbi-bot/chromedriver.exe')
        # self.__url = get_info('pbiself.__url', reports)

    def downloadReports(self, grupo:str):

        # print(os.path.dirname(os.path.realpath(__file__)))
        self.__driver.get('https://powerbi.microsoft.com')
        url = get_info('pbiurl', grupo)
        element = self.__driver.find_element_by_xpath("/html/body/nav/div/div[4]/ul[2]/li[1]/a")
        element.click()
        # E-mail
        sleep(10)
        element = self.__driver .find_element_by_xpath("//input[@name='loginfmt']")
        element.send_keys(self.__user)
        # Avançar
        element = self.__driver .find_element_by_id("idSIButton9")
        element.click()
        sleep(3)
        # Senha
        element = self.__driver.find_element_by_id("i0118")
        element.click()
        element.send_keys(self.__pass)
        # entrar
        element = self.__driver.find_element_by_id("idSIButton9")
        element.click()
        # Continuar Conectado - NÃO
        sleep(2)
        element = self.__driver .find_element_by_id("idBtn_Back")
        element.click()
        # maximiza janela
        self.__driver.maximize_window()

        for i in url:
            self.__driver.get(i)
            sleep(10)
            # abrir opções do menu exportar
            element = self.__driver.find_element_by_xpath("//span[.='Exportar']")
            element.click()
            sleep(2)
            # usar opção PDF
            element = self.__driver .find_element_by_xpath("//span[.='PDF']")
            element.click()
            sleep(10)
            # botão exportar
            element = self.__driver.find_element_by_css_selector(".primary")
            element.click()
            sleep(300)
            self.__driver.close()
