# CloudShop Microservices DevOps Project

## Overview

CloudShop is a production-inspired microservices application built to demonstrate modern DevOps practices from application development through deployment, monitoring, and visualization.

This project showcases how a DevOps engineer can build, containerize, deploy, monitor, and operate a Kubernetes-based microservices application using industry-standard tools.

---

## Project Objectives

* Build a containerized microservices application
* Deploy applications on Kubernetes (Kind)
* Configure NGINX Ingress for external routing
* Implement CI/CD using GitHub Actions
* Integrate DevSecOps security scanning
* Collect application metrics with Prometheus
* Visualize system health using Grafana
* Demonstrate production-style DevOps workflows

---

# Architecture

```text
                        Users
                          │
                          ▼
                  NGINX Ingress Controller
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   Frontend         User Service     Product Service
                          │
                          ▼
                   Order Service

──────────────────────────────────────────────

                Monitoring Stack

Frontend (NGINX Exporter)
        │
User Service (/metrics)
        │
Product Service (/metrics)
        │
Order Service (/metrics)
        │
        ▼
    Prometheus
        │
        ▼
     Grafana
```

---

# Technology Stack

## Cloud & Containers

* Docker
* Docker Hub
* Kubernetes
* Kind
* NGINX Ingress Controller

## Backend

* Python
* Flask

## Frontend

* HTML
* NGINX

## CI/CD

* GitHub Actions

## DevSecOps

* Bandit
* pip-audit
* Gitleaks

## Monitoring

* Prometheus
* Grafana
* NGINX Prometheus Exporter
* Prometheus Python Client

---

# Repository Structure

```text
cloudshop-microservices-project/

├── frontend/
├── user-service/
├── product-service/
├── order-service/
├── nginx/
├── k8s/
│   ├── frontend/
│   ├── user-service/
│   ├── product-service/
│   ├── order-service/
│   ├── monitoring/
│   ├── ingress.yml
│   └── namespace.yml
├── .github/
│   └── workflows/
├── docker-compose.yml
├── kind-config.yml
└── README.md
```

---

# Microservices

### Frontend

* Static NGINX web application
* Routes requests through Kubernetes Ingress
* Exposes NGINX metrics for Prometheus

---

### User Service

* User Management API
* CRUD endpoints
* Prometheus metrics endpoint

---

### Product Service

* Product Catalog API
* Product lookup endpoints
* Prometheus metrics endpoint

---

### Order Service

* Order Management API
* Order creation endpoint
* Prometheus metrics endpoint

---

# Kubernetes Components

* Namespace isolation
* Deployments
* ClusterIP Services
* NGINX Ingress
* Resource requests & limits
* Rolling updates

---

# CI/CD Pipeline

GitHub Actions pipeline performs:

* Source checkout
* Python dependency installation
* Unit testing
* Bandit security scan
* pip-audit vulnerability scan
* Gitleaks secret detection
* Docker image build
* Docker image push to Docker Hub

---

# Monitoring

Prometheus collects metrics from:

* Frontend (NGINX Exporter)
* User Service
* Product Service
* Order Service

Collected metrics include:

* HTTP request count
* Request rate
* CPU usage
* Memory usage
* Python runtime metrics
* NGINX active connections
* Service availability

---

# Grafana Dashboard

Custom dashboard includes:

* Service Health
* HTTP Request Rate
* CPU Usage
* Memory Usage
* Active Connections
* Total Requests

---

# DevOps Skills Demonstrated

* Docker Image Creation
* Multi-Service Architecture
* Kubernetes Deployments
* Kubernetes Networking
* Ingress Configuration
* Kubernetes Resource Management
* CI/CD Pipeline Design
* DevSecOps Integration
* Prometheus Monitoring
* Grafana Visualization
* Application Observability
* Git & GitHub Workflow

---

# Future Enhancements

Planned improvements include:

* Helm Charts
* Kubernetes Service Discovery
* Alertmanager
* Email Notifications
* Horizontal Pod Autoscaler (HPA)
* Loki & Promtail
* Distributed Tracing (Jaeger/Tempo)
* Terraform Infrastructure as Code
* Argo CD GitOps Deployment

---

# Screenshots

Add screenshots of:

* Application UI

<img width="1188" height="886" alt="UI" src="https://github.com/user-attachments/assets/ef92fb2d-a988-4fa5-84b9-6f40f589204f" />

* Grafana Dashboard

<img width="1459" height="906" alt="grafana-screenshot" src="https://github.com/user-attachments/assets/0bb41a52-b6f5-4c54-98b4-37a565f923e0" />

  
* GitHub Actions Pipeline

<img width="1886" height="419" alt="cicd-pipeline" src="https://github.com/user-attachments/assets/301612ec-e364-499e-aad3-8e5bcd2042d9" />


---

# Getting Started

## Clone the repository

```bash
git clone https://github.com/Yasir-Z/cloudshop-microservices-project.git
cd cloudshop-microservices-project
```

## Build Docker images

```bash
docker build -t <image-name> .
```

## Create Kind Cluster

```bash
kind create cluster --config kind-config.yml
```

## Deploy Kubernetes Resources

```bash
kubectl apply -f k8s/
```

## Verify Resources

```bash
kubectl get pods -n production
kubectl get ingress -n production
kubectl get svc -n production
```

---

# Key Learning Outcomes

This project demonstrates practical experience with:

* Building and deploying containerized microservices
* Managing Kubernetes workloads
* Implementing CI/CD automation
* Integrating security scanning into pipelines
* Monitoring applications with Prometheus
* Building operational dashboards with Grafana
* Applying production-inspired DevOps practices

---

## GitHub Repository

https://github.com/Yasir-Z/cloudshop-microservices-project

---

## Author

**Yasir Zafar**

DevOps Engineer | Kubernetes | Docker | CI/CD | DevSecOps | Prometheus | Grafana

LinkedIn: https://www.linkedin.com/in/yasir-zafar-495912405
