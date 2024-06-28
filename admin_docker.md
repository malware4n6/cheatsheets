# Docker 101

- [Commands cheatsheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)
- [Setup](https://docs.docker.com/engine/install/ubuntu/)
- [Post install setup](https://docs.docker.com/engine/install/linux-postinstall/): `sudo groupadd docker; sudo usermod -aG docker $USER`

## Dockerfile

Copied from [here](https://www.delftstack.com/howto/docker/docker-create-directory/)
```text
    FROM - Creates a layer of the parent image/base image that will be used.
    WORKDIR - allows us to set the working directory.
    COPY - allows us to copy current directory contents into a directory in the container.
    PULL - Adds files from your Docker repository.
    RUN - Command to be executed when we want to build the image.
    CMD - specifies what command to run when the container starts.
    ENV - Defines environmental variables used during the build.
    ENTRYPOINT - specifies what command to run when the container starts.
    MAINTAINER - Specifies the author of the image.
```

## Run

```sh
docker build -t demo .

# list images
docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
demo   latest    c591b1c18a7a   25 seconds ago   152MB

# get one instance running
docker run -it demo bash
# as bash is specified, the CMD provided in Dockerfile is not taken into account
# -it: interactive + allocate a pseudo-tty

# the previous command didnt't run app.py because bash was specified, but it also forgets the option `-p`
docker run -it -p 8000:8000 demo

# find it
docker container ls
CONTAINER ID   IMAGE        COMMAND   CREATED              STATUS              PORTS     NAMES
b41891a2546d   demo   "bash"    About a minute ago   Up About a minute             naughty_pasteur
# docker ps show the same results
# docker ps -a also shows exited containers

# if we stop the container
docker container stop b41891a2546d
# we can restart it
docker container start b41891a2546d

# but to see the logs, we now need 
docker container logs b41891a2546d
# -> will show stdout 
```

## Volumes

```sh

docker volume create logs
logs

docker volume ls
DRIVER    VOLUME NAME
local     logs

docker volume inspect 
logs
[
    {
        "CreatedAt": "2024-06-27T15:32:49+02:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/logs/_data",
        "Name": "logs",
        "Options": null,
        "Scope": "local"
    }
]

# rerun the container with the volume mounted
docker run -it -p 8000:8000 -v logs:/logs demo

# we can access the data by using the Mountpoint
```

