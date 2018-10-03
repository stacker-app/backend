# Stacker backend
> API PROVIDED

## Build setup
```bash
# Makemigrations
$ docker-compose run web python /code/manage.py makemigrations

# Build image and up
$ docker-compose up -d --build

# Migrate
$ docker-compose run web
# Or
$ docker-compose run web python /code/manage.py migrate --noinput

# Create user
$ docker-compose run web python /code/manage.py createsuperuser
```