import json

from DTOs.Contact import Contact

from DataAccess.ContactDataAccess import ContactDataAccess
from DataAccess.ContactDataAccess_Dump import  addContact, updateContact, deleteContact

class ContactService:
    def getContacts(self):
        contactDataAccess = ContactDataAccess()
        return contactDataAccess.getContacts()

    def addContact(self, contact):
        # making the object# Parse JSON into an object with attributes corresponding to dict keys.
        #contact = json.loads(contact, object_hook=lambda d: SimpleNamespace(**d))
        contact = Contact(contact)
        
        contactDataAccess = ContactDataAccess()
        return contactDataAccess.addContact(contact)

    def updateContact(self, contact):
        contact = Contact(contact)
        
        contactDataAccess = ContactDataAccess()
        return contactDataAccess.updateContact(contact)

    def deleteContact(self, contactId):
        contactDataAccess = ContactDataAccess()
        return contactDataAccess.deleteContact(int(contactId))