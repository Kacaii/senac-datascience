from dataclasses import dataclass


@dataclass
class Contact:
    """
      Represents a contact in our system.
    It should not be accessed directly.
    """

    name: str
    """  Name of the registred contact."""
    phone: str
    """󱆫  Phone of the registred contact."""
    email: str
    """󰛮  Email of the registred contact"""

    def __setitem__(self, key, new_value):
        self[key] = new_value


class ContactRegister:
    """
    󰨇  System used for CRUD operation..
    Use its public methods to update its internal list.

    󰛌  All memory storing the internal list will be deallocated
    once the execution ends.

      This script uses stack memory only.
    """

    __list: list[Contact]
    """󰒡  Internal use only. It should not be accessed directly."""

    def __init__(self) -> None:
        """  Initialize the class using an empty list."""
        self.__list = []

    def register_contact(self, contact: Contact) -> None:
        self.__list.append(contact)

    def remove_contact(self, contact: Contact) -> None:
        self.__list.remove(contact)

    def update_contact(self, contact: Contact, field: str, new_value: str) -> None:
        contact[field] = new_value
        return

    def get_contacts(self) -> list[Contact]:
        """󰆏 Returns a copy of its internal list."""
        return self.__list.copy()
