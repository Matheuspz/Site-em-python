import tkinter as tk
from tkinter import messagebox
import os

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GLH - Cadastro")
        self.root.geometry("600x700")
        self.root.configure(bg="#9be2cc")

        # Header
        self.header_frame = tk.Frame(root, bg="#54c4a3", height=80)
        self.header_frame.pack(fill="x")
        self.header_frame.pack_propagate(False)
        
        # Logo no Header
        self.logo = tk.Label(self.header_frame, text="GLH", font=("Arial", 30, "bold"), bg="#54c4a3", fg="#000000")
        self.logo.pack(pady=(10, 10))

        # Título
        self.titulo = tk.Label(root, text="Crie Uma Conta Agora Mesmo.", font=("Arial", 18), bg="#9be2cc")
        self.titulo.pack(pady=(30, 10))

        # Subtítulo
        self.link_login = tk.Label(root, text="JÁ É REGISTRADO? FAÇA O LOGIN", font=("Arial", 10), bg="#9be2cc", cursor="hand2")
        self.link_login.pack(pady=5)
        self.link_login.bind("<Button-1>", self.abrir_login)


        # Frame para os campos de entrada
        frame = tk.Frame(root, bg="#9be2cc")
        frame.pack(pady=20)

        # Nome
        self.label_nome = tk.Label(frame, text="INSIRA SEU NOME COMPLETO", font=("Arial", 10), bg="#9be2cc")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nome = tk.Entry(frame, width=40, font=("Arial", 12), show="*")
        self.entry_nome.grid(row=1, column=0, padx=5, pady=5)

        # Email
        self.label_email = tk.Label(frame, text="INSIRA SEU EMAIL", font=("Arial", 10), bg="#9be2cc")
        self.label_email.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_email = tk.Entry(frame, width=40, font=("Arial", 12))
        self.entry_email.grid(row=3, column=0, padx=5, pady=5)

        # Senha
        self.label_senha = tk.Label(frame, text="INSIRA SUA SENHA", font=("Arial", 10), bg="#9be2cc")
        self.label_senha.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_senha = tk.Entry(frame, width=40, font=("Arial", 12), show="*")
        self.entry_senha.grid(row=5, column=0, padx=5, pady=5)

        # Data de Nascimento
        self.label_data_nasc = tk.Label(frame, text="INSIRA SUA DATA DE NASCIMENTO", font=("Arial", 10), bg="#9be2cc")
        self.label_data_nasc.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.entry_data_nasc = tk.Entry(frame, width=40, font=("Arial", 12))
        self.entry_data_nasc.grid(row=7, column=0, padx=5, pady=5)

        # Botão de Cadastro
        self.botao_cadastrar = tk.Button(root, text="Cadastre-se", command=self.enviar, font=("Arial", 14), bg="#2f9e81", fg="#ffffff")
        self.botao_cadastrar.pack(pady=20)

    def enviar(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        data_nasc = self.entry_data_nasc.get()

        if nome and email and senha and data_nasc:
            messagebox.showinfo("Cadastro Realizado", "Cadastro realizado com sucesso!")
            self.entry_nome.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_senha.delete(0, tk.END)
            self.entry_data_nasc.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos")

    def abrir_login(self, event):
        self.root.destroy()
        os.system("py login.py")

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()
