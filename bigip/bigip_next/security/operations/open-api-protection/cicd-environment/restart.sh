docker compose down
rm -rf jenkinshome
rm -rf shared
docker compose build
docker compose up
