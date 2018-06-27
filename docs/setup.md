# Getting Started

To deliver this workshop you will need at least one host with Docker installed.  To complete the clustered activities you will need at least 3 hosts.  The recommended setup is

- client machine (Windows, Mac, or Linux)
- 3 host machines
- all machine configured with Docker CE installed from the Docker store

##Setting Up Your Client Machine

To do this workshop you will need Docker, Docker Compose, and Docker Machine.

### Installing Docker

All the editions of Docker on different platforms are now available from the Docker store

- https://store.docker.com/

Download your flavor, this document covers Docker CE running on Ubuntu 16.04.3 LTS https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/

After everything is setup, you should be able to get `version` and `info` from you client's Docker daemon

```bash
$ docker version
Client:
 Version:      17.09.0-ce
 API version:  1.32
 Go version:   go1.8.3
 Git commit:   afdb6d4
 Built:        Tue Sep 26 22:42:18 2017
 OS/Arch:      linux/amd64
 ...
 
$ docker info
Containers: 1
 Running: 0
 Paused: 0
 Stopped: 1
Images: 3
Server Version: 17.09.0-ce
...
```

As a final test, try

```bash
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

### Installing Docker Compose

Install compose by following the instructions here

- [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

### Installing Docker Machine

Install machine by following the instructions here

- [https://docs.docker.com/machine/install-machine/](https://docs.docker.com/machine/install-machine/)

Congrats! You're client machine is ready :)

## Setting up Host Machines

_Note: this step is only needed for the Docker Swarm portion_

For host setup we will use Docker Machine to create 3 hosts in Google's cloud.  Follow the setup instructions here

- https://docs.docker.com/machine/drivers/gce/

_Note: the above directions are outdated with respect to Application Default Credentials, you need to login with one of the following commands to use the example below_

-`gcloud auth application-default login`

Then you can create all 3 hosts with this simple script

```bash
#!/bin/bash -e

[ -z $1 ] && echo "Missing PREFIX" && exit

PREFIX=$1
PROJECT_ID='advizex-184819'

for node in {1..3}; do
docker-machine create \
    --driver google \
    --google-project $PROJECT_ID \
    "${PREFIX}-${node}" &
done
```

Run it like

```
$ ./bin/create-hosts my-host
```

If all goes well, you should be able to see 3 shiny new machines

```bash
$ docker-machine ls
NAME        ACTIVE   DRIVER   STATE     URL                         SWARM   DOCKER        ERRORS
my-host-1   -        google   Running   tcp://104.198.202.6:2376            v17.10.0-ce   
my-host-2   -        google   Running   tcp://104.197.11.162:2376           v17.10.0-ce   
my-host-3   -        google   Running   tcp://35.188.206.188:2376           v17.10.0-ce   
```

_Note: Swarm column empty at this point is normal_

To use a different provider follow the appropriate directions here

- https://docs.docker.com/machine/drivers/

Test a host like this

```bash
jack@jackbook:~ 
$ eval $(docker-machine env my-host-1)

jack@jackbook:~ [my-host-1]
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
9a0669468bf7: Pull complete 
Digest: sha256:cf2f6d004a59f7c18ec89df311cf0f6a1c714ec924eebcbfdd759a669b90e711
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```
*TODO: stuff to create a swarm*

```bash
jack@jackbook:~/src/github.com/advizex/demo
$ docker-machine ssh sandswarm-1
docker-user@sandswarm-1:~$ sudo docker swarm init --advertise-addr 10.128.0.3
docker-user@sandswarm-1:~$ sudo docker swarm join-token manager
docker-user@sandswarm-1:~$ logout
jack@jackbook:~/src/github.com/advizex/demo
$ docker-machine ssh sandswarm-2
docker-user@sandswarm-2:~$ sudo docker swarm join --token SWMTKN-1-27bd26v6qk0omg8atlvt23x0vw5ajpwpkiicj1memd8swct4x6-4exvvgd3mbzymdn9got5l4aqw 10.128.0.3:2377
docker-user@sandswarm-2:~$ logout
jack@jackbook:~/src/github.com/advizex/demo
$ docker-machine ssh sandswarm-3
docker-user@sandswarm-3:~$ sudo docker swarm join --token SWMTKN-1-27bd26v6qk0omg8atlvt23x0vw5ajpwpkiicj1memd8swct4x6-4exvvgd3mbzymdn9got5l4aqw 10.128.0.3:2377
```

Congrats! Your hosts are ready for the workshop.

<script type="text/javascript" src="http://localhost:3000/a/KLgHeIVgN111rrUtAIf9iCT5l.js?rows=15" id="asciicast-KLgHeIVgN111rrUtAIf9iCT5l" async data-rows=15 data-autoplay=true></script>
