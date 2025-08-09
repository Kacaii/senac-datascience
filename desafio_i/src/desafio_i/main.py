from .sistema_de_cadastro import SistemaDeCadastro


def main():
    sistema = SistemaDeCadastro()

    # TODO: Interface do programa
    match input(" > "):
        case "1" | "add":
            pass
        case "2" | "del":
            pass
        case "3" | "update":
            pass


if __name__ == "__main__":
    main()
