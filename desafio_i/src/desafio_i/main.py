from .contact_register import ContactRegister
from .handlers import handle_add


def main():
    register = ContactRegister()

    #   Main Loop
    while True:
        match input(" > "):
            case "1" | "add":
                handle_add(register)
            case "2" | "del":
                pass
            case "3" | "update":
                pass
            case "4" | "list":
                # TODO: Use a handler
                print(register.get_contacts())
            case "":
                return
            case _:
                print(" Input not recognized.")


if __name__ == "__main__":
    main()
