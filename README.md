# Kubernetes Lab with FastAPI and PostgreSQL

This repository contains a FastAPI application integrated with a PostgreSQL database, designed for deployment in a Kubernetes environment.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Deployment](#deployment)
- [Accessing the Application](#accessing-the-application)
- [Testing the Application](#testing-the-application)
- [Cleanup](#cleanup)

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [PostgreSQL](https://www.postgresql.org/download/) (optional for local testing)

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/MrCorazon01/k8s-lab.git
   cd k8s-lab
   ```

2. **Build the Docker Image**:

   Build the Docker image for the FastAPI application using the following command:

   ```bash
   docker build -t myapp-backend .
   ```

## Deployment

1. **Start Minikube**:

   Start a Minikube cluster with three nodes:

   ```bash
   minikube start --nodes 3 --driver=docker
   ```

2. **Apply Kubernetes Manifests**:

   Deploy the application and database by applying the Kubernetes manifest files. Run the following commands in the directory where your YAML files are located:

   ```bash
   kubectl apply -f k8s/database-secret.yaml
   kubectl apply -f k8s/database-configmap.yaml
   kubectl apply -f k8s/database-deployment.yaml
   kubectl apply -f k8s/database-service.yaml
   kubectl apply -f k8s/backend-secret.yaml
   kubectl apply -f k8s/backend-configmap.yaml
   kubectl apply -f k8s/backend-deployment.yaml
   kubectl apply -f k8s/backend-service.yaml
   ```

3. **Verify Deployments**:

   Ensure that all pods are running:

   ```bash
   kubectl get pods
   ```

   You should see the backend and database pods listed, and their statuses should be `Running`.

## Accessing the Application

To access the FastAPI application, you need to find the NodePort assigned to the backend service. Run the following command:

```bash
kubectl get services
```

Look for the `backend-service` and note the `NodePort` (it should be between `30000` and `30080`).

You can access the application in your web browser or via curl with the following URL format:

```
http://<minikube-ip>:<NodePort>
```

To get the Minikube IP, run:

```bash
minikube ip
```

## Testing the Application

1. **Health Check**:

   To check if the application is running, you can access the health endpoints:

   ```bash
   curl http://<minikube-ip>:<NodePort>/health/live
   curl http://<minikube-ip>:<NodePort>/health/ready
   ```

2. **CRUD Operations**:

   You can perform CRUD operations on the `/items` endpoint:

   - **Create an Item**:

     ```bash
     curl -X POST http://<minikube-ip>:<NodePort>/items -H "Content-Type: application/json" -d '{"name": "Item Name"}'
     ```

   - **Get All Items**:

     ```bash
     curl http://<minikube-ip>:<NodePort>/items
     ```

## Cleanup

To clean up and remove all resources created during this deployment, you can delete the Kubernetes objects:

```bash
kubectl delete -f k8s/
```

You can also stop the Minikube cluster when you're done:

```bash
minikube stop
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.