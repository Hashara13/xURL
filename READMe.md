# xURL

xURL is a powerful URL shortener application built with Flask, SQLAlchemy, Redis, and Celery. It allows users to easily convert long URLs into short, manageable links, while tracking click statistics and managing redirection seamlessly.

## Features

- **URL Shortening**: Quickly shorten long URLs into compact links.
- **Click Tracking**: Monitor the number of clicks for each shortened URL.
- **User-Friendly Interface**: A simple and intuitive web interface for easy URL management.
- **Background Processing**: Utilizes Celery for handling background tasks like click tracking.
- **Redis Caching**: Implements Redis for caching, improving performance.

## Tech Stack

- **Backend**: Flask
- **Database**: SQLAlchemy (SQLite)
- **Caching**: Redis
- **Background Tasks**: Celery

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/xURL.git
   cd xURL

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   cd xURL

4. Set up Redis and start the server:
   ```bash
   redis-server

5. Run the Flask application:
   ```bash
   flask run

6. Start the Celery worker in a new terminal:
   ```bash
   celery -A app.celery worker --loglevel=info