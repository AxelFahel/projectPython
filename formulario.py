# -*- coding: utf-8 -*-
"""Formulario.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WptfcAp0Bv25KENwZDulXgQgw7IMUXAv
"""

pip install db-sqlite3

import tkinter as tk
from tkinter import messagebox
import sqlite3

class FerramentaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Ferramenta de Cadastro")

        # Conectar ao banco de dados SQLite (ou crie um novo)
        self.conn = sqlite3.connect('cadastro.db')
        self.c = self.conn.cursor()

        # Criar tabela de usuários se não existir
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                rede_social TEXT,
                telefone TEXT,
                endereco TEXT
            )
        ''')
        self.conn.commit()

        # Componentes da interface
        self.label_nome = tk.Label(root, text="Nome:")
        self.entry_nome = tk.Entry(root)

        self.label_email = tk.Label(root, text="E-mail:")
        self.entry_email = tk.Entry(root)

        self.label_senha = tk.Label(root, text="Senha:")
        self.entry_senha = tk.Entry(root, show="*")

        self.label_rede_social = tk.Label(root, text="Rede Social:")
        self.entry_rede_social = tk.Entry(root)

        self.label_telefone = tk.Label(root, text="Telefone:")
        self.entry_telefone = tk.Entry(root)

        self.label_endereco = tk.Label(root, text="Endereço:")
        self.entry_endereco = tk.Entry(root)

        self.btn_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_usuario)

        # Posicionamento dos componentes
        self.label_nome.grid(row=0, column=0, sticky="e", pady=10)
        self.entry_nome.grid(row=0, column=1, pady=10)

        self.label_email.grid(row=1, column=0, sticky="e", pady=10)
        self.entry_email.grid(row=1, column=1, pady=10)

        self.label_senha.grid(row=2, column=0, sticky="e", pady=10)
        self.entry_senha.grid(row=2, column=1, pady=10)

        self.label_rede_social.grid(row=3, column=0, sticky="e", pady=10)
        self.entry_rede_social.grid(row=3, column=1, pady=10)

        self.label_telefone.grid(row=4, column=0, sticky="e", pady=10)
        self.entry_telefone.grid(row=4, column=1, pady=10)

        self.label_endereco.grid(row=5, column=0, sticky="e", pady=10)
        self.entry_endereco.grid(row=5, column=1, pady=10)

        self.btn_cadastrar.grid(row=6, column=0, columnspan=2, pady=10)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        rede_social = self.entry_rede_social.get()
        telefone = self.entry_telefone.get()
        endereco = self.entry_endereco.get()

        # Verificar se todos os campos estão preenchidos
        if not nome or not email or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios.")
            return

        try:
            # Inserir dados na tabela de usuários
            self.c.execute("INSERT INTO usuarios (nome, email, senha, rede_social, telefone, endereco) VALUES (?, ?, ?, ?, ?, ?)",
                           (nome, email, senha, rede_social, telefone, endereco))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso.")
            self.limpar_campos()
        except sqlite3.IntegrityError:
            messagebox.showwarning("Aviso", "E-mail já cadastrado. Escolha outro e-mail.")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_rede_social.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_endereco.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FerramentaCadastro(root)
    root.mainloop()

import sqlite3
import getpass  # Módulo para ocultar a senha durante a entrada

class FerramentaCadastro:
    def __init__(self):
        # Conectar ao banco de dados SQLite (ou crie um novo)
        self.conn = sqlite3.connect('cadastro.db')
        self.c = self.conn.cursor()

        # Criar tabela de usuários se não existir
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                rede_social TEXT,
                telefone TEXT,
                endereco TEXT
            )
        ''')
        self.conn.commit()

    def cadastrar_usuario(self):
        nome = input("Digite o nome: ")
        email = input("Digite o e-mail: ")
        senha = getpass.getpass("Digite a senha: ")
        rede_social = input("Digite a rede social (opcional): ")
        telefone = input("Digite o telefone (opcional): ")
        endereco = input("Digite o endereço (opcional): ")

        try:
            # Inserir dados na tabela de usuários
            self.c.execute("INSERT INTO usuarios (nome, email, senha, rede_social, telefone, endereco) VALUES (?, ?, ?, ?, ?, ?)",
                           (nome, email, senha, rede_social, telefone, endereco))
            self.conn.commit()
            print("Usuário cadastrado com sucesso.")
        except sqlite3.IntegrityError:
            print("E-mail já cadastrado. Escolha outro e-mail.")

    def listar_usuarios(self):
        self.c.execute("SELECT * FROM usuarios")
        usuarios = self.c.fetchall()
        for usuario in usuarios:
            print(usuario)

if __name__ == "__main__":
    cadastro = FerramentaCadastro()

    # Exemplo de cadastro de usuário
    cadastro.cadastrar_usuario()

    # Exemplo de listar todos os usuários
    cadastro.listar_usuarios()