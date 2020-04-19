[![Build Status](https://circleci.com/gh/vsevolod-skripnik/vash-backend.svg?style=shield)](https://circleci.com/gh/vsevolod-skripnik/vash-backend)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/104083b6754649dfa1df343baffee257)](https://www.codacy.com/gh/vash-framework/vash-backend?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vash-framework/vash-backend&amp;utm_campaign=Badge_Grade)
[![The Humanoid Typhoon](https://img.shields.io/badge/wanted-%24%2460%2C000%2C000%2C000-red)](https://trigun.fandom.com/wiki/Vash_the_Stampede)



# Vash

Commands:

- Test backend: `docker exec -it vash-backend_backend_1 coverage run --source=. -m pytest --emoji`

- Run backend migrations: `docker exec -it vash-backend_backend_1 python manage.py migrate`

- Collect static: `docker exec -it vash-backend_backend_1 python manage.py collectstatic`


## How to run in development mode

Create `.env` with the following content:

```sh
# Assigned to user inside container to avoid permission problems when mounting volumes. You can get your id by running `id -u`
BACKEND_USER_ID=1000

# Used to tag backend image. Leave as `latest` if you don’t care
BACKEND_VERSION=latest

# Used in Django settings
BACKEND_DEBUG=on
BACKEND_SECRET_KEY=f$anhq$lj#8n5cd(wlxe^41-0cx9i)zxmuc9zf5o_^!@y_e!^8

# Used during database initialization and in Django settings to connect to the database
DATABASE_HOST=database
DATABASE_PORT=5432
DATABASE_DB=vash
DATABASE_USER=user
DATABASE_PASSWORD=password1234
```

Then build and up images: `docker-compose --project-directory . -f backend/compose/common.yml -f backend/compose/development.yml -f database/compose.yml -f webserver/compose.yml up --build`


## How to run in production mode

Create `.env` with the same content as in “How to run in development mode”, but change `BACKEND_DEBUG` to `off`, change `BACKEND_VERSION` to something meaningful, change secret `BACKEND_SECRET_KEY` and `DATABASE_PASSWORD` to secret values

Then build images: `docker-compose --project-directory . -f backend/compose/common.yml -f backend/compose/production.yml -f database/compose.yml -f webserver/compose.yml build`

And then up images: `docker-compose --project-directory . -f backend/compose/common.yml -f backend/compose/production.yml -f database/compose.yml -f webserver/compose.yml up --detach`
