# Challenge
- Create a simple deployable web app using PHP and MySQL to store names added on a web form.
- You need to develop 2 endpoints, one for adding new names and another for reading names. 
- Public URL must be configured on Helm values.yaml file.
- A group of files to be used/deployed locally (docker-compose)
- A group of files to be deployed in a K8s cluster with Helm (in DigitalOcean)
- A diagram

## Stensul project
This project is a simple Flask application that connects to a MySQL database. It allows users to add names to the database and retrieve a list of all names.

## Project tree

```bash
.
├── README.md
├── app
│   ├── dockerfile
│   ├── main.py
│   └── requirements.txt
├── db
│   ├── Dockerfile
│   └── database.sql
└── deploy
    ├── docker
    │   ├── docker-compose.yaml
    │   └── push_images.sh
    └── helm
        └── stensul-app
            ├── Chart.yaml
            ├── charts
            ├── templates
            │   ├── _helpers.tpl
            │   ├── deployment.yaml
            │   ├── service.yaml
            │   └── statefulset.yaml
            └── values.yaml
```

## Prerequisite 

```bash
- Docker
- Docker Compose
- helm
- kubectl
```

## Start app locally

```bash
cd deploy/docker/
docker-compose up --build
```

## Test app locally
```bash
# add user endpoint
curl -X POST -H "Content-Type: application/json" -d '{"name": "javi"}' http://localhost:5000/add_name # add colima ip here
# list users endopint
curl -X GET http://localhost:5000/list_names # add colima ip here
```

## Push docker to registry
```bash
chmod +x deploy/docker/push_images.sh
cd /deploy/docker/
./push_images.sh
```

## Deploy app remotly 
```bash
helm install stensul-app deploy/helm/stensul-app/ --namespace default
```

## Clean up
```bash
# docker
cd deploy/docker/
docker-compose down -v

# helm
helm uninstall stensul-app --namespace default
```