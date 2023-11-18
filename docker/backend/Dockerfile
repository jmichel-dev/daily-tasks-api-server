ARG APP_NAME=daily_tasks_server
ARG APP_PATH=/opt/$APP_NAME
ARG PYTHON_VERSION=3.11.4
ARG POETRY_VERSION=1.5.1

#
# Stage: staging
#
FROM python:$PYTHON_VERSION as staging
ARG APP_NAME
ARG APP_PATH
ARG POETRY_VERSION

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1
ENV \
    POETRY_VERSION=$POETRY_VERSION \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

# Import our project files
WORKDIR $APP_PATH
COPY ./poetry.lock ./pyproject.toml ./
COPY ./$APP_NAME ./$APP_NAME
RUN touch README.md

#
# Stage: development
#
FROM staging as development
ARG APP_NAME
ARG APP_PATH

# Install project in editable mode and with development dependencies
WORKDIR $APP_PATH
RUN poetry install

CMD ["poetry", "run", "uvicorn", "daily_tasks_server.main:app", "--reload"]

#
# Stage: production
#
FROM staging as production
ARG APP_NAME
ARG APP_PATH

WORKDIR $APP_PATH
RUN poetry install

ENV PORT=5000
ENV APP_NAME=$APP_NAME

CMD ["poetry", "run", "uvicorn", "--port", "5000", "daily_tasks_server.main:app"]
