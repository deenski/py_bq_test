.PHONY: docker.build docker.run

docker.build:
    docker build -t bq_test .

docker.run: docker.build
    docker run --rm -it -v $(shell pwd):/bq_test -e GOOGLE_APPLICATION_CREDENTIALS=/bq_test/creds.json bq_test
