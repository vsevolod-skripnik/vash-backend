[![Build Status](https://circleci.com/gh/vsevolod-skripnik/vash-backend.svg?style=shield)](https://circleci.com/gh/vsevolod-skripnik/vash-backend)
[![The Humanoid Typhoon](https://img.shields.io/badge/wanted-%24%2460%2C000%2C000%2C000-red)](https://trigun.fandom.com/wiki/Vash_the_Stampede)

# Vash

## How to run in development mode

Create `.env` with the following content:

1. `USER_ID=1000`. Assigned to user inside container to avoid permission problems when mounting volumes. You can get your id by running `id -u`

2. `DATABASE_PASSWORD=password1234`. Used as root password during database initialization


Create `backend/code/vash/.env` with the following content:

1. `DEBUG=on`. Used in settings

2. `SECRET_KEY=f$anhq$lj#8n5cd(wlxe^41-0cx9i)zxmuc9zf5o_^!@y_e!^8`. Used in settings

3. `SQLITE_URL=sqlite:///db.sqlite3`. Used in settings


Then build images: `docker-compose --project-directory . -f backend/compose/common.yml -f backend/compose/development.yml -f database/compose.yml -f webserver/compose.yml build`

And run images: `docker-compose --project-directory . -f backend/compose/common.yml -f backend/compose/development.yml -f database/compose.yml -f webserver/compose.yml up`


## How to run in production mode

1. Execute steps 1 and 2 from “How to run in development mode”

2. Write `BACKEND_VERSION=1.27.42a` to `.env`. Version may be any string. Used to tag image during deployment. Set to `latest` if you don't care

3. Run images which must be built already: `docker-compose --project-directory . -f backend/compose/common.yml -f backend/compose/production.yml -f database/compose.yml -f webserver/compose.yml up -d`


Scripts:

1. Test backend: `docker exec -it vash-backend_backend_1 pytest --emoji`.

2. Run backend migrations: `docker exec -it vash-backend_backend_1 python manage.py migrate`.
