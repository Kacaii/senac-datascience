import pandas as pd
from .contact_manager import Contact, ContactManager


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


def handle_add(contact_manager: ContactManager) -> None:
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
    for registred_contact in contact_manager.get_contacts():
        if registred_contact["email"] == contact.email:
            print("Email already registred in the list, please use a different one.")
            return
        if registred_contact["phone"] == contact.phone:
            print("Phone already registred in the list, please use a different one.")
            return

    # 󰆓  Register the contact if everything goes well
    contact_manager.register_contact(contact=contact)
    return


def handle_del(contact_manager: ContactManager) -> None:
    "  Handler for removing contacts"

    email = input("󰛮  Input the email you would like to remove:\n  > ")

    updated_list: list[Contact] = list(
        filter(
            lambda contact: contact["email"] == email,
            contact_manager.get_contacts(),
        )
    )

    # Remove everyone that has this email.
    for contact in updated_list:
        contact_manager.remove_contact(contact)
    return


def handle_update(contact_manager: ContactManager) -> None:
    "󰚰  Handler for updating information about the contacts."

    email = input("󰛮  Input the email from the contact you like to update:\n  > ")

    # Return safely if empty input.
    if email == "":
        return

    updated_list: list[Contact] = list(
        filter(
            lambda contact: contact["email"] == email,
            contact_manager.get_contacts(),
        )
    )

    # Return if no contacts with that email were found.
    if len(updated_list) == 0:
        print("No contact was found with that email address:")
        return

    print("\n")
    handle_list(contact_manager=contact_manager)

    # Continue if you found a contact with the given address.
    print("  What information would you like to update?")
    print("  1. name")
    print("  2. phone")
    print("  3. email")

    target = input("\n  >  ")
    new_value = input("  Input the new value:\n  > ")

    match target:
        # Updating the name.
        case "1" | "name":
            for contact in updated_list:
                # Happy path
                contact_manager.update_contact(
                    contact=contact, field="name", new_value=new_value
                )
                return

        # Updating the phone number.
        case "2" | "phone":
            for contact in updated_list:
                # First check if it doesnt exist
                if contact["phone"] == new_value:
                    print(
                        "Phone already registred in the list, please use a different one."
                    )
                    return  # Return if found

                # Happy path ---------------------------------------------------
                contact_manager.update_contact(
                    contact=contact, field="phone", new_value=new_value
                )
                return  # 

        # Updating the email address.
        case "3" | "email":
            for contact in updated_list:
                # First check if it doesnt exist
                if contact["email"] == new_value:
                    print(
                        "Email already registred in the list, please use a different one."
                    )

                    return  # Return if found

                # Happy path ---------------------------------------------------
                contact_manager.update_contact(
                    contact=contact, field="email", new_value=new_value
                )
                return  # 

        case "":
            # Return safely if blank
            return

        case _:
            print("Unsuported field")
            return


def handle_list(contact_manager: ContactManager) -> None:
    "  Handler for print every contact on the terminal."

    contacts = contact_manager.get_contacts()

    # Only print if the list is not empty.
    if len(contacts) > 0:
        df = pd.DataFrame(contacts)
        print(df)
