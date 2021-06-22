data = {
        "contacts":[
            {
                "Id" : 1,
                "FirstName" : "Jon",
                "LastName" : "Doe",
                "DOB" : "01/01/1980",
                "City" : "Los Angeles"
            },
            {
                "Id" : 2,
                "FirstName" : "Smith",
                "LastName" : "John",
                "DOB" : "01/01/1981",
                "City" : "New York"
            }
        ]
    }

def getContacts():
    return data["contacts"]

def addContact(contact):
    contact["Id"] = len(data["contacts"]) + 1
    data["contacts"].append(contact)

    return {
        "success" : True,
        "messages" : [{"type" : "information", "message" : "Contact added successful."}]
    }

def updateContact(contact):
    for i, cnt in enumerate(data["contacts"]):
        if cnt["Id"] == contact["Id"]:
            data["contacts"][i] = contact

    return {
        "success" : True,
        "messages" : [{"type" : "information", "message" : "Contact updated successful."}]
    }

def deleteContact(contactId):
    contatToRemove = '';

    for cnt in data["contacts"]:
        if cnt["Id"] == int(contactId):
            contatToRemove = cnt

    if cnt:
        data["contacts"].remove(contatToRemove)

    return {
        "success" : True,
        "messages" : [{"type" : "information", "message" : "Contact delete successful."}]
    }