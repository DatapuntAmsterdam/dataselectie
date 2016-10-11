#!/usr/bin/env bash

set -u
set -e

# wait for elastic
while ! nc -z ${ELASTICSEARCH_PORT_9200_TCP_ADDR} ${ELASTICSEARCH_PORT_9200_TCP_PORT}
do
	echo "Waiting for elastic..."
	sleep 0.1
done

# wait for postgres BAG
while ! nc -z ${DATABASE_BAG_PORT_5432_TCP_ADDR} ${DATABASE_BAG_PORT_5432_TCP_PORT}
do
	echo "Waiting for postgres..."
	sleep 0.1
done

# wait for postgres dataselectie
while ! nc -z ${DATABASE_dataselectie_PORT_5432_TCP_ADDR} ${DATABASE_dataselectie_PORT_5432_TCP_PORT}
do
	echo "Waiting for postgres..."
	sleep 0.1
done