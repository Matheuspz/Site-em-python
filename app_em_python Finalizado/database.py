import sqlite3

def criar_tabela():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        data_nasc TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def inserir_usuario(nome, email, senha, data_nasc):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO usuarios (nome, email, senha, data_nasc)
    VALUES (?, ?, ?, ?)
    ''', (nome, email, senha, data_nasc))
    conn.commit()
    conn.close()

def verificar_credenciais(email, senha):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''
    SELECT * FROM usuarios WHERE email = ? AND senha = ?
    ''', (email, senha))
    usuario = c.fetchone()
    conn.close()
    return usuario is not None
