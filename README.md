# Books API

## Overview
This a book CRUD API using Flask & MySQL. <br />
It is a swagger-enabled Flask server which uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+ <br />
pip3 <br />
If you don’t have them installed yet, install [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/)

## Cloning the repo
    git clone https://github.com/Yosr-Ch/books-api.git 

## Usage
To run the server, please execute the following from the root directory:

    pip3 install -r requirements.txt
    python3 -m swagger_server

and open your browser to here:

    http://localhost:8080/v2/ui/

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

    # running the app
    docker-compose up

    # stopping the app
    docker-compose stop
