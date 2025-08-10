from src.desafio_i.contact_manager import ContactManager, Contact


def test_contact_manager():
    manager = ContactManager()

    #   Manager start empty ---------------------------------------------------
    assert 0 == len(manager.get_contacts())

    #   Wibble is added successfully to the list. -----------------------------
    wibble = Contact(name="wibble", phone="1234", email="wibble@wobble")
    manager.register_contact(wibble)

    assert 1 == len(manager.get_contacts())
    assert wibble == manager.get_contacts()[0]

    #   Wibble is updated successfully ----------------------------------------
    updated_dict: dict[str, str] = {
        "name": "wooble",
        "phone": "4321",
        "email": "wobble@wibble",
    }

    for field, new_value in updated_dict.items():
        contact = manager.get_contacts()[0]
        manager.update_contact(contact=contact, field=field, new_value=new_value)

        assert contact[field] == new_value
