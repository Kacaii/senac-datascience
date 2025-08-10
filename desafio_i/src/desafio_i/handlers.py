from .contact_register import ContactRegister, Contact


def handle_add(register: ContactRegister):
    name = input("name")
    phone = input("phone")
    email = input("email")

    contact = Contact(name=name, phone=phone, email=email)
    register.register_contact(contact)
