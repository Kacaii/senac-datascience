from .contact_register import ContactRegister
from .handlers import handle_add, handle_del


def main():
    #   First we need somewhere to store it.
    # Stack memory should work just fine for this Simple example.
    register = ContactRegister()

    #   Main Loop -------------------------------------------------------------
    while True:
        # TODO: Commands
        match input(" > "):
            case "1" | "add":
                handle_add(register)

            case "2" | "del":
                handle_del(register)

            case "3" | "update":
                # TODO: Handle updating
                print("TODO")

            case "4" | "list":
                # TODO: Use a handler
                print(register.get_contacts())

            case "help":
                # TODO: Help message
                print("TODO")

            case "":
                # If your press enter: 󰌑
                # Just return safely from the main function.
                return

            case _:
                print(" Input not recognized.")

    # 󰑀  End of the main event loop --------------------------------------------


if __name__ == "__main__":
    main()
