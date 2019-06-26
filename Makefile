PROJECT_NAME=gitinfo

# Common

all: run

run:
	@docker-compose up

stop:
	@docker-compose stop

down:
	@docker-compose down
