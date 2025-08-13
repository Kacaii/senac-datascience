from dataclasses import dataclass


@dataclass
class Contact:
    """
      Represents a contact in our system.
    It should not be accessed directly.
    """

    name: str
    "  Name of the registred contact."
    phone: str
    "󱆫  Phone of the registred contact."
    email: str
    "󰛮  Email of the registred contact"

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, new_value):
        self.__dict__[key] = new_value


class ContactManager:
    """
    󰟀  Manager used for CRUD operation..
    Use its public methods to update its internal list.

    󰛌  All memory storing the internal list will be deallocated
    once the execution ends.

      This script uses stack memory only.
    """

    __list: list[Contact]
    "󰒡  Internal use only. It should not be accessed directly."

    def __init__(self) -> None:
        """
          Initialize the class using an empty list.
        Use its public methods to update it.
        """
        self.__list = []
        return

    def register_contact(self, contact: Contact) -> None:
        "  Appends a contact to the list."
        self.__list.append(contact)
        return

    def remove_contact(self, contact: Contact) -> None:
        "󰂭  Removes a contact from the list."
        self.__list.remove(contact)
        return

    def update_contact(self, contact: Contact, field: str, new_value: str) -> None:
        "󰚰  Updates a contact from the list."
        contact[field] = new_value
        return

    def get_contacts(self) -> list[Contact]:
        "󰆏  Returns a copy of its internal list."
        return self.__list.copy()
