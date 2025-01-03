# Deployable Multi-Service Blog Application Using Docker and AWS

## Overview

This project demonstrates the development and deployment of a multi-service blog platform utilizing Docker containers and AWS services. The application comprises three primary services:

- **User Service**: Manages user authentication and profile management using JWT for authentication and bcrypt for password hashing.
- **Blog Service**: Handles blog post creation, retrieval, updating, and deletion, with support for pagination.
- **Comment Service**: Manages comments on blog posts, initially implemented as a flat structure with potential for future nesting.

The application is containerized using Docker and orchestrated with Docker Compose. It is deployed on AWS using EC2 instances and PostgreSQL for database management.

## Project Structure

The project is organized as follows:


## Prerequisites

Before setting up the project, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS Account](https://aws.amazon.com/)

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shalu07Yadav/docker.git
cd docker
docker-compose up --build
SECRET_KEY=your_secret_key
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=blog_db
 sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
newgrp docker
scp -i your-key.pem -r /path/to/your/project ec2-user@your-ec2-public-dns:/home/ec2-user/
 cd /home/ec2-user/docker
docker-compose up --build -d

This `README.md` provides a comprehensive guide to understanding the workflow and code of the multi-service blog application. It includes sections on project structure, prerequisites, local development setup, AWS deployment, API endpoints, design decisions, and a conclusion.
::contentReference[oaicite:0]{index=0}
 
