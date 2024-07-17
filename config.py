import os

API_ID = API_ID =  27665762

API_HASH = os.environ.get("API_HASH", "b2b6f18e1280f194b8f7349db4737eb9")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6746702961:AAHpksRXgLYM3A5zboILn0me-uUtVg813oU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7152249320))

LOG = -1002139865043,

# UPDATE_GRP = -1002140332321, # bot sat group

# auth_chats = [5219193259,1327415906]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7152249320").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


