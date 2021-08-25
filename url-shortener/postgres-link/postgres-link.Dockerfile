FROM postgres:12.2-alpine

COPY ./postgres-link/init_database.sql /docker-entrypoint-initdb.d