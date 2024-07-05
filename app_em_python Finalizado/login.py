import tkinter as tk
from tkinter import messagebox
from database import verificar_credenciais
import os

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GLH - Login")
        self.root.geometry("400x500")
        self.root.configure(bg="#9be2cc")

        # Header
        self.header_frame = tk.Frame(root, bg="#54c4a3", height=80)
        self.header_frame.pack(fill="x")
        self.header_frame.pack_propagate(False)

        # Logo no Header
        self.logo = tk.Label(self.header_frame, text="GLH", font=("Arial", 30, "bold"), bg="#54c4a3", fg="#000000")
        self.logo.pack(pady=(10, 10))

        # Frame para o conteúdo
        self.content_frame = tk.Frame(root, bg="#ffffff", bd=1, relief="solid")
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=300)

        # Título
        self.titulo = tk.Label(self.content_frame, text="LOGIN", font=("Arial", 18), bg="#ffffff")
        self.titulo.pack(pady=(20, 10))

        # Usuário
        self.label_usuario = tk.Label(self.content_frame, text="Email", font=("Arial", 10), bg="#ffffff")
        self.label_usuario.pack(pady=5, anchor="w", padx=20)
        self.entry_usuario = tk.Entry(self.content_frame, width=30, font=("Arial", 12), bg="#dcdcdc")
        self.entry_usuario.pack(pady=5)

        # Senha
        self.label_senha = tk.Label(self.content_frame, text="Senha", font=("Arial", 10), bg="#ffffff")
        self.label_senha.pack(pady=5, anchor="w", padx=20)
        self.entry_senha = tk.Entry(self.content_frame, width=30, font=("Arial", 12), show="*", bg="#dcdcdc")
        self.entry_senha.pack(pady=5)

        # Link para criar conta
        self.link_criar_conta = tk.Label(self.content_frame, text="Crie uma conta", font=("Arial", 10), bg="#ffffff", fg="#808080", cursor="hand2")
        self.link_criar_conta.pack(pady=10)
        self.link_criar_conta.bind("<Button-1>", self.abrir_cadastro)

        # Botão de Login
        self.botao_login = tk.Button(self.content_frame, text="Entrar", command=self.login, font=("Arial", 12), bg="#54c4a3", fg="#ffffff")
        self.botao_login.pack(pady=20)

    def login(self):
        email = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if email and senha:
            if verificar_credenciais(email, senha):
                messagebox.showinfo("Login", "Login realizado com sucesso!")
                self.entry_usuario.delete(0, tk.END)
                self.entry_senha.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Credenciais inválidas. Tente novamente.")
        else:
            messagebox.showwarning("Atenção", "Email e senha devem ser preenchidos")

    def abrir_cadastro(self, event):
        self.root.destroy()
        os.system("py cadastro.py")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
