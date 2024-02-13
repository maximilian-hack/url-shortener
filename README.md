# URL Shortener Project

This project is a URL shortener implemented mainly in JavaScript, utilizing Express.js for the API and Sequelize for interfacing with a MySQL database. It is hosted within Docker containers orchestrated by Docker Compose. The deployment includes a Nginx web server and a Nginx reverse proxy.

## Technologies Used:

- **JavaScript:** The primary programming language used for implementing the backend logic.
- **Express.js:** A web application framework for Node.js, used for building the API endpoints.
- **Sequelize:** An ORM (Object-Relational Mapping) for Node.js, used for managing interactions with the MySQL database.
- **MySQL:** A relational database management system used for storing URL data.
- **Docker:** A platform for developing, shipping, and running applications in containers.
- **Docker Compose:** A tool for defining and running multi-container Docker applications.
- **Nginx:** A high-performance web server used for serving static files and as a reverse proxy.

## Project Features:

- **URL Shortening:** Users can input a long URL and receive a shortened version, allowing for more convenient sharing.
- **Database Storage:** Shortened URLs and their corresponding long URLs are stored persistently in a MySQL database.
- **Containerized Deployment:** The application is deployed using Docker containers, ensuring consistent runtime environments across different platforms.
- **Nginx Web Server:** Nginx is utilized as the web server to serve static content and handle incoming HTTP requests.
- **Nginx Reverse Proxy:** Nginx acts as a reverse proxy, forwarding requests to the appropriate containers based on their URLs.

## Learning Highlights:

- **Docker:** Gain practical experience with Docker, understanding containerization principles and how to manage multi-container applications.
- **JavaScript:** Deepened understanding of JavaScript, particularly in the context of building backend applications with Node.js and Express.js.
- **Sequelize:** Learned how to use Sequelize as an ORM to simplify database interactions and manage database schemas effectively.
- **MySQL:** Acquired knowledge of working with MySQL databases, including schema design, data modeling, and query optimization.
- **Nginx:** Explored the capabilities of Nginx, both as a web server and a reverse proxy, understanding its role in modern web application architectures.

--- 
© 2024 Maximilian Hack

Feel free to contribute to the project by submitting pull requests or reporting issues.