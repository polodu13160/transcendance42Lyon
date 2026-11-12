from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError(".env is not good : : DATABASE_URL is required")

CLIENT_ID = os.environ.get("CLIENT_ID")
if not CLIENT_ID:
    raise ValueError(".env is not good : CLIENT_ID is required")

CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
if not CLIENT_SECRET:
    raise ValueError(".env is not good : CLIENT_SECRET is required")
GRANT_TYPE = os.environ.get("GRANT_TYPE")
if not GRANT_TYPE:
    raise ValueError(".env is not good : GRANT_TYPE is required")
ENVIRONMENT = os.environ.get("ENVIRONMENT")
if not ENVIRONMENT:
    raise ValueError(".env is not good : ENVIRONMENT is required")
