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

