#!/bin/bash
set -e

echo "If encounter error, please delete the keycloack-db container then delete postgres_data volume"
# CREATE TABLE AND USER FOR API-DB
mysql -v ON_ERROR_STOP=1 --username "$MYSQL_USER" --dbname "$MYSQL_DB" <<-EOSQL
    CREATE USER '$MYSQL_DB_API_USER'@'localhost' IDENTIFIED BY '$MYSQL_DB_API_PASSWORD';
    CREATE DATABASE $MYSQL_DB_API;
    GRANT ALL PRIVILEGES ON DATABASE $MYSQL_DB_API TO $MYSQL_DB_API_USER@'localhost';
EOSQL

echo "Finished init new table with its auth for API database."

