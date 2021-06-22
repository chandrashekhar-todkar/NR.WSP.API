import datetime

def default(o):
    if isinstance(o, (datetime.datetime, datetime.date)):
        return o.isoformat()
