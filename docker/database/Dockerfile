ARG PG_VERSION=15.3

FROM postgres:$PG_VERSION

COPY ./docker/database/create_todo_database.sql /docker-entrypoint-initdb.d/create_todo_database.sql


