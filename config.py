import os
API_ID = int(os.getenv("API_ID", "5866979"))
API_HASH = os.getenv("API_HASH", "9182938d2e0eaac257c3a563ab0877a9")
BOT_TOKEN = os.getenv("BOT_TOKEN","1998209048:AAH_hGmeWZ7XZq76mbnX-CHRk7zRL3YhS6M")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "1518238620").split()})
