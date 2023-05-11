# NiftyBridge

This project is called NiftyBridge. It provides a set of instructions to run the project using Docker.

## Setup

1. Start by copying the example `.env` file and paste your keys or configurations there.

   ```shell
   cp example.env .env

Update the .env file with your desired values.

    Build the Docker container using the provided Dockerfile.

    shell

    docker build -t myapp .

Running the Application

To run the application, use the following command:

shell

docker run -p 8000:8000 myapp

This command will start the Docker container and map port 8000 from the container to port 8000 on your local machine.

