




all: .init




.init: 
	@echo "PASSWORD root :";
	@read PostgresPWD; \
	echo "$$PostgresPWD"  | tr -d '\n' | cat > ./srcs/secrets/secretsPostGres_Password ;\
	read -p "userName for db : " userName; \
	read -p "mdp for db : " userPassword; \
	cat srcs/sqlInit/sqlInitBDD.txt > srcs/data-test/sqlInitBDD.txt; \
	echo "\nCREATE USER $$userName WITH ENCRYPTED PASSWORD '$$userPassword';" >> srcs/data-test/sqlInitBDD.txt; \
	echo "GRANT ALL PRIVILEGES ON DATABASE principal_db TO $$userName;" >> srcs/data-test/sqlInitBDD.txt
	sudo docker compose up -d



	@touch .init;

	
createDB:
	@sudo docker exec bdd-db-1 psql -c "CREATE DATABASE principal_db OWNER root;"
	@sudo docker exec bdd-db-1 psql -f /var/lib/postgresql/sqlInitBDD.txt principal_db
	@sudo docker exec bdd-db-1 rm -rf /var/lib/postgresql/sqlInitBDD.txt



fclean: 
	@rm -rf ./srcs/secrets/secretsPostGres_Password
	@sudo docker compose down
	@rm -rf .init; \
	sudo rm -rf ./srcs/data-test; 
	@mkdir ./srcs/data-test/; 

cleanImages:
	@sudo docker rmi adminer:latest postgres:latest 

stop:
	@sudo docker compose stop

run: 
	@sudo docker compose start


	


