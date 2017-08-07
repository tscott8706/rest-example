# rest-example

This is an example webserver backend that provides a RESTful API using Flask and
MongoDB.

## Installation

This application is run entirely within Docker containers.  So a few Docker
tools will do the job.

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* docker build . --tag restexample:lastest

## Running
* Start: docker-compose up -d
* Stop: docker-compose down
* (in the future) The REST API can be retrieved from localhost:5000/api.
* Use your favorite tool to make REST requests or run the testing containers.

## Testing
* Unit testing: docker-compose -f docker-compose-unit-test.yml run --rm nosetests
* System testing: (tests not yet setup correctly) docker-compose -f docker-compose-system-test.yml up
