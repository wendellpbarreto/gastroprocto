#!/bin/bash
#
#-----------------------------------
# @autor: Wendell P. Barreto
# @email: wendellp.barreto@gmail.com
# @project: gastroprocto
# @doc: restart_db.sh
# ----------------------------------


while true; do
    read -p "Are you using Linux (y or n)? " yn
    case $yn in
        [Yy]* )
        	sudo -u postgres psql -c 'DROP DATABASE gastroprocto_db'
			sudo -u postgres psql -c 'CREATE DATABASE gastroprocto_db'
			sudo -u postgres psql -c 'CREATE USER gastroprocto_admin'
            sudo -u postgres psql -c "ALTER USER gastroprocto_admin WITH PASSWORD 't1IUilS14,747we'"
			sudo -u postgres psql -c 'GRANT ALL PRIVILEGES ON DATABASE gastroprocto_db TO gastroprocto_admin'
			sudo -u postgres psql -d gastroprocto_db -c 'CREATE EXTENSION hstore'

			break;;
        [Nn]* )
			psql -c 'DROP DATABASE gastroprocto_db'
			psql -c 'CREATE DATABASE gastroprocto_db'
			psql -c 'CREATE USER gastroprocto_admin'
            psql -c "ALTER USER gastroprocto_admin WITH PASSWORD 't1IUilS14,747we'"
			psql -c 'GRANT ALL PRIVILEGES ON DATABASE gastroprocto_db TO gastroprocto_admin'
			psql -d gastroprocto_db -c 'CREATE EXTENSION hstore'

			break;;
        * ) echo "Please answer yes or no.";;
    esac
done

python manage.py syncdb
python manage.py collectstatic