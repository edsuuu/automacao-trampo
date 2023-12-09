import pyautogui
import time

#preencher outro forms
pyautogui.moveTo(2400, 501)
pyautogui.click()
time.sleep(1)
#copiar assunto
#mover pro vs code e clicar e copiar 
pyautogui.moveTo(3100, 115)
pyautogui.click()
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)
# #mover pro terminal e colar 
pyautogui.moveTo(2400, 525)
pyautogui.click()
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("tab")