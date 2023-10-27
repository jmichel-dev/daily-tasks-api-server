from email_validator import validate_email, EmailNotValidError

from daily_tasks_server.src.entity import Entity
from daily_tasks_server.src.config import Config
from daily_tasks_server.src.utils import hash_password


class User(Entity):

    def __init__(self, ):
        super().__init__()
        self.__first_name = None
        self.__last_name = None
        self.__email = None
        self.__password = None
        self.__active_email = False
        self.__enable = True
        self.__password_salt = None

    def change_first_name(self, first_name: str) -> None:
        if not isinstance(first_name, str):
            raise ValueError("First name must be define as string")

        self.__first_name = first_name

    @property
    def first_name(self) -> str:
        return self.__first_name

    def change_last_name(self, last_name: str) -> None:
        if not isinstance(last_name, str):
            raise ValueError('Last name must be define as string')
        self.__last_name = last_name

    @property
    def last_name(self, ) -> str:
        return self.__last_name

    def change_email(self, email: str) -> None:
        try:
            email_info = validate_email(email, check_deliverability=False)
            self.__email = email_info.normalized
        except EmailNotValidError:
            raise ValueError("Email provided is not valid")

    @property
    def email(self, ) -> str:
        return self.__email

    def change_password_salt(self, password_salt: str | bytes) -> None:
        if not isinstance(password_salt, str) and not isinstance(password_salt, bytes):
            raise ValueError("Password salt must be typed as string or bytes")

        if isinstance(password_salt, str):
            self.__password_salt = bytes(password_salt, "utf-8")
        else:
            self.__password_salt = password_salt

    @property
    def password_salt(self) -> bytes:
        if not self.__password_salt or not isinstance(self.__password_salt, bytes):
            return hash_password.generate_password_salt()

        return self.__password_salt

    def encrypt_password(self, password: str) -> None:
        if not isinstance(password, str):
            raise ValueError('Password must be an string')
        elif len(password) < Config.PASSWORD_MIN_LENGTH:
            raise ValueError(f'Password requires more than {Config.PASSWORD_MIN_LENGTH} characters')

        self.__password = hash_password.hashing(password, self.password_salt)

    def encrypted_password(self, hashed_password: str) -> None:
        if not isinstance(hashed_password, str):
            raise ValueError('Password must be an string')

        self.__password = hashed_password

    @property
    def password(self) -> str:
        return self.__password

    def change_active_email(self, active_email: bool) -> None:
        self.__active_email = active_email

    @property
    def active_email(self) -> bool:
        return self.__active_email

    def activate_email(self) -> None:
        self.__active_email = True

    def change_enable(self, enable: bool) -> None:
        self.__enable = enable

    @property
    def enable(self) -> bool:
        return self.__enable

    def disable_user(self) -> None:
        self.__enable = False

    def enable_user(self) -> None:
        self.__enable = True
