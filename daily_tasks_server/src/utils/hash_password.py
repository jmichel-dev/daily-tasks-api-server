import bcrypt

from daily_tasks_server.src.config import Config


def hash_password(password: str) -> str:
    password_hash = bcrypt.hashpw(password.encode("utf-8"), Config.PASSWORD_SALT)
    return password_hash.decode("utf-8")


def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
