from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.services.user.search_user_by_email import SearchUserByEmail
from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.services.jwt.jwt_service import JWTService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[DatabaseInterface, Depends(DatabaseSession)]
) -> UserResponseModel:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate your credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = JWTService.verify(token)
        email = payload["payload"]["email"]

    except JWTError:
        raise credentials_exception

    with db.get_session() as session:
        search_user_by_email_service = SearchUserByEmail(session)
        return search_user_by_email_service.execute(email)


def get_current_active_user(
    current_user: Annotated[UserResponseModel, Depends(get_current_user)]
) -> UserResponseModel:
    if not current_user.enable:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive user")

    return current_user
