from datetime import datetime


class Entity:

    def __init__(self) -> None:
        self.__uid = None
        self.__created_at = None
        self.__updated_at = None

    def change_uid(self, uid: str) -> None:
        if not isinstance(uid, str):
            raise ValueError("Uid must be an string")
        self.__uid = uid

    @property
    def uid(self,) -> str:
        return self.__uid

    def change_created_at(self, created_at: datetime) -> None:
        if not isinstance(created_at, datetime):
            raise ValueError("You must provide created at as datetime object")
        self.__created_at = created_at

    @property
    def created_at(self) -> datetime | None:
        try:
            return self.__created_at
        except AttributeError:
            return None

    def change_updated_at(self, updated_at: datetime) -> None:
        if not isinstance(updated_at, datetime):
            raise ValueError("You must provide updated at as datetime object")
        self.__updated_at = updated_at

    @property
    def updated_at(self) -> datetime | None:
        try:
            return self.__updated_at
        except AttributeError:
            return None
