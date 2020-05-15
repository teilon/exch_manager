CREATE TABLE bank (
 id SERIAL PRIMARY KEY,
 name varchar(40) NOT NULL,
 adress varchar(40)
);
CREATE TABLE money_type (
 id SERIAL PRIMARY KEY,
 name varchar(15) NOT NULL
);
INSERT INTO money_type (name) VALUES ('наличные');
INSERT INTO money_type (name) VALUES ('безналичные');
CREATE TABLE currency (
 id SERIAL PRIMARY KEY,
 name varchar(5) NOT NULL
);
CREATE TABLE phone (
 id SERIAL PRIMARY KEY,
 bank_id integer references bank(id),
 phone_number varchar(20) NOT NULL
);
CREATE TABLE saturday (
 id SERIAL PRIMARY KEY,
 bank_id integer references bank(id),
 money_id integer references money_type(id),
 currency_id integer references currency(id),
 buy real,
 sale real,
 creation_date date NOT NULL DEFAULT CURRENT_DATE
);
CREATE TABLE saturday2 (
 id SERIAL PRIMARY KEY,
 bank_name varchar(60) NOT NULL,
 money_type varchar(15) NOT NULL
 currency_name varchar(5) NOT NULL
 buy real,
 sale real,
 creation_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);