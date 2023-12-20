import tkinter as tk
from threading import Thread
import time
import pyautogui

class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Gráfica")

        self.label = tk.Label(root, text="")
        self.label.pack(pady=10)

        self.botao_iniciar = tk.Button(root, text="Iniciar Script", command=self.iniciar_script)
        self.botao_iniciar.pack(pady=20)

        self.botao_parar = tk.Button(root, text="Parar Script", command=self.parar_script, state=tk.DISABLED)
        self.botao_parar.pack(pady=20)

        self.executando = False
        self.thread = None

    def iniciar_script(self):
        if not self.executando:
            self.executando = True
            self.thread = Thread(target=self.executar_script)
            self.thread.start()

    def parar_script(self):
        self.executando = False
        self.botao_iniciar["state"] = tk.NORMAL
        self.botao_parar["state"] = tk.DISABLED

    def executar_script(self):
        self.atualizar_label("Script em execução...")
        self.botao_iniciar["state"] = tk.DISABLED
        self.botao_parar["state"] = tk.NORMAL

        time.sleep(5)

        pyautogui.press('left')
        pyautogui.press('left')

        pyautogui.keyDown('shift')

        total_iterations = 10000

        for i in range(total_iterations):
            if not self.executando:
                break

            pyautogui.press('down')


        pyautogui.keyUp('shift')

        if self.executando:
            self.atualizar_label("Script concluído.")
            self.botao_iniciar["state"] = tk.NORMAL
            self.botao_parar["state"] = tk.DISABLED
        else:
            self.atualizar_label("Script interrompido.")
            self.botao_iniciar["state"] = tk.NORMAL
            self.botao_parar["state"] = tk.DISABLED

    def atualizar_label(self, mensagem):
        self.label["text"] = mensagem
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    interface = InterfaceGrafica(root)
    root.mainloop()
