from .contact_register import ContactRegister, Contact


def handle_help() -> None:
    "󰂺  Handler for printing a help message on the terminal."

    HELP_MESSAGE = """
        Usage:

            1. add      󰆓  Add a contact to the list
            2. del      󰂭  Remove a contact from the list
            3. update   󰚰  Update a contact from the list.
            4. list       Print the list of contacts.

            press ENTER to quit 󰌑
        """

    print(HELP_MESSAGE)
    return


def handle_add(register: ContactRegister) -> None:
    """
      Handler for registering contacts.

      Verifies if the phone / email is already
    on the list before appending to it.
    """
    name = input("  Input your name:\n  > ")
    phone = input("󰘂  Input your phone:\n  > ")
    email = input("󰛮  Input your email:\n  > ")

    contact = Contact(name=name, phone=phone, email=email)

    # Check if it already exists.
    for registred_contact in register.get_contacts():
        if registred_contact["email"] == contact.email:
            print("Email already registred in the list, please use a different one.")
            return
        if registred_contact["phone"] == contact.phone:
            print("Phone already registred in the list, please use a different one.")
            return

    # 󰆓  Register the contact if everything goes well
    register.register_contact(contact)
    return


def handle_del(register: ContactRegister) -> None:
    "  Handler for removing contacts"
    email = input("󰛮  Input the email you would like to remove:\n  > ")

    updated_list: list[Contact] = list(
        filter(
            lambda contact: contact["email"] == email,
            register.get_contacts(),
        )
    )

    # Remove everyone that has this email.
    for contact in updated_list:
        register.remove_contact(contact)
    return


def handle_list(register: ContactRegister) -> None:
    "  Handler for print every contact on the terminal."
    for registred_contact in register.get_contacts():
        print(registred_contact)
    return
