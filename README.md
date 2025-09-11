# Quotes App
A simple **Flask web application** that displays random motivational quotes.  
This project demonstrates how to **Dockerize a Python Flask app**, push the image to **Docker Hub**, and deploy it to **Render**.


## Features
- Built with **Flask (Python)**
- Adding and Deleting Quotes
- Displays random motivational quotes  
- Dockerized for easy deployment  
- Hosted live on **Render**



## Tech Stack
- **Python** (Flask)  
- **Docker**  
- **Docker Hub**  
- **GitHub**  
- **Render**


## 📂 Project Setup

### 1.Clone the Repository
```bash
git clone https://github.com/Akhileswar6/Quotes-app.git
cd Quotes-app
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run the App Locally
```
python app.py
```
Visit ``` http://127.0.0.1:5000 ```

---
## 🐳 Docker Setup
### 1. Build Docker Image
```
docker build -t quotes-app .
```

### 2. Run Container
```
docker run -d -p 5000:5000 quotes-app
```
### 3. Push to Docker Hub
```
docker login
```
### 4. Giving a tag before pushing to docker
```
docker tag quotes-app your-dockerhub-usernam/quotes-app:latest
```
### 5. Pushing to docker hub
```
docker push your-dockerhub-username/quotes-app:latest
```
### 6. Pull and Run (from Docker Hub)
```
docker pull your-dockerhub-username/quotes-app
docker run -d -p 5000:5000 your-dockerhub-username/quotes-app
```
