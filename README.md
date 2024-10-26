# AuthSystemAPI

### Secure and scalable API for user registration, login, and authentication

![Flask](https://img.shields.io/badge/Flask-v2.0+-blue) ![Python](https://img.shields.io/badge/Python-3.8+-green) ![License](https://img.shields.io/badge/License-MIT-brightgreen)

> A lightweight, scalable authentication API built with Flask, Flask_Session and PyMySQL. This API provides secure endpoints for registration, login and management of user sessions with log system.

## Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Endpoints](#endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **User Registration**: Allows new users to register with a secure password.
- **User Login**: Authenticates users and establishes sessions.
- **Session Management**: Manages user sessions securely using Flask-Session.
- **Password Hashing**: Uses bcrypt for password hashing and validation.
- **Error Handling**: Provides clear error messages for authentication failures.
- **Environment-Based Configuration**: Easy setup with `.env` for sensitive data.
- **Automatic Logging**: Implements automatic logging for all endpoints, recording requests and responses, including status codes and timestamps, to assist in monitoring and debugging.

## Requirements
- Python 3.8+
- Flask
- Flask-Session
- PyMySQL
- bcrypt
- python-dotenv
- MySQL database

## Installation

Follow the steps below to set up and run the project on your local machine:

### 1. Download the Project

To download only the latest version of the project (without the full commit history), [click here](https://github.com/your-username/authAPI/archive/refs/heads/main.zip) to download the source code as a ZIP file. Extract the contents to a directory on your machine.

Alternatively, you can use `git clone` to download just the latest commit:

```bash
git clone --depth 1 https://github.com/your-username/authAPI.git
cd authAPI
```

### 2. Create and Activate a Virtual Environment

For a cleaner setup, create and activate a virtual environment:
```bash
python3 -m venv venv

source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate  # On Windows: 
```

### 3. Install Dependencies

With the virtual environment active, install the required libraries:

```bash
pip install -r requirements.txt
```

### 4. Configure the Project

Open the configuration file in the project directory `config.py` and update the following settings:

```dotenv
SECRET_KEY = "your-secret-key-here"
DB_HOST = "host"
DB_USER = "user"
DB_PASSWORD = "password"
DB_NAME = "database-name"
```

- Replace `your_secret_key` with a unique secret key.
- Replace `host`, `user`, `password` and `database-name` with your MySQL database credentials.

### 5. Run the Project to Initialize Database Tables

To set up the database tables, run the project for the first time in the project diretory:

```bash
python main.py
```

The API will be available at `http://127.0.0.1:5000/` by default.

You can also configure the host and port directly from the `.env` file:

```dotenv
# API CONFIG
API_HOST="127.0.0.1"
API_PORT="5000"
```