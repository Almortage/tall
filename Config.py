import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))
if ENVIRONMENT:
    
API_ID = int(os.environ.get('API_ID', None))
API_HASH = os.environ.get('API_HASH', None)
BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
OWNER_ID = int(os.environ.get('OWNER_ID', None)) 
DATABASE_URL = os.environ.get('DATABASE_URL', None)
DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = ""
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    MUST_JOIN = ""
    OWNER_ID = ""
