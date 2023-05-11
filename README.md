# NiftyBridge

This project is called NiftyBridge. It provides a set of instructions to run the project using Docker.

## Setup

1. Start by copying the example `.env` file and paste your keys or configurations there.

      ```cp example.env .env```

Update the .env file with your desired values.

2. Build the Docker container using the provided Dockerfile.

      ```docker build -t myapp .```

Running the Application

3. To run the application, use the following command:

      ```docker run -p 8000:8000 myapp```

This command will start the Docker container and map port 8000 from the container to port 8000 on your local machine.

