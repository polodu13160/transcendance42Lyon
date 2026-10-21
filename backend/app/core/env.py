from dotenv import load_dotenv
load_dotenv()

import os
DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError(".env is not good")
