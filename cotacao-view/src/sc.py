from selenium import webdriver
import time

def abrir_rolar_fechar_site(url, vezes):
    driver = webdriver.Chrome()
    driver.get(url)

    for i in range(vezes):
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        driver.quit() 
        driver = webdriver.Chrome()  
        driver.get(url)

    driver.quit()

url = "https://gazetamorena.com.br/"
vezes = 3

abrir_rolar_fechar_site(url, vezes)
