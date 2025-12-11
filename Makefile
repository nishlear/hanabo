up:
	docker-compose -p discordbot -f docker/docker-compose.yml up -d

down:
	docker-compose -p discordbot -f docker/docker-compose.yml down

run:
	make down && make up

build:
	docker build -t discord-bot .