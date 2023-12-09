import tkinter as tk
import pyautogui
import time

def preencher_formulario():


    def mudar_cor_verde():
        botao_iniciar.config(bg="green")
        janela.update()

    def restaurar_cor_original():
        botao_iniciar.config(bg="SystemButtonFace")
        janela.update()

    data_assinatura = "18/07/2023"
    data_blindagem = "01/07/2023"

    def descer_seleção():
        pyautogui.press("down")
        pyautogui.press("enter")
        pyautogui.press("tab")

    def preencher_blindagem():
        #data de blindagem 
        pyautogui.write(data_blindagem) 
        pyautogui.press("tab")
        #meses de blindagem
        pyautogui.write("24")
        pyautogui.press("tab")

    def preencher_outro():
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

    num_zeros = int(entrada_zeros.get())

    time.sleep(2)

    mudar_cor_verde()

    for _ in range(num_zeros):
        #passando pelas taxas
        pyautogui.write("0")
        pyautogui.press("tab")

    #antecipaçao 
    pyautogui.write("1.5")
    pyautogui.press("tab")

    #pula as 9 linhas 

    for _ in range(11):
        pyautogui.write("0")
        time.sleep(0.1)
        pyautogui.press("tab")

    #tem blindagem 
    descer_seleção()

    preencher_blindagem()

    #n tem sub
    pyautogui.press("down")
    descer_seleção()

    #data de assinatura 
    pyautogui.write(data_assinatura)
    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(2)
    preencher_outro()
    time.sleep(1)
    descer_seleção()
    descer_seleção()

    restaurar_cor_original()

#interface gráfica
janela = tk.Tk()
janela.title("Auto-Forms")

janela.geometry("400x200")  # Largura x Altura

fonte = ("Arial", 13)
janela.option_add("*Font", fonte)

tk.Label(janela, text="1 para vale transporte").pack()
entrada_zeros = tk.Entry(janela)
entrada_zeros.pack()

botao_iniciar = tk.Button(janela, text="Iniciar Preenchimento", command=preencher_formulario)
botao_iniciar.pack()

janela.mainloop()