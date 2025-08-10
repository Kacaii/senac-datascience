from .contact_register import ContactRegister, Contact


def handle_add(register: ContactRegister):
    "  Handler for registering contacts"
    name = input("  Input your name:\n > ")
    phone = input("󰘂  Input your phone:\n > ")
    email = input("󰛮  Input your email:\n >")

    contact = Contact(name=name, phone=phone, email=email)
    register.register_contact(contact)
