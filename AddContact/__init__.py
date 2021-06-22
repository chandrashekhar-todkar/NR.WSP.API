import logging, json

import azure.functions as func
from Services.ContactService import ContactService

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python AddContact function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass

    contactService = ContactService()
    data = contactService.addContact(req_body.get("contact"))
    return func.HttpResponse(json.dumps(data), headers={"content-type" : "application/json"})