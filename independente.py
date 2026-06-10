import tkinter as tk
from tkinter import messagebox, ttk

#1 criar configurações de janela
janela = tk.Tk()
janela.title = ("TESTE")
janela.geometry = ("400x400")
janela.configure(bg="#1e2938")

#defs

def saudação():
    nome = entry_nome.get()
    messagebox.showinfo(f"","Olá, {nome}")



# 3 
lbl_nome = tk.Label(janela, text="Qual é o seu nome?", font = ("Arial", 12), bg= "#1e2938", fg= "#ffffff")
entry_nome = tk.Entry(janela, font = ("Arial", 12))
btn_saudacao = tk.Button(janela,text="Saudação", bg="#22354f", command=saudação)

#4 onde fica posicionado (mais facil slk)
lbl_nome.grid(row=2, column=0, pady=10,padx=10)
entry_nome.grid(row=3, column=0, pady=10,padx=10)
btn_saudacao.grid(row=4, column=0, pady=10, padx=10)

# 5
janela.mainloop()
    