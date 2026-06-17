# Microservices E-Commerce App on Kubernetes 🚀

## Architecture
User Service → Port 5001
Product Service → Port 5002  
Order Service → Port 5003

## Tech Stack
- Kubernetes (Kind)
- Docker + DockerHub
- Python Flask
- HPA (Auto Scaling)
- GitHub Actions CI/CD

## Services
| Service | Port | Endpoint |
|---|---|---|
| User Service | 5001 | /users |
| Product Service | 5002 | /products |
| Order Service | 5003 | /orders |

## How to Run
kubectl apply -f k8s/
