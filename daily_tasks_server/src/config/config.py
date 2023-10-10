import os
from datetime import datetime, timedelta
from dotenv import load_dotenv


load_dotenv()


class Config:
    APP_HOST = "localhost"
    APP_API_ROUTE = "/api"

    CORS_ORIGIN_ALLOWED = ["*"]
    CORS_CREDENTIALS = True
    CORS_METHODS_ALLOWED = ["*"]
    CORS_HEADERS_ALLOWED = ["*"]

    PASSWORD_SALT = bytes(os.getenv("PASSWORD_HASH", "changeme"), "utf-8")
    PASSWORD_MIN_LENGTH = 8

    DATABASE_USER = os.getenv("DATABASE_USER", "todo")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "todo")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "smartway")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = os.getenv("DATABASE_PORT", 5432)

    JWT_SECRET = os.getenv("JWT_SECRET", "secret")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_TIME_IN_SECONDS = int(os.getenv("JWT_EXPIRATION_TIME_IN_SECONDS", 30))
    JWT_ACTIVATE_EMAIL_TOKEN_EXPIRATION = datetime.utcnow() + timedelta(seconds=JWT_EXPIRATION_TIME_IN_SECONDS)
    # REFRESH TOKEN EXPIRATION CONFIG
    JWT_REFRESH_TOKEN_EXPIRATION_IN_DAYS = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRATION_IN_DAYS", 1))
    JWT_REFRESH_TOKEN_EXPIRATION = datetime.utcnow() + timedelta(days=JWT_REFRESH_TOKEN_EXPIRATION_IN_DAYS)
    # ACCESS TOKEN EXPIRATION CONFIG
    JWT_ACCESS_TOKEN_EXPIRATION_IN_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRATION_IN_MINUTES", 1))
    JWT_ACCESS_TOKEN_EXPIRATION = datetime.utcnow() + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRATION_IN_MINUTES)
    JWT_CLAIMS = {
        "exp": datetime.utcnow() - timedelta(seconds=JWT_EXPIRATION_TIME_IN_SECONDS)
    }

    EMAIL_HOST = os.getenv("EMAIL_HOST", "localhost")
    EMAIL_PORT = int(os.getenv("EMAIL_PORT", 2525))
    EMAIL_LOGIN = os.getenv("EMAIL_LOGIN", "user")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "password")
    EMAIL_SENDER = os.getenv("EMAIL_SENDER", "notifications@example.com")

    MAIL_TEMPLATE_ACTIVATE_USER_EMAIL = os.getcwd() + "/src/templates/active_user_email.html"
    MAIL_TEMPLATE_REQUEST_PASSWORD_EMAIL = os.getcwd() + "/src/templates/change_password_request.html"
