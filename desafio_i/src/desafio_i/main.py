from .sistema_de_cadastro import ContactRegister


def main():
    system = ContactRegister()

    #   Main Loop
    while True:
        match input(" > "):
            case "1" | "add":
                pass
            case "2" | "del":
                pass
            case "3" | "update":
                pass
            case "4" | "list":
                print(system.get_contacts())
            case "":
                return
            case _:
                print(" Input not recognized.")


if __name__ == "__main__":
    main()
