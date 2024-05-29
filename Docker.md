# DOCKER

# File

```dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

```

## Comands

docker version: Display the Docker version information.

docker info: Display system-wide information about Docker.

docker images: List all Docker images available locally on your system.

docker ps: List all running Docker containers.

docker ps -a: List all Docker containers, including those that are stopped.

docker pull <image_name>: Download a Docker image from a registry.

docker run <image_name>: Create and start a new Docker container based on the specified image.

docker stop <container_id or container_name>: Stop a running Docker container.

docker start <container_id or container_name>: Start a stopped Docker container.

docker restart <container_id or container_name>: Restart a running Docker container.

docker rm <container_id or container_name>: Remove a Docker container.

docker rmi <image_id or image_name>: Remove a Docker image.

docker exec -it <container_id or container_name> <command>: Execute a command inside a running Docker container.

docker logs <container_id or container_name>: View the logs of a Docker container.

docker build <path_to_Dockerfile>: Build a Docker image from a Dockerfile.

docker-compose up: Start Docker containers defined in a Docker Compose file.

docker-compose down: Stop and remove Docker containers defined in a Docker Compose file.
