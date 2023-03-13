## QUICKSTART
 - install "Docker" and "Docker Compose"
 - create and fill dev.env or prod.env with .env.template 
 - docker-compose <dev/prod/stage file> up -d --build
    - for dev version add "-f docker-compose.dev.yml" after "docker-compose"
    - go into backend container and run ./manage.py migrate
