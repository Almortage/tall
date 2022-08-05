import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', "8964162"))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', "5297963487"))
    except ValueError:
        raise Exception("Your OWNER_ID is not a valid integer.")
    DATABASE_URL = os.environ.get('DATABASE_URL', )
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = "8964162"
    API_HASH = "57fd71da68029890610ade3b62017472"
    BOT_TOKEN = "5545299580:AAEUMfHOJQAl4c10kYpCNfDw1YByiTgcU04"
    DATABASE_URL = ""
    MUST_JOIN = "YY8GG"
    OWNER_ID = "5297963487"
