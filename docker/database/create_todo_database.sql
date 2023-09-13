CREATE TYPE TODO_STATUS AS ENUM ('FINISHED', 'DELETED', 'CANCELLED', 'PENDING', 'DOING');
CREATE TYPE TODO_PRIORITY AS ENUM ('LOW', 'NORMAL', 'HIGH');

CREATE TABLE IF NOT EXISTS person(
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    first_name VARCHAR(80) NOT NULL,
    last_name VARCHAR(80) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    active_email BOOL DEFAULT false,
    enable BOOL DEFAULT true,
    created_at timestamp default CURRENT_TIMESTAMP not null,
    updated_at timestamp default CURRENT_TIMESTAMP not null
);

CREATE TABLE IF NOT EXISTS tokens(
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    token VARCHAR NOT NULL,
    valid BOOL DEFAULT true,
    created_at timestamp default CURRENT_TIMESTAMP not null,
    updated_at timestamp default CURRENT_TIMESTAMP not null
);

CREATE TABLE IF NOT EXISTS todo(
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    todo_title VARCHAR(150) NOT NULL,
    todo_description VARCHAR,
    todo_status TODO_STATUS NOT NULL DEFAULT 'PENDING',
    todo_priority TODO_PRIORITY NOT NULL DEFAULT 'NORMAL',
    created_at timestamp default CURRENT_TIMESTAMP not null,
    updated_at timestamp default CURRENT_TIMESTAMP not null,
    owner_id uuid not null,
    FOREIGN KEY (owner_id) REFERENCES person(id)
);