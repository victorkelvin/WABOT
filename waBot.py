from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(10)

grupos=[' GRUPO TESTE #001',' GRUPO TESTE #002 ']
msg= 'MENSAGEM TESTE COM NEGRITOS,  e Link => https://www.instagram.com/escoladecosturar'

#copyable-text selectable-text
def buscar_grupo(grupo):
    campo_pesquisa= driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(0.5)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(grupo)
    time.sleep(1)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_msg(msg):
    campo_msg = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_msg[1].click
    time.sleep(0.5)
    campo_msg[1].send_keys(msg)
    time.sleep(5)
    campo_msg[1].send_keys(Keys.ENTER)

for grupo in grupos:
    buscar_grupo(grupo)
    enviar_msg(msg)
