#!/bin/bash

FLASK_APP_DIR="../../app/"
MYSQL_DB_DIR="../../db/"
FLASK_IMAGE="majavier/stensul-flask:latest"
MYSQL_IMAGE="majavier/stensul-mysql:latest"

# Build and push Flask app image
echo "Building image from $FLASK_APP_DIR..."
docker build --platform=linux/amd64 -t "$FLASK_IMAGE" "$FLASK_APP_DIR"

# if last command was successful
if [ $? -eq 0 ]; then 
    echo "Pushing image $FLASK_IMAGE..."
    docker push "$FLASK_IMAGE"

    if [ $? -eq 0 ]; then
        echo "Successfully pushed $FLASK_IMAGE"
    else
        echo "Failed to push $FLASK_IMAGE"
    fi
else
    echo "Failed to build image from $FLASK_APP_DIR"
fi

# Build and push MySQL image
echo "Building image from $MYSQL_DB_DIR..."
docker build --platform=linux/amd64 -t "$MYSQL_IMAGE" "$MYSQL_DB_DIR"

# if last command was successful
if [ $? -eq 0 ]; then
    echo "Pushing image $MYSQL_IMAGE..."
    docker push "$MYSQL_IMAGE"

    if [ $? -eq 0 ]; then
        echo "Successfully pushed $MYSQL_IMAGE"
    else
        echo "Failed to push $MYSQL_IMAGE"
    fi
else
    echo "Failed to build image from $MYSQL_DB_DIR"
fi

echo "All images have been processed."