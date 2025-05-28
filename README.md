# Flask Auth0 Web App

This project demonstrates a Python Flask web application integrated with Auth0 for secure authentication. It supports login, logout, session-based authentication, and route protection.

---

## Features

- Auth0 login/logout flow
- User session management
- Protected route `/protected` accessible only to authenticated users
- Redirects unauthenticated users to login
- Configurable using `.env`

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jaspreet1388/flask-auth0-app.git
cd flask-auth0-app

---

### Create a Virtual Environment and Activate It
bash
Copy
Edit

### Install Dependencies
If you have requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt

---
### Auth0 Setup
Go to Auth0 Dashboard

Create a new Regular Web Application

In Application → Settings, update these fields:

- Allowed Callback URLs:

bash
Copy
Edit
http://localhost:5000/callback
- Allowed Logout URLs:

arduino
Copy
Edit
http://localhost:5000
- Allowed Web Origins:

arduino
Copy
Edit
http://localhost:5000

