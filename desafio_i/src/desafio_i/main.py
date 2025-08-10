from .contact_register import ContactRegister
from .handlers import handle_add, handle_del, handle_list

HELP_MESSAGE = """
    Usage:

        1. add      󰆓  Add a contact to the list
        2. del      󰂭  Remove a contact from the list
        3. update   󰚰  Update a contact from the list.
        4. list       Print the list of contacts.

        press ENTER to quit 󰌑
    """


def main():
    #   First we need somewhere to store it.
    # Stack memory should work just fine for this Simple example.
    register = ContactRegister()

    #   Main Loop -------------------------------------------------------------
    while True:
        match input("  > "):
            case "1" | "add":
                handle_add(register)

            case "2" | "del":
                handle_del(register)

            case "3" | "update":
                # TODO: Handle updating
                print("TODO")

            case "4" | "list":
                handle_list(register)

            case "help":
                # Show a nice help message for the user.
                print(HELP_MESSAGE)

            case "" | "quit" | "q" | "exit":
                # Just return safely from the main function.
                return

            case _:
                print(" Input not recognized.")

    # 󰑀  End of the main event loop --------------------------------------------


if __name__ == "__main__":
    main()
