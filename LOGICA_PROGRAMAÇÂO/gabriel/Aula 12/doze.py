import tkinter as tk
from tkinter import messagebox

def bemvindo():
    # .get() serve para buscar o texto da caixa
    nome_usuario = usuario_nome.get()

    if nome_usuario == "":
        messagebox.showerror("!","por favor digite seu nome :)")
    else:
        messagebox.showinfo("Bem vindo", f"Olá {nome_usuario} você tem {usuario_idade} anos")

#|janela
janela_bemvindo = tk.Tk()
janela_bemvindo.title("Saudações Do Usuario")
janela_bemvindo.geometry("1000x1000")
janela_bemvindo.configure(bg= "#696565")


# Componentes

# Labels
lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome :)")
lbl_mensagem_usuario.grid(row=0, column=0, pady=10,padx=10)

lbl_mensagem_idade = tk.Label(janela_bemvindo, text="Digite sua idade :)")
lbl_mensagem_idade.grid(row=1, column=0, pady=10,padx=10)

# Entrys
usuario_nome = tk.Entry(janela_bemvindo, font = ("Arial", 12))
usuario_nome.grid(row=0, column=1, pady=10,padx=10)

usuario_idade = tk.Entry(janela_bemvindo, font = ("Arial", 12))
usuario_idade.grid(row=1, column=1, pady=10,padx=10)


#botão
btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar mensagens", command = bemvindo)
btn_enviar_mensagem.grid(row=0, column=3, pady=10, padx=10)


btn_fechar = tk.Button(janela_bemvindo, text="fechar o mundo", command=janela_bemvindo.destroy )
btn_fechar.grid(row = 4, column=0,pady=10,padx=10)





# Rodar interface
janela_bemvindo.mainloop()

