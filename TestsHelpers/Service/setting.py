from ..TestsUtils.config import CONFIG
from os import getenv

data = CONFIG["place4play"]
URL = data["scheme"] + "://"+ data["host"] + ":"+ data["port"] + data["basePath"]