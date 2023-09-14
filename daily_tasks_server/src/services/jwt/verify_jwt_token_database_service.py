from fastapi import HTTPException, status


class VerityJWTTokenDatabaseService:

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def execute(self, token: str) -> None:

        sql = "SELECT valid FROM tokens WHERE token = %s"
        data = (token,)

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        output = cursor.fetchone()
        if output is None or len(output) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Could not find the token in the resource!"
            )

        enabled = output[0]
        cursor.close()

        if not enabled:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The token is not valid!"
            )
