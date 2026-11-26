# Flask Blog
**FlaskBlog** is a full-stack multi-user blogging platform built with Python and Flask. Engineered with secure authentication, token-based password recovery, and strict ownership-based access control, it enables users to publish content and manage their accounts safely.

## Key Features
* **Authentication & Session Management:** Secure user registration, login, and logout workflows.
* **Token-Based Password Recovery:** Automated forgot-password flow that dispatches time-sensitive reset tokens via email.
* **Post Management:** Create, read, update, and delete blog posts with rich content support.
* **Ownership-Based Access Control:** Enforces authorization checks ensuring users can only edit or delete their own posts and access their own account settings.
* **Profile Management:** Allows authenticated users to update their username, email address, password, and profile picture.
* **Custom Error Handling:** Dedicated error pages for `403` (Forbidden), `404` (Not Found), and `500` (Internal Server Error) responses.

## Tech Stack
* **Backend:** Python, Flask, SQLAlchemy
* **Database:** PostgreSQL / SQLite (via SQLAlchemy ORM)
* **Frontend:** HTML5, CSS, Bootstrap, Jinja2
* **Deployment:** Nginx, Gunicorn, python-dotenv


## Project Structure
```
.
├── flask_blog
│   ├── config.py
│   ├── errors
│   │   ├── handlers.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models.py
│   ├── posts
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static
│   │   ├── default.jpg
│   │   └── main.css
│   ├── templates
│   │   ├── about.html
│   │   ├── account.html
│   │   ├── create_post.html
│   │   ├── errors
│   │   │   ├── 403.html
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── home.html
│   │   ├── layout.html
│   │   ├── login.html
│   │   ├── post.html
│   │   ├── register.html
│   │   ├── reset_request.html
│   │   ├── reset_token.html
│   │   └── user_posts.html
│   └── users
│       ├── forms.py
│       ├── __init__.py
│       ├── routes.py
│       └── utils.py
├── README.md
├── requirements.txt
└── server.py
```

## Setup & Install
To install and run FlaskBlog locally, follow these steps and replace the placeholder credentials with your own:
> **Note for Windows users:** Run these commands in **Git Bash**, using `python` instead of `python3` and `source .venv/Scripts/activate` to activate the virtual environment.

````bash
# Clone Project Files & Navigate To It
git clone "<repo_link_here>"
cd "<repo_folder_here>"

# Python Virtual Environment Setup & Activate
python3 -m venv .venv
source .venv/bin/activate

# Install Project Requirements
pip install -r requirements.txt

# Create & Configure .env File
touch .env
echo 'SECRET_KEY=<your_secret_key_here>' >> .env
echo 'SQLALCHEMY_DATABASE_URI=<your_db_uri_here>' >> .env
echo 'MAIL_USERNAME=<your_mail_username_here>' >> .env
echo 'MAIL_PASSWORD=<your_mail_password_here>' >> .env

# Run The Project In Development Environment
python3 server.py
````

Once running, open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

#### To Run In Production
```bash
gunicorn -w 3 -b 127.0.0.1:5000 server:app
```


## Author's Notes
* Built with the Python and Flask ecosystem to deliver a reliable, multi-user blogging platform.
* Designed with a strong focus on clean modular architecture, relational data integrity, and secure user authentication.
* Structured to provide a clear, maintainable, and production-ready foundation for modern web applications.
