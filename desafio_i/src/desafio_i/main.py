from .contact_register import ContactRegister
from .handlers import handle_add, handle_del, handle_list, handle_help


def main():
    #   First we need somewhere to store it.
    # Stack memory should work just fine for this Simple example.
    register = ContactRegister()

    #   Main Loop -------------------------------------------------------------
    while True:
        match input("  > "):
            case "1" | "add":
                # Receive input from stdin to register a new contact.
                handle_add(register)

            case "2" | "del":
                # Pass an arbitrary email to delete the contact from the list.
                handle_del(register)

            case "3" | "update":
                # TODO: Handle updating
                print("TODO")

            case "4" | "list":
                # Print every contact on the terminal.
                handle_list(register)

            case "help":
                # Show a nice help message for the user.
                handle_help()

            case "" | "quit" | "q" | "exit":
                # Just return safely from the main function.
                return

            case _:
                print(" Input not recognized.")

    # 󰑀  End of the main event loop --------------------------------------------


if __name__ == "__main__":
    main()
