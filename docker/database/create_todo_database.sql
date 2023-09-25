CREATE TYPE TASK_STATUS AS ENUM ('FINISHED', 'DELETED', 'CANCELLED', 'PENDING', 'DOING');
CREATE TYPE TASK_PRIORITY AS ENUM ('LOW', 'NORMAL', 'HIGH');

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

CREATE TABLE IF NOT EXISTS role(
    id uuid DEFAULT gen_random_uuid()  PRIMARY KEY,
    role VARCHAR(30)  NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS person_roles(
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    person_id uuid not null,
    role_id uuid not null,
    FOREIGN KEY (person_id) REFERENCES person(id),
    FOREIGN KEY (role_id) REFERENCES role(id)
);

CREATE TABLE IF NOT EXISTS tokens(
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    token VARCHAR NOT NULL,
    valid BOOL DEFAULT true,
    created_at timestamp default CURRENT_TIMESTAMP not null,
    updated_at timestamp default CURRENT_TIMESTAMP not null
);

CREATE TABLE IF NOT EXISTS project(
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description VARCHAR,
    created_at timestamp default CURRENT_TIMESTAMP not null,
    updated_at timestamp default CURRENT_TIMESTAMP not null,
    owner_id uuid not null,
    FOREIGN KEY (owner_id) REFERENCES person(id)
);

CREATE TABLE IF NOT EXISTS task(
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description VARCHAR,
    status TASK_STATUS NOT NULL DEFAULT 'PENDING',
    priority TASK_PRIORITY NOT NULL DEFAULT 'NORMAL',
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    project_id uuid NOT NULL,
    FOREIGN KEY (project_id) REFERENCES project(id)
);