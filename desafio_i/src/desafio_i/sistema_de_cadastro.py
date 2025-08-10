from dataclasses import dataclass


@dataclass
class Contato:
    """
      Representa um contato em nosso sistema.
    Não deve ser acessado diretamente.
    """

    nome: str
    """  Nome do contato cadastrado."""
    telefone: str
    """󱆫  Telefone do contato cadastrado."""
    email: str
    """󰛮  Email do contato cadastrado."""


class SistemaDeCadastro:
    """
    󰨇  Sistema utilizado para operações CRUD.
    Faça uso de seus métodos públicos para manipular sua lista interna.

    Esse programa usa apenas stack memory,
    toda a lista será apagada ao fim da execução do programa.
    """

    __lista: list[Contato]
    """󰒡  Apenas uso interno, não deve ser acessada diretamente,"""

    def __init__(self) -> None:
        self.__lista = []

    def cadastrar_contato(self, pessoa: Contato) -> None:
        self.__lista.append(pessoa)

    def remover_contato(self, pessoa: Contato) -> None:
        self.__lista.remove(pessoa)

    def listar_contatos(self) -> list[Contato]:
        """󰆏 Retorna uma cópia da lista interna."""
        return self.__lista.copy()
