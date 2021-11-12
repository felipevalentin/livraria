"""
O programa tem como objetivo implementar um sistema de vendas de uma livraria, 
nela um usuário, que pode ser tanto um funcionário quanto um cliente, podem se 
cadastrar e logar. Após o login é possível o usuário consultar os livros disponíveis, 
verificando seu preço e gênero. Também é possível inserir novos livros, com um 
campo de nome e gênero. Por fim, o usuário pode comprar um livro. O programa se 
encerra quando a janela de Acesso ou de Menu são fechadas. Os dados de usuário e 
livros ficam armazenados num arquivo de texto.
"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from livraria_classes import Usuario, Generico, Ficcao, NaoFiccao, Tecnico

usuarios = []
livros = []

class Acesso:
    """
    Janela responsável pela janela de Acesso, a primeira janela de todas
    que dá acesso a Entrar e Registar, tem como atributos apenas um objeto
    que é o objeto tk.Tk()
    """
    def __init__(self, acesso):
        self.acesso = acesso
        self.acesso.title("Acesso")
        tk.Label(self.acesso, text="Livraria", font=("Arial Bold", 24)).grid()
        tk.Button(self.acesso, text='Entrar', width=30, height=2, command=self.login).grid()
        tk.Button(self.acesso, text='Registrar', width=30, height=2, command=self.registrar).grid()
        tk.Button(self.acesso, text='Sair', width=30, height=2, command=self.close_acesso).grid()

    def login(self):
        """
        Cria uma nova janela para entrar instanciando a classe Entrar
        """
        self.new_window = tk.Toplevel(self.acesso)
        Entrar(self.new_window, self.acesso)

    def registrar(self):
        """
        Cria uma nova janela para registrar instanciando a classe Registrar
        """
        self.new_window = tk.Toplevel(self.acesso)
        Registrar(self.new_window)

    def close_acesso(self):
        """
        Fecha a janela e sai do programa
        """
        self.acesso.quit()


class Entrar:
    """
    Janela responsável por entrar no menu, verifica se o usuário está cadastrado e caso estiver
    faz instância uma nova janela chamada Menu ao mesmo tempo que fecha as anteriores
    """
    def __init__(self, login, acesso):
        self.login = login
        self.login.title("Entrar")
        self.acesso = acesso
        tk.Label(self.login, text="Nome").grid()
        self.nome = tk.Entry(self.login, width=30)
        self.nome.grid()
        tk.Label(self.login, text="Senha").grid()
        self.senha = tk.Entry(self.login, width=30, show="*")
        self.senha.grid()
        tk.Button(self.login, text='Entrar', width=30, height=2, command=self.menu).grid()
        tk.Button(self.login, text='Retornar', width=30, height=2, command=self.close_login).grid()

    def menu(self):
        """
        Verifica informações das caixas de Entry e caso usuário estiver cadastrado
        cria uma nova janela, e entao instância um objeto da classe Menu. Ao mesmo
        tempo fecha a janela de acesso, saindo da primeira parte do programa
        """
        for usuario in usuarios:
            if (usuario.nome == self.nome.get()
                    and usuario.senha == self.senha.get()):
                self.new_window = tk.Tk()
                self.acesso.destroy()
                Menu(self.new_window, usuario)
                break
        else:
            tk.Tk().withdraw()
            messagebox.showerror(title="Erro", message="Usuário não encontrado!")

    def close_login(self):
        """
        Apenas fecha a janela de login, retornando a tela de acesso
        """
        self.login.destroy()


class Registrar:
    """
    Janela responsável pelo cadastro, recebe informações de nome e senha e
    cria um novo usuário armazenando-o na lista de usuários
    """
    def __init__(self, registrar):
        self.registrar = registrar
        self.registrar.title("Registrar")
        tk.Label(self.registrar, text="Nome").grid()
        self.nome = tk.Entry(self.registrar, width=30)
        self.nome.grid()
        tk.Label(self.registrar, text="Senha").grid()
        self.senha = tk.Entry(self.registrar, width=30, show="*")
        self.senha.grid()
        tk.Button(self.registrar, text='Registrar', width=30, height=2, command=self.reg).grid()
        tk.Button(self.registrar, text='Retornar', width=30, height=2, command=self.close_registrar).grid()

    def reg(self):
        """
        recebe as informações inseridas nas caixas de Entry e cria um novo Usuário
        """
        nome = self.nome.get()
        senha = self.senha.get()
        usuario = Usuario(nome, senha)
        usuarios.append(usuario)
        tk.Tk().withdraw()
        messagebox.showinfo(title="Sucesso", message=f"Cliente cadastrado com sucesso!")
        self.close_registrar()

    def close_registrar(self):
        """
        Apenas fecha a janela de registrar, retornando a tela de acesso
        """
        self.registrar.destroy()


class Menu:
    """
    Janela responsável pelo uso do sistema, recebendo um usuário, que agora está logado,
    É possível acessar novas janelas para comprar, inserir e consultar os livros
    """
    def __init__(self, menu, usuario):
        self.menu = menu
        self.usuario = usuario
        self.menu.title("Menu")
        tk.Label(self.menu, text=f"Bem vindo {self.usuario.nome}!", font=("Arial Bold", 16)).grid()
        tk.Button(self.menu, text='Comprar', width=30, height=2, command=self.comprar).grid()
        tk.Button(self.menu, text='Inserir', width=30, height=2, command=self.inserir).grid()
        tk.Button(self.menu, text='Consultar', width=30, height=2, command=self.consultar).grid()
        tk.Button(self.menu, text='Sair', width=30, height=2, command=self.close_menu).grid()

    def comprar(self):
        """
        Cria uma nova janela para comprar instanciando a classe comprar
        """
        self.new_window = tk.Toplevel(self.menu)
        Comprar(self.new_window)

    def inserir(self):
        """
        Cria uma nova janela para inserir instanciando a classe inserir
        """
        self.new_window = tk.Toplevel(self.menu)
        Inserir(self.new_window)

    def consultar(self):
        """
        Cria uma nova janela para consultar instanciando a classe consultar
        """
        self.new_window = tk.Toplevel(self.menu)
        Consultar(self.new_window)

    def close_menu(self):
        """
        Fecha a janela e sai do programa
        """
        self.menu.quit()


class Comprar:
    """
    Janela responsável por comprar os livros, utilizando se de Combobox para 
    a seleção do livro
    """
    def __init__(self, comprar):
        self.comprar = comprar
        self.comprar.title("Comprar")
        self.cb = ttk.Combobox(self.comprar, width=30)
        self.cb['values'] = [f"{livro.nome} - {livro.genero} - R${livro.preco}" for livro in livros]
        self.cb.grid()
        tk.Button(self.comprar, text='Confirmar ', width=30, height=2, command=self.confirmar).grid()
        tk.Button(self.comprar, text='Retornar', width=30, height=2, command=self.close_comprar).grid()

    def confirmar(self):
        """
        Confirma a compra do livro verificando antes se o livro realmente existe
        , caso exista a compra é efuada e se retorna a janela de Menu
        """
        for livro in livros:
            if livro.nome in self.cb.get():
                tk.Tk().withdraw()
                messagebox.showinfo(title="Sucesso", message=f"Compra efetuada com successo: R${livro.preco}")
                livros.remove(livro)
                self.close_comprar()
                break
        else:
            tk.Tk().withdraw()
            messagebox.showerror(title="Erro", message="Livro não encontrado!")

    def close_comprar(self):
        """
        Apenas fecha a janela de Comprar, retornando a tela de Menu
        """
        self.comprar.destroy()


class Inserir:
    """
    Janela responsável por inserir novos livros, recebendo o nome e genero do livro 
    por meio de uma combobox
    """
    def __init__(self, inserir):
        self.inserir = inserir
        self.inserir.title("Inserir")
        tk.Label(self.inserir, text="Nome do Livro").grid()
        self.nome = tk.Entry(self.inserir, width=30)
        self.nome.grid()
        tk.Label(self.inserir, text="Gênero do Livro").grid()
        self.cb = ttk.Combobox(self.inserir, width=30)
        self.cb['values'] = ["Genérico", "Ficção", "Não Ficção", "Técnico"]
        self.cb.grid()
        tk.Button(self.inserir, text='Confirmar', width=30, height=2, command=self.confirmar).grid()
        tk.Button(self.inserir, text='Retornar', width=30, height=2, command=self.close_inserir).grid()

    def confirmar(self):
        """
        Confirma a inserção do livro criando uma instância do livro e 
        adiciona à lista de livros
        """
        genero = self.cb.get()
        livro = gerar_livro(self.nome.get(), genero)
        livros.append(livro)
        tk.Tk().withdraw()
        messagebox.showinfo(title="Sucesso", message=f"Livro inserido com sucesso!")
        self.close_inserir()

    def close_inserir(self):
        """
        Apenas fecha a janela de inserir, retornando a tela de Menu
        """
        self.inserir.destroy()


class Consultar():
    """
    Janela responsável por consultar livros disponíveis, listando-os
    """
    def __init__(self, consultar):
        self.consultar = consultar
        self.consultar.title("Consultar")
        tk.Label(self.consultar, text="Nome - Gênero - Preço")
        for livro in livros:
            tk.Label(self.consultar, text=f"{livro.nome} - {livro.genero} - R${livro.preco}").grid()
        tk.Button(self.consultar, text='Retornar', width=30, height=2, command=self.close_consultar).grid()

    def close_consultar(self):
        """
        Apenas fecha a janela de consultar, retornando a tela de Menu
        """
        self.consultar.destroy()

def gerar_livro(nome, genero):
    """
    Gera um livro baseado no genero dele, selecionando a classe correta
    """
    if genero == "Genérico":
        livro = Generico(nome)
    elif genero == "Ficção":
        livro = Ficcao(nome)
    elif genero == "Não Ficção":
        livro = NaoFiccao(nome)
    elif genero == "Técnico":
        livro = Tecnico(nome)
    return livro

def main():
	# Recebendo os dados armazenados no arquivo de texto usuários
    global usuarios
    global livros
    try:
	    usuarios_txt = open("usuarios.txt", "r")
	    for usuario in usuarios_txt.read().splitlines():
	        usuarios.append(Usuario(*usuario.split(", ")))
    except FileNotFoundError:
	    usuarios_txt = open("usuarios.txt", "w")
    usuarios_txt.close()


	# Recebendo os dados armazenados no arquivo de texto livros
    try:
	    livros_txt = open("livros.txt", "r")
	    for livro in livros_txt.read().splitlines():
		    livros.append(gerar_livro(*livro.split(", ")))
    except FileNotFoundError:
	    livros_txt = open("livros.txt", "w")
    livros_txt.close()
	
	# Cria a janela de acesso e insere instância a classe Acesso
    acesso = tk.Tk()
    app = Acesso(acesso)
    acesso.mainloop()   
    # Salva os usuários criados no arquivo de texto usuários
    usuarios_txt = open("usuarios.txt", "w")
    for usuario in usuarios:
        usuarios_txt.write(f"{usuario.get_dados()}\n")
    usuarios_txt.close()    
    # Salva os livros criados no arquivo de texto livros
    livros_txt = open("livros.txt", "w")
    for livro in livros:
        livros_txt.write(f"{livro.get_dados()}\n")
    livros_txt.close()  

if __name__ == '__main__':
    main()
