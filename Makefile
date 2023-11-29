
PG_COMPOSE_FILE=postgres/compose_pg.yml
PG_DB_NAME=test_database
PG_USER=postgres

MYSQL_COMPOSE_FILE=mysql/compose_mysql.yml

MONGO_COMPOSE_FILE=mongo/compose_mongo.yml

.PHONY: pg_up mongo_up

up: pg_up mysql_up mongo_up

pg_up:
	docker-compose -f $(PG_COMPOSE_FILE) up -d

pg_down:
	docker-compose -f $(PG_COMPOSE_FILE) down

# Remove the Postgres container and its volumes
pg_clean:
	docker-compose -f $(PG_COMPOSE_FILE) down -v --remove-orphans

mysql_up:
	docker-compose -f $(MYSQL_COMPOSE_FILE) up -d

mysql_down:
	docker-compose -f $(MYSQL_COMPOSE_FILE) down -v --remove-orphans

mongo_up:
	docker-compose -f $(MONGO_COMPOSE_FILE) up -d

mongo_down:
	docker-compose -f $(MONGO_COMPOSE_FILE) down -v --remove-orphans

ps:
	docker ps

down: pg_down mysql_down mongo_down