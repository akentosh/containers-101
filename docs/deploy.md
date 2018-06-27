# Deploying the Application

From the `advizex/demo/asciinema`, run the following

```bash
docker-compose up -d postgres
docker-compose run --rm web setup
docker-compose up -d
```
You can test with
```bash
export ASCIINEMA_API_URL=http://localhost:3000
asciinema auth
asciinema rec
```
