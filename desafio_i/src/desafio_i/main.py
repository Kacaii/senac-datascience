from .sistema_de_cadastro import SistemaDeCadastro


def main():
    sistema = SistemaDeCadastro()

    #   Loop de execução principal.
    while True:
        match input(" > "):
            case "1" | "add":
                pass
            case "2" | "del":
                pass
            case "3" | "update":
                pass
            case "":
                return
            case _:
                print(" Comando não reconhecido")


if __name__ == "__main__":
    main()
