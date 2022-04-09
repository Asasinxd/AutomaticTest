from os import getenv

TIMEOUT = getenv('TIMEOUT')
if TIMEOUT == True:
    TIMEOUT = (10,10)
else:
    TIMEOUT = None
    

CONFIG = {
    "place4play": {
        "scheme": "https",
        "port": "443",
        "host": "place4play.herokuapp.com",
        "basePath": "/place4play/api"
    }
}