from selenium import webdriver
import time

# Função para abrir o site, rolar a página e fechar
def abrir_rolar_fechar_site(url, vezes):
    driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado
    driver.get(url)

    for i in range(vezes):
        time.sleep(2)  # Espera 2 segundos
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Rola a página até o final
        time.sleep(2)  # Espera mais 2 segundos
        driver.quit()  # Fecha o navegador
        driver = webdriver.Chrome()  # Abre o navegador novamente
        driver.get(url)

    driver.quit()

# URL do site que você deseja automatizar
url = "https://gazetamorena.com.br/"
# Quantidade de vezes que você deseja abrir e fechar o site
vezes = 3

abrir_rolar_fechar_site(url, vezes)
