import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))  
API_ID = int(os.environ.get('API_ID', ""))
API_HASH = os.environ.get('API_HASH', "")
BOT_TOKEN = os.environ.get('BOT_TOKEN', "")
OWNER_ID = int(os.environ.get('OWNER_ID', ""))
DATABASE_URL = os.environ.get('DATABASE_URL', "")
DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
MUST_JOIN = os.environ.get('MUST_JOIN', "")
