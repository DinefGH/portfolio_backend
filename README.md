# Django Backend Project

This is a Django-based backend application designed to work with a frontend. The project includes setup instructions, Docker configuration, and deployment guidelines.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
  - [Running Locally](#running-locally)
  - [Running with Docker](#running-with-docker)

---

## Project Overview

This backend project provides a RESTful API using Django and Django REST framework. It includes endpoints for handling application data and is designed to work with an Angular frontend.

## Features

- RESTful API built with Django REST framework
- Dockerized for easy deployment
- Configurable CORS settings for frontend communication
- Separate environment settings for local and production

---

## Setup Instructions

### Prerequisites

- **Python 3.8+**
- **Django**: Install using `pip install django`
- **Docker** (if running with Docker)


Environment Variables
# .env file

# Django settings
SECRET_KEY=your-secret-key
DEBUG=True

# Database configuration (optional if using SQLite)
DATABASE_URL=your-database-url

# Allowed hosts and CORS settings
ALLOWED_HOSTS=localhost,127.0.0.1
FRONTEND_URL=https://your-frontend-url.com



Running the Project

Running Locally
1. Create a Virtual Environment (optional but recommended):

bash
Code kopieren
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


2.Install Dependencies:

bash
Code kopieren
pip install -r requirements.txt


3.Run Migrations:

bash
Code kopieren
python manage.py migrate


4.Run the Development Server:

bash
Code kopieren
python manage.py runserver
Access the Project: Open http://127.0.0.1:8000 in your browser.



Running with Docker


1.Build the Docker Image:

bash
Code kopieren
docker build -t django-backend .


2.Run the Docker Container:

bash
Code kopieren
docker run -d -p 8001:8001 django-backend
The app will be available at http://localhost:8001.


