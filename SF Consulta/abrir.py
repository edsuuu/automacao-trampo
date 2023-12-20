from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time 
import openpyxl

caminho_arquivo = r'C:\Users\edson.dasilva.ext\Documents\github\automacao-trampo\SF Consulta\Consulta.xlsx'

wb = openpyxl.load_workbook(caminho_arquivo)

sheet = wb['SF_Consulta']

# Define os títulos para as colunas A e B
sheet['A1'] = 'CNPJ'
sheet['B1'] = 'Tem PDF?'

wb.save(caminho_arquivo)

driver = webdriver.Edge()

try:
    # Abre o site
    driver.get("https://sodexo360.lightning.force.com/one/one.app")

    time.sleep(5)

    for _ in range(5):
        pyautogui.press("tab") 

        pyautogui.press("enter")

    


finally:
    # Fecha o navegador ao final
    wb.close()
    driver.quit()