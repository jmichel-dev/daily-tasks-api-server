from psycopg2.extensions import connection

from fastapi import HTTPException, status

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.models.auth.login_request_response_model import LoginResponseModel, LoginRequestModel
from daily_tasks_server.src.services import GenerateAndSaveTokenService
from daily_tasks_server.src.services.auth.compare_user_password_service import CompareUserPasswordService
from daily_tasks_server.src.services.user.search_user_by_email import SearchUserByEmail
from daily_tasks_server.src.services.jwt.jwt_service import JWTService


class LoginUserController:

    @staticmethod
    def execute(login_request: LoginRequestModel, db: connection) -> LoginResponseModel:
        search_user_service = SearchUserByEmail(db)
        user = search_user_service.execute(login_request.email)

        compare_user_password_service = CompareUserPasswordService(db)
        valid_password = compare_user_password_service.execute(login_request.email, login_request.password)

        generate_and_save_token_service = GenerateAndSaveTokenService(db)

        if not valid_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email/password invalid"
            )

        token_payload = {
            "email": login_request.email
        }

        refresh_token = generate_and_save_token_service.execute(
            token_payload,
            Config.JWT_REFRESH_TOKEN_EXPIRATION
        )

        access_token = generate_and_save_token_service.execute(
            token_payload,
            Config.JWT_ACCESS_TOKEN_EXPIRATION
        )

        db.commit()

        return LoginResponseModel(
            refresh_token=refresh_token,
            access_token=access_token,
            user=user
        )
