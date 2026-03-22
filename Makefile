SHELL := /bin/bash

.PHONY: install install-dev test run docker-build docker-test

install:
	./scripts/ubuntu/install.sh

install-dev:
	./scripts/ubuntu/install-dev.sh

test:
	./scripts/ubuntu/test.sh

run:
	./scripts/ubuntu/run.sh

docker-build:
	docker build -f docker/build.Dockerfile -t python-template-build .

docker-test:
	docker build -f docker/test.Dockerfile -t python-template-test .
	docker run --rm python-template-test
