from app.contact_manager import Contact, ContactManager


def test_contact_manager():
    """
    󰙨  Verify if the CRUD operations from the  ContactManager
    are working as expected.
    """

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
        "name": "wobble",
        "phone": "4321",
        "email": "wobble@wibble",
    }

    for field, new_value in updated_dict.items():
        contact = manager.get_contacts()[0]
        manager.update_contact(contact=contact, field=field, new_value=new_value)

        assert contact[field] == new_value

    #   Wibble is rmeoved from the list ---------------------------------------
    manager.remove_contact(wibble)
    assert 0 == len(manager.get_contacts())
    assert wibble not in manager.get_contacts()
