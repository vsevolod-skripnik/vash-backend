How to run in development mode:

1. Write `USER_ID=1000` to `.env`. Used as container user's id to avoid permission problems when mounting volumes. You can get your id by running `id -u`

2. Write `DATABASE_PASSWORD=password1234` to `.env`. Used as root password during database initialization

3. Build images: `docker-compose --project-directory . -f backend/compose/common.yml -f backend/compose/development.yml -f database/compose.yml -f webserver/compose.yml build`

4. Run images: `docker-compose --project-directory . -f backend/compose/common.yml -f backend/compose/development.yml -f database/compose.yml -f webserver/compose.yml up`


How to run in production mode:

1. Execute steps 1 and 2 from “How to run in development mode”

2. Write `BACKEND_VERSION=1.27.42a` to `.env`. Version may be any string. Used to tag image during deployment. Set to `latest` if you don't care

3. Run images which must be built already: `docker-compose --project-directory . -f backend/compose/common.yml -f backend/compose/production.yml -f database/compose.yml -f webserver/compose.yml up -d`


Scripts:

1. Test backend: `docker exec -it vash-backend_backend_1 pytest --emoji`.

2. Run backend migrations: `docker exec -it vash-backend_backend_1 python manage.py migrate`.
