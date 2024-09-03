import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

log_file = open("error_log.txt", "w")
sys.stderr = log_file

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-logging")

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def barra_de_preenchimento(total, intervalo=1):
    for i in range(1, total + 1):
        print(i, end='.')
        time.sleep(intervalo)
    print()

def imprimir_com_mensagem(mensagem):
    linha_superior = "█" * 30  
    linha_vazia = "█" + " " * 28 + "█"  
    mensagem_formatada = f"█{mensagem:^28}█"  

    print(linha_superior)
    print(linha_vazia)
    print(mensagem_formatada)
    print(linha_vazia)
    print(linha_superior)

def imprimir_erro(mensagem):
    linha_superior = "█" * 30  
    linha_vazia = "█" + " " * 28 + "█" 
    mensagem_formatada = f"█ ERRO: {mensagem:^16}█"  

    print(linha_superior)
    print(linha_vazia)
    print(mensagem_formatada)
    print(linha_vazia)
    print(linha_superior)

imprimir_com_mensagem("ABRINDO A APLICAÇÃO")

def abrir_links_dos_artigos(driver):
    artigos = None
    try:
        artigos = driver.find_elements(By.CSS_SELECTOR, 'article.wpr-grid-item')
    except Exception as e:
        imprimir_erro(str(e))
        return

    for artigo in artigos:
        try:
            link = artigo.find_element(By.CSS_SELECTOR, 'h2.wpr-grid-item-title a')
            link_url = link.get_attribute('href')
            driver.execute_script("window.open('" + link_url + "', '_blank');")
            time.sleep(2)
        except Exception as e:
            imprimir_erro(str(e))
            continue

num_ciclos = 50

for _ in range(num_ciclos):
    driver = webdriver.Edge()
    driver.get('https://gazetamorena.com/category/campogrande/')
    limpar_console()
    time.sleep(1)
    imprimir_com_mensagem("EXECUTANDO SEGUNDA VEZ")
    time.sleep(3)
    limpar_console()
    
    abrir_links_dos_artigos(driver)

    imprimir_com_mensagem("FECHANDO A APLICAÇÃO")
    time.sleep(2)

    limpar_console()

    driver.quit()

    time.sleep(1)
    limpar_console()

log_file.close()
