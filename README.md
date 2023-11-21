# Daily Tasks backend server

A simple API HTTP server for managing daily projects and tasks.

## Running on development mode

- Copy the env.example file to env.dev
```console
cp env.example env.dev
``` 

- Replace the values on the env.dev file accordingly to your development environment
```
APP_VERSION=1.0.0

DATABASE_USER=todo
DATABASE_NAME=todo
DATABASE_PASSWORD=smartway
DATABASE_HOST=localhost
DATABASE_PORT=5432

PASSWORD_HASH=<replace here>

JWT_SECRET=<replace here>
JWT_ALGORITHM=<replace here>
JWT_EXPIRATION_TIME_IN_SECONDS=3600
JWT_REFRESH_TOKEN_EXPIRATION_IN_DAYS=7
JWT_ACCESS_TOKEN_EXPIRATION_IN_MINUTES=5

EMAIL_HOST=<replace here>
EMAIL_PORT=<replace here>
EMAIL_LOGIN=<replace here>
EMAIL_PASSWORD=<replace here>
EMAIL_SENDER=notifications@example.com

AWS_REGION=<aws region>
AWS_ACCESS_KEY_ID=<aws access key id>
AWS_SECRET_ACCESS_KEY=<aws access key>
```

- Building and running the server
```console
docker compose -f docker-compose.dev.yaml --env-file .env.dev up --build
```
- Then you can access http://localhost:8000/docs to check if the server is running

## Running on production mode

- To run in production mode, you could follow the same steps as development mode, you just need to change the word "**dev**" to "**prod**"

Ex:
```console
docker compose -f docker-compose.prod.yaml --env-file .env.prod up --build
```

- The difference between dev and prod is that in development mode the server is running in hot reload. So, you are able to change your code and the FastAPI will automatically apply the changes

- In production mode, you can check if the server is running on http://localhost:5000/docs
