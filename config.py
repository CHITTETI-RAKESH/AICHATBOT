import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask Security
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-this-secret-key"
    )

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///chatbot.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenAI
    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )

    # Session Security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False  # True in production with HTTPS
    SESSION_COOKIE_SAMESITE = "Lax"

    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = False

    # Upload Settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    UPLOAD_FOLDER = "uploads"

    # Chat Settings
    MAX_CHAT_HISTORY = 20

    # OpenAI Settings
    MODEL_NAME = "gpt-4o"

    TEMPERATURE = 0.7

    MAX_TOKENS = 1500

    # Application Settings
    APP_NAME = "AI Chatbot Pro"

    VERSION = "1.0.0"

    DEBUG = True
