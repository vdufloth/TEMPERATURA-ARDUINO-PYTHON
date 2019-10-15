## Requirements:

* postgres version 10 was used
* Package postgresql-server-dev-10 to be installed on machine

### Postgresql CRUDS:

CREATE TABLE register (
 id serial PRIMARY KEY,
 datetime timestamp,
 temperature decimal,
 humidity decimal
);

