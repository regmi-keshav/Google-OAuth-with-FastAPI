import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    GOOGLE_REDIRECT_URI = os.getenv('GOOGLE_REDIRECT_URI')
    DATABASE_URL = os.getenv('DATABASE_URL')
    SESSION_SECRET_KEY = os.getenv('SESSION_SECRET_KEY')


settings = Settings()
