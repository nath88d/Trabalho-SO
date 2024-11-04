import tkinter as tk
from tkinter import scrolledtext
import os

class Saida:
    def __init__(self, master):
        self.master = master
        master.title("Saída do Escalonador Round Robin")
        master.configure(bg='black')

        title_frame = tk.Frame(master, bg='#2e2e2e', bd=0)
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text="Saída do Escalonador Round Robin", bg='#2e2e2e', fg='white')
        title_label.pack(padx=10, pady=5)

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=30, bg='#2e2e2e', fg='white')
        self.text_area.pack(padx=10, pady=10)

        self.text_area.tag_configure("fila", foreground="yellow")
        self.text_area.tag_configure("cpu", foreground="green")
        self.text_area.tag_configure("quantum", foreground="purple")
        self.text_area.tag_configure("chegada", foreground="orange")
        self.text_area.tag_configure("processos", foreground="#FF9999")
        self.text_area.tag_configure("asterisco", foreground="#87CEEB")
        self.text_area.tag_configure("operacao", foreground="#FF1493")
        self.text_area.tag_configure("encerrando", foreground="#8B0000")

        self.carregar_resultados()
        self.integrantes_label = tk.Label(master, text="INTEGRANTES: \n-> Nathan Dantas Mendes: 24.122.041-7\n-> Ana Beatriz de Souza: 24.122.018-5\n-> Luísa Graça Barbado: 24.122.058-1", bg='black', fg='white')
        self.integrantes_label.pack(pady=5)

        self.last_size = 0
        self.check_for_updates()

    def carregar_resultados(self):
        self.text_area.delete(1.0, tk.END)
        try:
            with open("saida.txt", "r") as file:
                conteudo = file.readlines()

            for linha in conteudo:
                if "OPERACAO" in linha:
                    self.text_area.insert(tk.END, linha, "operacao")
                elif "*" in linha:
                    self.text_area.insert(tk.END, linha, "asterisco")
                elif "FILA:" in linha:
                    self.text_area.insert(tk.END, linha, "fila")
                elif "CPU:" in linha:
                    self.text_area.insert(tk.END, linha, "cpu")
                elif "Quantum" in linha:
                    self.text_area.insert(tk.END, linha, "quantum")
                elif "CHEGADA" in linha:
                    self.text_area.insert(tk.END, linha, "chegada")
                elif "ENCERRANDO" in linha:
                    self.text_area.insert(tk.END, linha, "encerrando")
                elif "processos" in linha:
                    self.text_area.insert(tk.END, linha, "processos")
                else:
                    self.text_area.insert(tk.END, linha)
                self.text_area.see(tk.END)
        except FileNotFoundError:
            self.check_for_updates()

    def check_for_updates(self):
        try:
            current_size = os.path.getsize("saida.txt")
            if current_size != self.last_size:
                self.last_size = current_size
                self.carregar_resultados()
            self.master.after(1000, self.check_for_updates)
        except:
            self.check_for_updates()
