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

    num_zeros = int(entrada_zeros.get())

    # Tempo para clicar o no campo de entrada 
    time.sleep(2)

    # chamando a funçao para trocar a cor do botao
    mudar_cor_verde()

    for _ in range(num_zeros):
        #passando pelas taxas
        pyautogui.write("0")
        pyautogui.press("tab")

    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)

    #inserir a data da blindagem 
    #pyautogui.write("09/17/2020") 
    time.sleep(1)
    pyautogui.press("tab")
    #meses de blindagem 
    #pyautogui.write("24")
    pyautogui.press("tab")
    time.sleep(1)
    #subisidio se nao  tiver vai ter essa sequencia down, down, enter, tab
    #pyautogui.press("down")
    #pyautogui.press("down")
    #pyautogui.press("enter")
    #pyautogui.press("tab")
    #time.sleep(1)
    #pyautogui.write("09/17/2020")
    #time.sleep(1)
    #pyautogui.press("tab")
    #envio do furmulario 
    #pyautogui.press("enter")
    #time.sleep(3)
    #pyautogui.press("tab")
    #pyautogui.press("tab")
    #pyautogui.press("enter")
    #recaregando para mandar um novo preenchimento
    #time.sleep(1)
    #pyautogui.press("tab")
    #pyautogui.press("tab")
    #assunto para colocar para fazer o loop
    #pyautogui.write("ASSUNTOOOOOO")
    #pyautogui.press("tab")
    #pyautogui.press("down")
    #pyautogui.press("enter")
    #pyautogui.press("tab")
    #pyautogui.press("down")
    #pyautogui.press("enter")
    #passando pelas duas opcoes para selecionar
    #pyautogui.press("tab")

    #restaurando a cor d botao
    restaurar_cor_original()

#interface gráfica
janela = tk.Tk()
janela.title("Auto-Forms")

janela.geometry("400x200")  # Largura x Altura

fonte = ("Arial", 14)  # fonte e tamanho
janela.option_add("*Font", fonte)

tk.Label(janela, text="Limit 13 number").pack()
entrada_zeros = tk.Entry(janela)
entrada_zeros.pack()

botao_iniciar = tk.Button(janela, text="Iniciar Preenchimento", command=preencher_formulario)
botao_iniciar.pack()

janela.mainloop()