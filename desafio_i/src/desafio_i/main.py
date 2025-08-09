from typing import TypedDict


class Pessoa(TypedDict):
    nome: str
    telefone: str
    email: str


def main():
    # Utilizaremos esta string para guardar os valores.
    contatos: list[Pessoa] = []

    match input(" > "):
        case "1" | "add":
            pass
        case "2" | "del":
            pass
        case "3" | "update":
            pass


if __name__ == "__main__":
    main()
