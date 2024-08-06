include .env
export

.PHONY: start
start:
	docker-compose up -d

.PHONY: stop
stop:
	docker-compose stop

.PHONY: build-image
build-image:
	docker build --platform linux/amd64 -t eggsbit-telegram-bot -f docker/Dockerfile .

.PHONY: tag-image
tag-image:
	docker tag eggsbit-telegram-bot registry.gitlab.com/eggsbit/eggsbit-telegram-bot/telegram-bot:$(APP_IMAGE_TAG)

.PHONY: push-image
push-image:
	docker push registry.gitlab.com/eggsbit/eggsbit-telegram-bot/telegram-bot:$(APP_IMAGE_TAG)

.PHONY: start
start-test:
	docker-compose -f deploy/docker-compose.test.yaml up -d
