#!/bin/bash
docker-compose up -d
echo "waiting for message queue start..."

#sleep 15

echo "starting api and core plattaform"
(python app/app.py; [ "$?" -lt 2 ] && kill "$$") &
echo "run flask api"
sleep 2
(python core/queue.py; [ "$?" -lt 2 ] && kill "$$") &
echo "run python core"
wait