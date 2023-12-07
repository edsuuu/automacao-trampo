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

    data_preenchida = "11/09/2023"

    def descer_seleção():
        pyautogui.press("down")
        pyautogui.press("enter")
        pyautogui.press("tab")

    def preencher_blindagem():
        #data de blindagem 
        pyautogui.write(data_preenchida) 
        pyautogui.press("tab")
        #meses de blindagem
        pyautogui.write("22")
        pyautogui.press("tab")

    num_zeros = int(entrada_zeros.get())

    time.sleep(2)

    mudar_cor_verde()

    for _ in range(num_zeros):
        #passando pelas taxas
        pyautogui.write("0")
        pyautogui.press("tab")

    #antecipaçao 
    pyautogui.write("0.6")
    pyautogui.press("tab")

    #pula as 9 linhas 

    for _ in range(9):
        pyautogui.write("0")
        time.sleep(0.1)
        pyautogui.press("tab")

    #tem blindagem 
    descer_seleção()
    
    #nao tem tem blindagem 
    # pyautogui.press("down")
    # pyautogui.press("down")
    # pyautogui.press("enter")
    # pyautogui.press("tab")

    preencher_blindagem()
    
    #tem subisidio
    descer_seleção()
    #subisio2
    pyautogui.press("tab")
    #subisio3
    pyautogui.press("tab")
    pyautogui.press("space")
    pyautogui.press("tab")

    #nao tem subisidio
    # pyautogui.press("down")
    # pyautogui.press("down")
    # pyautogui.press("enter")
    # #subisio1
    # pyautogui.press("tab")

    #data de assinatura 
    pyautogui.write(data_preenchida)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)     
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)     
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(1)     
    pyautogui.write("SODEXO-PC-GSPAR ESTACIONAMENTOS LTDA - EPP-Stewart Motrico Prata-00731633-LAP")
    time.sleep(1)     

    pyautogui.press("tab")
    descer_seleção()
    descer_seleção()

    restaurar_cor_original()

#interface gráfica
janela = tk.Tk()
janela.title("Auto-Forms")

janela.geometry("400x200")  # Largura x Altura

fonte = ("Arial", 14)
janela.option_add("*Font", fonte)

tk.Label(janela, text="Limit 13 number").pack()
entrada_zeros = tk.Entry(janela)
entrada_zeros.pack()

botao_iniciar = tk.Button(janela, text="Iniciar Preenchimento", command=preencher_formulario)
botao_iniciar.pack()

janela.mainloop()