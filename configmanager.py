import json

CONFIG_FILE = "config/config.json"

ADDRESS = "address"
USER = "user"
PASSWORD = "password"
SERVER = "server"

config = None


def _load(email, filepath=CONFIG_FILE):
    """ get key from json """
    global config
    try:
        with open(filepath, "r") as config_file:
            config = json.load(config_file)
    except FileNotFoundError as FNFE:
        print(f"_load|KO|the file '{filepath}' does not exist")
        return False
    else:
        config = config.get(email)
        if config:
            print(f"_load|OK|mail '{email}' found in file '{filepath}'")
            return True
        else:
            print(f"_load|KO|mail '{email}' NOT found in file '{filepath}'")
            return False


def get_config_pretty(email, filepath=CONFIG_FILE):
    if _load(email, filepath):
        return json.dumps(config, indent=4)
    return None


def get_config(email, filepath=CONFIG_FILE):
    if _load(email, filepath):
        return config
    return None


def get_user(email, filepath=CONFIG_FILE):
    if _load(email, filepath):
        return get_config(email).get(USER)
    return None


def get_password(email, filepath=CONFIG_FILE):
    if _load(email, filepath):
        return get_config(email).get(PASSWORD)
    return None


def get_server(email, filepath=CONFIG_FILE):
    if _load(email, filepath):
        return get_config(email).get(SERVER)
    return None
