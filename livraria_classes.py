"""
Classes para um sistema de biblioteca, podendo ser criado um usuário
e 4 tipos de livros, sendo um deles chamado Generico que é utilizado como
modelo para as heranças das outras 3
"""

class Usuario:
    """
    Cria um usuário com nome e senha pro sistema de livraria
    """
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def get_dados(self):
        """
        Retorna os dados formatados para guardar em um texto
        """
        return f"{self.nome}, {self.senha}"


class Generico:
    """
    Cria um livro generico, contendo nome, genero e preco, sendo genero e preco
    fixos
    """
    def __init__(self, nome):
        self.nome = nome
        self.genero = "Genérico"
        self.preco = 30

    def get_dados(self):
        """
        Retorna os dados formatados para guardar em um texto
        """
        return f"{self.nome}, {self.genero}"


class Ficcao(Generico):
    """
    Classe filha da classe generico, alterando os valores de genero e preco
    """
    def __init__(self, nome):
        super().__init__(nome)
        self.genero = "Ficção"
        self.preco = 35


class NaoFiccao(Generico):
    """
    Classe filha da classe generico, alterando os valores de genero e preco
    """
    def __init__(self, nome):
        super().__init__(nome)
        self.genero = "Não Ficção"
        self.preco = 25


class Tecnico(Generico):
    """
    Classe filha da classe generico, alterando os valores de genero e preco
    """
    def __init__(self, nome):
        super().__init__(nome)
        self.genero = "Técnico"
        self.preco = 40
