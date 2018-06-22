# Agenda

### Overview of Docker architecture

- Discussion around [Docker Architecture](https://docs.docker.com/engine/docker-overview/#docker-architecture)

- Containers are best compared to a process (more about what containers are and how they are not VMs)

- Images versus containers

- Image layers

    - Write only layers (overlayfs, unionfs)
    - Allows for faster pull and local caching
    - Only writing to the top layer so we can build on other images

- Network and storage drivers

### Why Docker

- Standard shipping container analogy

- Cloud portability

- Software development life-cycle with containers

- How containers help increase your security posture

    - Immutability (containers don't change, going back to layers)

- Common operations lifecycle and tooling (draws the line between development and operations)

    - Discussion around [CNCF](https://www.cncf.io/)
    - Kubernetes is their orchestration platform of choice so probably focused around that

# Demo

### Docker Demo

- Format and components of Dockerfile

- Call out on DB -- using mssql in a container which is cool (optional)

- make-graph.sh to show what we are deploying

- Application overiew

    - Phase 1 of demo is containers deployed on laptop

- Show the apps running and the processes on the local host

- Quick chat around orchestration/kubernetes and running containers in prod

    - Phase 2 is demo running on kubernetes in GCP 

- Interactive opportunity, allow attendees to spin up containers?
