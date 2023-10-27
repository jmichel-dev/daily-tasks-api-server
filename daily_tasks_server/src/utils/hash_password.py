import bcrypt


def hashing(password: str, salt: bytes) -> str:
    password_hash = bcrypt.hashpw(bytes(password, "utf-8"), salt)
    return password_hash.decode("utf-8")


def check(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


def generate_password_salt() -> bytes:
    return bcrypt.gensalt()
