from typing import TypedDict


class Pessoa(TypedDict):
    """
      Representa um usuário em nosso sistema.
    Não deve ser acessado diretamente.
    """

    nome: str
    """  Nome do usuário cadastrado."""
    telefone: str
    """󱆫  Telefone do usuário cadastrado."""
    email: str
    """󰛮  Email do usuário cadastrado."""


class SistemaDeCadastro:
    """
    󰨇  Sistema utilizado para operações CRUD.
    Faça uso de seus métodos públicos para manipular sua lista interna.

    Esse programa usa apenas stack memory,
    toda a lista será apagada ao fim da execução do programa.
    """

    __lista: list[Pessoa]
    """󰒡  Apenas uso interno, não deve ser acessada diretamente,"""

    def __init__(self) -> None:
        self.__lista = []

    def cadastrar_usuario(self):
        # TODO:
        pass

    def remover_usuario(self):
        # TODO:
        pass

    def acessar_usuarios(self) -> list[Pessoa]:
        """󰆏 Retorna uma cópia da lista interna."""
        return self.__lista.copy()
