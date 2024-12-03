docker compose down
rm -rf jenkins-home
docker compose build
docker compose up
