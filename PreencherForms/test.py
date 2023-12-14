import tkinter as tk
from tkinter import ttk
import pyautogui

def criar_botao_iniciar(janela):
    botao_iniciar = tk.Button(janela, text="Iniciar Preenchimento", command=automacao)
    botao_iniciar.pack(side=tk.BOTTOM, pady=10)

def automacao():
    def mudar_cor_verde():
        botao_iniciar.config(bg="green")
        janela.update()

    def restaurar_cor_original():
        botao_iniciar.config(bg="SystemButtonFace")
        janela.update()

    def descer_selecao_sim():
        pyautogui.press("down")
        pyautogui.press("enter")
        pyautogui.press("tab")

    def descer_selecao_nao():
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("enter")
        pyautogui.press("tab")

    def preencher_blindagem():
        # Substitua com os valores desejados ou obtenha esses valores de alguma forma
        data_assinatura = entrada_data.get()
        meses_blindagem = entrada_meses.get()

        # data de blindagem
        pyautogui.write(data_assinatura)
        pyautogui.press("tab")
        # meses de blindagem
        pyautogui.write(meses_blindagem)
        pyautogui.press("tab")

    def dropdown_select(event):
        selected_option = dropdown_var.get()

        # Verifica se os widgets já foram criados
        if selected_option == "Sim" and not hasattr(automacao, 'entrada_data'):
            # Criação dos widgets
            label_data_blindagem = tk.Label(janela, text="Data da Blindagem")
            label_data_blindagem.pack()

            entrada_data = tk.Entry(janela)
            entrada_data.pack()

            label_meses_blindagem = tk.Label(janela, text="Meses de Blindagem")
            label_meses_blindagem.pack()

            entrada_meses = tk.Entry(janela)
            entrada_meses.pack()

            # Associando as variáveis locais à função automacao
            automacao.entrada_data = entrada_data
            automacao.entrada_meses = entrada_meses
            automacao.label_data_blindagem = label_data_blindagem
            automacao.label_meses_blindagem = label_meses_blindagem
        elif selected_option == "Sim":
            # Destruição dos widgets existentes
            for widget in [automacao.entrada_data, automacao.entrada_meses, automacao.label_data_blindagem, automacao.label_meses_blindagem]:
                if widget:
                    widget.destroy()

            # Criação dos widgets
            label_data_blindagem = tk.Label(janela, text="Data da Blindagem")
            label_data_blindagem.pack()

            entrada_data = tk.Entry(janela)
            entrada_data.pack()

            label_meses_blindagem = tk.Label(janela, text="Meses de Blindagem")
            label_meses_blindagem.pack()

            entrada_meses = tk.Entry(janela)
            entrada_meses.pack()

            # Associando as variáveis locais à função automacao
            automacao.entrada_data = entrada_data
            automacao.entrada_meses = entrada_meses
            automacao.label_data_blindagem = label_data_blindagem
            automacao.label_meses_blindagem = label_meses_blindagem
        elif selected_option == "Não":
            # Destruição dos widgets existentes
            for widget in [automacao.entrada_data, automacao.entrada_meses, automacao.label_data_blindagem, automacao.label_meses_blindagem]:
                if widget:
                    widget.destroy()

    # Criação da janela principal
    janela = tk.Tk()
    janela.title("Automação Forms")
    janela.geometry("600x600")

    fonte = ("Arial", 12)
    janela.option_add("*Font", fonte)

    # Widgets
    tk.Label(janela, text="Blindagem").pack()
    dropdown_var = tk.StringVar()
    options = ["Sim", "Não"]
    dropdown = ttk.Combobox(janela, textvariable=dropdown_var, values=options, state="readonly")
    dropdown.set("Escolha uma opção")
    dropdown.bind("<<ComboboxSelected>>", dropdown_select)
    dropdown.pack(pady=10)

    criar_botao_iniciar(janela)

    # Inicializando as variáveis globais na função automacao
    automacao.entrada_data = None
    automacao.entrada_meses = None
    automacao.label_data_blindagem = None
    automacao.label_meses_blindagem = None

    janela.mainloop()

automacao()
