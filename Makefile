infra:
	docker compose up -d postgres rabbitmq redis

up:
	docker compose up -d --build
