Here’s a concise GitHub description for your backend and GitHub Actions setup:

---

# Backend for MQTT-NodeMCU IoT Project 🌐  

This repository contains the **Django backend** for the MQTT-NodeMCU IoT project. The backend is hosted on **AWS Lightsail**, uses **Redis** for WebSocket communication, and is containerized with **Docker Compose** for easy deployment and scalability.  

## Features  
- **MQTT Integration**: Receives data from NodeMCU via MQTT and processes it.  
- **WebSocket Support**: Real-time communication with the frontend using Django Channels and Redis.  
- **Dockerized Deployment**: Built and deployed using Docker Compose.  
- **CI/CD Pipeline**: Automated deployment with GitHub Actions.  

---

## Deployment  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repo-name.git  
   cd MQTT-NodeMCU/IOT  
   ```  

2. Build and start containers:  
   ```bash  
   docker compose up --build  
   ```  

3. Pull the latest Docker images (if needed):  
   ```bash  
   docker pull lakshanwanniarachchi/nginx  
   docker pull lakshanwanniarachchi/iot  
   ```  

4. Access the backend at the deployed server URL.  

---

## GitHub Actions CI/CD Pipeline  

The CI/CD pipeline is configured with GitHub Actions to automate the deployment process:  
1. **Push Code**: On pushing code to the main branch, GitHub Actions builds the Docker images for the backend and Nginx.  
2. **Docker Hub**: The images are pushed to Docker Hub:  
   - `lakshanwanniarachchi/nginx`  
   - `lakshanwanniarachchi/iot`  
3. **AWS Lightsail Deployment**: The GitHub runner pulls the latest Docker images to the AWS Lightsail server and starts the application using Docker Compose.  

---

This setup ensures seamless deployment and real-time functionality for the IoT system. Feel free to contribute or suggest improvements! 😊  

--- 

