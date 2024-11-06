import tkinter as tk
from tkinter import scrolledtext
import os

class Gantt:
    def __init__(self, master):
        self.master = master
        master.title("Gráfico Gantt")
        master.configure(bg='black')

        title_frame = tk.Frame(master, bg='#2e2e2e', bd=0)
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text="Gráfico Gantt", bg='#2e2e2e', fg='white')
        title_label.pack(padx=10, pady=5)

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.NONE, width=100, height=30, bg='#2e2e2e', fg='white',relief="flat", bd=0)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(master, orient="horizontal", command=self.text_area.xview)
        scrollbar.pack(side="bottom", fill="x")
        
        self.text_area.config(xscrollcommand=scrollbar.set)

        self.text_area.tag_configure("io", foreground="#FF1493")
        
        self.carregar_resultados()
        self.integrantes_label = tk.Label(master, text="INTEGRANTES: \n-> Nathan Dantas Mendes: 24.122.041-7\n-> Ana Beatriz de Souza: 24.122.018-5\n-> Luísa Graça Barbado: 24.122.058-1", bg='black', fg='white')
        self.integrantes_label.pack(pady=5)

        self.last_size = 0
        self.check_for_updates()

    def carregar_resultados(self):
        self.text_area.delete(1.0, tk.END)
        try:
            with open("grafico.txt", "r") as file:
                conteudo = file.readlines()

            for linha in conteudo:
                if "I/O" in linha:
                    start_idx = 0
                    while start_idx < len(linha):
                        start_idx = linha.find("I/O", start_idx)
                        if start_idx == -1:
                            break
                        self.text_area.insert(tk.END, linha[:start_idx])
                        self.text_area.insert(tk.END, "I/O", "io")
                        linha = linha[start_idx + 3:]
                        start_idx = 0
                    self.text_area.insert(tk.END, linha)
                else:
                    self.text_area.insert(tk.END, linha)
                self.text_area.see(tk.END)
        except FileNotFoundError:
            self.check_for_updates()

    def check_for_updates(self):
        try:
            current_size = os.path.getsize("grafico.txt")
            if current_size != self.last_size:
                self.last_size = current_size
                self.carregar_resultados()
            self.master.after(1000, self.check_for_updates)
        except:
            self.check_for_updates()
