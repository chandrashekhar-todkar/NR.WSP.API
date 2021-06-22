import logging, json

import azure.functions as func
from Services.ContactService import ContactService

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python DeleteContact function processed a request.')

    try:
        contactId = req.route_params.get('id')
    except ValueError:
        pass

    contactService = ContactService()
    data = contactService.deleteContact(contactId)
    return func.HttpResponse(json.dumps(data), headers={"content-type" : "application/json"})