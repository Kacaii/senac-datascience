from .contact_register import ContactRegister, Contact


# HACK: You should probaly check if the email or phone is already registred.
def handle_add(register: ContactRegister) -> None:
    "  Handler for registering contacts"
    name = input("  Input your name:\n  > ")
    phone = input("󰘂  Input your phone:\n  > ")
    email = input("󰛮  Input your email:\n  > ")

    contact = Contact(name=name, phone=phone, email=email)
    register.register_contact(contact)


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
