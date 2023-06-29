# App Database (App DB)

This repo serves as a python backend to the database for the AU5k Production application.

## Docker Setup
Currently we are running the database in a docker container. Installing and running the container can be done with one command in the terminal:

``` bash
docker run -p 127.0.0.1:3306:3306  --name mdb -e MARIADB_ROOT_PASSWORD=Password123! -d mariadb:latest
```

Now the container should be running at `localhost` on port 3306 with the password `Password123!` with the container name `mdb`. You can check the status of all container in the terminal by running the command:

``` bash
docker ps -a
```

To restart the container, you can run the following:

``` bash
docker container restart CONTAINER_NAME
```
