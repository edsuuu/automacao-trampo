import tkinter as tk
import pyautogui
import time

def preencher_formulario():
    # Função para mudar a cor do botão para verde
    def mudar_cor_verde():
        botao_iniciar.config(bg="green")
        janela.update()

    # Função para restaurar a cor original do botão
    def restaurar_cor_original():
        botao_iniciar.config(bg="SystemButtonFace")
        janela.update()

    # Pegar o número de vezes que "0" deve ser inserido
    num_zeros = int(entrada_zeros.get())

    # Tempo de espera para você posicionar o cursor no campo de entrada
    time.sleep(2)

    # Chamar a função para mudar a cor do botão para verde antes da tarefa demorada
    mudar_cor_verde()

    # Inserir "0" no campo a quantidade de vezes especificada
    for _ in range(num_zeros):
        pyautogui.write("0")
        pyautogui.press("tab")

    # Executar a sequência de teclas após inserir os "0"
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.write("09/17/2020")
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.write("24")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.write("09/17/2020")
    time.sleep(1)
    pyautogui.press("tab")
    # pyautogui.press("enter")
    # time.sleep(3)
    # pyautogui.press("tab")
    # pyautogui.press("tab")
    # pyautogui.press("enter")
    # time.sleep(1)
    # pyautogui.press("tab")
    # pyautogui.press("tab")
    # pyautogui.write("ASSUNTO")
    # pyautogui.press("tab")
    # pyautogui.press("down")
    # pyautogui.press("enter")
    # pyautogui.press("tab")
    # pyautogui.press("down")
    # pyautogui.press("enter")
    # pyautogui.press("tab")


    # Chamar a função para restaurar a cor original do botão após a tarefa
    restaurar_cor_original()

# Configurar a interface gráfica
janela = tk.Tk()
janela.title("Automatização de Formulário")

# Definir largura e altura da janela
janela.geometry("400x200")  # Largura x Altura

# Aumentar o tamanho da letra da interface
fonte = ("Arial", 14)  # Definir fonte e tamanho
janela.option_add("*Font", fonte)

# Rótulo e entrada para o número de "0"s
tk.Label(janela, text="Número de 0s a inserir:").pack()
entrada_zeros = tk.Entry(janela)
entrada_zeros.pack()

# Botão para iniciar a automação
botao_iniciar = tk.Button(janela, text="Iniciar Automação", command=preencher_formulario)
botao_iniciar.pack()

# Iniciar a interface gráfica
janela.mainloop()