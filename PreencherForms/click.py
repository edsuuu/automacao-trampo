import pyautogui
import time


def iniciaVarias():
    pyautogui.moveTo(2150, 905) #INICIA
    pyautogui.click()
    pyautogui.moveTo(3350, 605) #INICIA 2 
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(2400, 955)
    pyautogui.click() # escolhe a rainha
    pyautogui.moveTo(2250, 565)
    pyautogui.click() # coloca

    pyautogui.moveTo(2050, 815)
    pyautogui.click() # render

    pyautogui.moveTo(2980, 615)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(2880, 915)
    pyautogui.click()

def quantidadees():
    quantide = 20
    for i in range(quantide): 
        iniciaVarias()
        print(i + 1)
        time.sleep(2)
        
quantidadees()
        
