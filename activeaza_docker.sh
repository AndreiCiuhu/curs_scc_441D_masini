#!/bin/bash

docker stop masini-container || true
docker rm masini-container || true


docker build -t masini-app .
docker run -d -p 5055:5055 --name masini-container masini-app

echo "Aplicatia ruleaza la http://localhost:5055"
