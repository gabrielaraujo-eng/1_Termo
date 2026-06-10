import tkinter as tk
from tkinter import messagebox


def janela_bemvindo():
    aluno = aluno_usuario.get()
    comunidade = comunidade_usuario.get()

    if aluno == "" and comunidade == "":
        messagebox.showwarning("Aviso", "Digite seu nome e sua categoria :)")
    else:
        messagebox.showinfo(
            "Bem-Vindo",
            f"Olá {aluno} ({comunidade}) - Seja bem-vindo ao sistema"
        )


def abrir_segunda_janela():
    janela_livros = tk.Toplevel(janela)
    janela_livros.title("LIVROS")
    janela_livros.geometry("400x300")
    janela_livros.configure(bg="black")

    tk.Label(janela_livros, text="Livro básico ou raro:", fg="white", bg="black").grid(row=0, column=0)

    livro_usuario = tk.Entry(janela_livros)
    livro_usuario.grid(row=0, column=1)

    def checar_livro():
        livro = livro_usuario.get()
        if livro == "":
            messagebox.showwarning("Aviso", "Digite básico ou raro")
        else:
            messagebox.showinfo("Sucesso", f"Livro '{livro}' selecionado!")

    tk.Button(janela_livros, text="Confirmar", command=checar_livro).grid(row=1, column=0, columnspan=2)


def taxa_renovacao():
    tempo = tempo_livro.get()

    if tempo == "":
        messagebox.showwarning("Aviso", "Digite o tempo de empréstimo")
    else:
        messagebox.showinfo("Taxa", "R$5,00 por dia extra após o prazo")


# JANELA PRINCIPAL
janela = tk.Tk()
janela.title("BIBLIOTECA COMUNITÁRIA")
janela.geometry("550x400")
janela.configure(bg="black")

tk.Label(janela, text="Nome:", fg="white", bg="black").grid(row=0, column=0)
tk.Label(janela, text="Categoria (Aluno/Comunidade):", fg="white", bg="black").grid(row=1, column=0)

aluno_usuario = tk.Entry(janela)
aluno_usuario.grid(row=0, column=1)

comunidade_usuario = tk.Entry(janela)
comunidade_usuario.grid(row=1, column=1)

tk.Button(janela, text="Mensagem", command=janela_bemvindo).grid(row=2, column=0)
tk.Button(janela, text="Abrir Biblioteca", command=abrir_segunda_janela).grid(row=3, column=0)

# JANELA TAXA (se quiser usar depois)
janela_taxa = tk.Toplevel(janela)
janela_taxa.title("Taxa de Renovação")
janela_taxa.geometry("400x200")

tk.Label(janela_taxa, text="Dias de empréstimo:").grid(row=0, column=0)

tempo_livro = tk.Entry(janela_taxa)
tempo_livro.grid(row=0, column=1)

tk.Button(janela_taxa, text="Calcular", command=taxa_renovacao).grid(row=1, column=0)

janela.mainloop()
