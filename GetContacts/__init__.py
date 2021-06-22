import logging, json
import azure.functions as func

from Common.Utility import default
from Services.ContactService import ContactService

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python GetContact function processed a request.')

    id = req.params.get('id')
    if not id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            id = req_body.get('id')

        contactService = ContactService()
        data = contactService.getContacts()
        return func.HttpResponse(json.dumps(obj=data, indent=4, default=default), headers={"content-type" : "application/json"})