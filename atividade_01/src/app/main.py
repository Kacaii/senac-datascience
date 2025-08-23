from .contact_manager import ContactManager
from .handlers import handle_add, handle_del, handle_list, handle_help, handle_update
import os


def main():
    #   First we need somewhere to store it.
    # Stack memory should work just fine for this simple example.
    manager = ContactManager()

    #   Useful from making separators.
    terminal_columns = os.get_terminal_size().columns

    # Print help on first interaction
    handle_help()

    #   Main event loop -------------------------------------------------------------

    while True:
        print("-" * terminal_columns)
        match input("  > "):
            case "1" | "add" | "new":
                # Receive input from stdin to register a new contact.
                handle_add(contact_manager=manager)

            case "2" | "del" | "remove":
                # Pass an arbitrary email to delete the contact from the list.
                handle_del(contact_manager=manager)

            case "3" | "update":
                handle_update(contact_manager=manager)

            case "4" | "list" | "l":
                # Print every contact on the terminal.
                handle_list(contact_manager=manager)

            case "help" | "h":
                # Show a nice help message for the user.
                handle_help()

            case "" | "quit" | "q" | "exit":
                # Just return safely from the main function.
                return

            case _:
                # Unsupported input.
                print(" Input not recognized.")

    # 󰑀  End of the main event loop --------------------------------------------


if __name__ == "__main__":
    main()
