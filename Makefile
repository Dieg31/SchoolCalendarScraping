.PHONY: build-dev run-dev build-prod run-prod

build-dev:
	docker-compose -f docker/docker-compose.dev.yml build

run-dev:
	docker-compose -f docker/docker-compose.dev.yml up -d
	docker exec -it scraperDev /bin/bash
