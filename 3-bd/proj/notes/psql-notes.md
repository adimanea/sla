# PostgreSQL Notes

## Installation and Startup
Best Linux setup: see **Juba, Volkov - Learning PostgreSQL 11 2019, pages 55-57**.

- Setup environment variables in `~/.bashrc`:
```sh
export PGROOT="/var/lib/postgres"
export PGDATA="/var/lib/postgres/data"
export PGHOST="localhost"
export PGPORT="5432"
export PGLOG="/var/log/postgres"
```
- Check the `postgresql.conf` (search for it with `locate` or `find / -name postgresql.conf`) configuration file to accept `localhost`:
```sh
# postgresql.conf
listen_address = '*'
```

- The owner of the `$PGROOT` directory is `postgres`! So switch to that user:
```sh
$ sudo su - postgres
```

- Initialize database (after logging in as `postgres`):
```sh
initdb --locale en_US.UTF-9 -D /var/lib/postgres/data
```

Whenever needed, check the status of the `postgresql.service`:
```sh
systemctl status postgresql
systemctl restart postgresql
systemctl enable postgresql
```

**Create a role and database for current user!!**, it will be much better. See the commands:
```sql
alter user {username};
alter role {give him superuser etc};
```
Then at the command line, initialize a database with his name: `createdb {username}`.

See also [here](https://www.a2hosting.com/kb/developer-corner/postgresql/managing-postgresql-databases-and-users-from-the-command-line).

## Create and delete database
Create a database with:
```sql
create database test;
-- uppercase works as well
CREATE DATABASE test;
```

List the current databases with `\l` under `psql`.

After creating, enter the database (connect to it) with `psql {db_name}`, i.e. `psql test` or connect from within `psql` by entering `\c {db_name}`, i.e. `\c test`.

To delete the database, enter:
```sql
drop database test;
```

## Create table
General syntax:
```sql
create table table_name (
    column name + data type + constraints
)
```

Example:
```sql
create table person (
    id int,
    first_name varchar(50),
    last_name varchar(50),
    gender varchar(6),
    date_of_birth timestamp, -- INCLUDES H:M:S
    -- simpler
    date_of_birth date,
)
```

View created tables or entries with `\d`, so for example:
```sql
\d -- shows whole table
\d person -- shows the fields of person
```

### Create table with constraints
To impose certain constraints to a table created, you can write, for example:
```sql
create table person (
    id bigserial not null primary key,
    -- bigserial = increments by itself
    -- primary key = uniquely identifies the person
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    gender varchar(5) not null,
    date_of_birth date not null,
    email varchar(150),
);
```

You can `drop` the table and create the new one which contains the constraints.

When listing the new table, you get:
```
List of relations
    Schema |     Name      |   Type   |  Owner
   --------+---------------+----------+----------
    public | person        | table    | postgres
    public | person_id_seq | sequence | postgres
(2 rows)
```

Note that `person_id_seq` is due to the primary key, which is `id`:
```
                        Table "public.person"
    Column     |          Type          | Collation | Nullable |              Default
---------------+------------------------+-----------+----------+------------------------------------
 id            | bigint                 |           | not null | nextval('person_id_seq'::regclass)
 first_name    | character varying(50)  |           | not null |
 last_name     | character varying(50)  |           | not null |
 gender        | character varying(7)   |           | not null |
 date_of_birth | date                   |           | not null |
 email         | character varying(150) |           |          |

Indexes: "person_pkey" PRIMARY KEY, btree (id)
```

The command `\dt` shows only the tables, without the relation, so it drops the `person_id_seq`.

## Insert records
Example:
```sql
insert into person (
    first_name,
    last_name,
    gender,
    date_of_birth)
values ('Anne', 'Smith', 'FEMALE', DATE '1988-01-09');
```
Note that the example above *does not* contain email, since it is allowed to be null. Another example is:
```sql
insert into person (
    first_name,
    last_name,
    gender,
    date_of_birth,
    email)
values ('Jake', 'Jones', 'MALE', date '1990-01-10', 'jake@gmail.com');
```
Query to see what you inserted with:
```sql
select * from person
```

### Generate 1000 rows with `Mockaroo`
[Link](https://mockaroo.com/).

Generate `sql` file, then load it with `\i {FILE}`.

## Basic operations
### Select
To query the database for a certain entry, use `select`.
Example:
```sql
select * from person where first_name = 'Jones';
-- this shows all entries for the result
-- if you want to just show its name, use:
select first_name, last_name from person where first_name = 'Jones';
```
### Order
Sort from the table:
```sql
select * from person order by country_of_birth desc; -- descending order
```
You can also choose multiple criteria to sort:
```sql
select * from person order by id, email asc;
-- sorted by id first, then email
```

### Distinct
To show unique entries:
```sql
select distinct country_of_birth from person order by country_of_birth;
-- shows only one entry for each country
```

### `where` clause and `and`
Example:
```sql
select * from person where gender = 'FEMALE';
select * from person where gender = 'FEMALE' and email is not null;
```


## Misc
- You can enter shell commands while in `psql` with `\!`, so for example clear screen with `\! clear`;
- You can personalize `psql` by editing `.psqlrc` for better prompt and error handling;


## JUBA & VOLKOV
The logical objects of PostgreSQL are organized in the server, which contains:
- template databases;
- databases;
- roles;
- tablespaces;
- settings;
- template procedural languages.

**Template databases** are the existing databases which you can see when installing PostgreSQL and which are cloned for your first example. The existing PostgreSQL Server templates are:
- `template1`, which is the default to be cloned;
- `template0`, which is a safeguard or version database that can be used for restoring corrupt data in `template1`. Note that unlike `template1`, this database does not contain encoding-specific or locale-specific data.

**User databases** are those created by the user. One can have as many databases as needed in a database cluster. The client which connects to the PostgreSQL server can access only the data in a single database, which is specified in the connection string. This means that data is not shared between databases.

The `\l` meta-command of `psql` shows the list of databases in the database cluster and the associate attributes. The privileges are the following:
- `CREATE` (`-C`): allows the specified role to create new schemas in the database;
- `CONNECT` (`-c`): when a role tries to connect to a database, the connect permissions are checked;
- `TEMPORARY` (`-T`): temporary tables are destroyed after the user session is terminated.

In general, when listing (`\l`), the privileges are represented like:
```
<user>=<privileges>/granted by
```
