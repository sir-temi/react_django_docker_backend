# React Django Docker Backend

This repository contains the code for a full-stack web application built with React for the frontend, Django for the backend, and Docker for containerization.

## Features

- **React Frontend:** Modern and responsive user interface built with React.
- **Django Backend:** Backend API server powered by Django.
- **Dockerized Environment:** Easily deploy the application in a Docker container.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/sir-temi/react_django_docker_backend.git
   cd react_django_docker_backend
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

   This command will start the React development server and Django backend server inside Docker containers.

3. Access the application:
   - Backend: The Django API server is accessible at `http://localhost:8000`.

## Project Structure
- `/`: Houses the Django backend code.
- `docker-compose.yml`: Configuration file for Docker Compose.

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
