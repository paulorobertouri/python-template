build:
	bash ./scripts/ubuntu/build.sh
SHELL := /bin/bash

.PHONY: install install-dev test run format lint docker-build docker-test
lint:
	bash ./scripts/ubuntu/lint.sh

install:
	./scripts/ubuntu/install.sh

install-dev:
	./scripts/ubuntu/install-dev.sh

test:
	./scripts/ubuntu/test.sh

run:
	./scripts/ubuntu/run.sh

format:
	bash ./scripts/ubuntu/format.sh

docker-build:
	docker build -f docker/build.Dockerfile -t python-template-build .

docker-test:
	docker build -f docker/test.Dockerfile -t python-template-test .
	docker run --rm python-template-test
