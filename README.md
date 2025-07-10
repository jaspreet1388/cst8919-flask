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
```
---

### Create a Virtual Environment and Activate It
bash
Copy
Edit

### Install Dependencies
If you have requirements.txt:
```
bash
Copy
Edit
pip install -r requirements.txt
```
---
### Auth0 Setup
Go to Auth0 Dashboard

Create a new Regular Web Application

In Application → Settings, update these fields:

### Allowed Callback URLs:
```
bash
Copy
Edit
http://localhost:5000/callback
```

### Allowed Logout URLs:
```
arduino
Copy
Edit
http://localhost:5000
```
### Allowed Web Origins:
```
arduino
Copy
Edit
http://localhost:5000
```

### Create .env File
In the root of your project, create a file named .env with the following content:
```
APP_SECRET_KEY=your_flask_secret_key_here
AUTH0_CLIENT_ID=your_auth0_client_id
AUTH0_CLIENT_SECRET=your_auth0_client_secret
AUTH0_DOMAIN=https://your-tenant-name.us.auth0.com
AUTH0_CALLBACK_URL=http://localhost:5000/callback

Note - Same is uploade to the azure for azure app to work with this environment
```
---
### Run the App
```
export FLASK_APP=app.py
flask run  (local)
For azure the app will work once code is committed on github.

```
### Screenshots:

<img width="1352" height="697" alt="image" src="https://github.com/user-attachments/assets/a0464d65-72eb-4e8f-8b09-70fa1f3f19e3" />

<img width="1897" height="700" alt="image" src="https://github.com/user-attachments/assets/337bcff9-c014-4ad5-bd45-62ac31de089f" />

<img width="1912" height="796" alt="image" src="https://github.com/user-attachments/assets/b24872aa-f793-4f91-a5b5-09b79635f548" />

<img width="1920" height="492" alt="image" src="https://github.com/user-attachments/assets/46814b3c-33fa-40a7-8f5e-00a4b1ef184b" />

<img width="1490" height="327" alt="image" src="https://github.com/user-attachments/assets/f124ee7f-651d-4e5a-9a7b-c213e44a71f7" />

<img width="1862" height="733" alt="image" src="https://github.com/user-attachments/assets/1edaf909-af72-4443-b101-c60037649edf" />

<img width="1783" height="720" alt="image" src="https://github.com/user-attachments/assets/dd1bcc82-d00c-45b1-9abb-ef7ef50f93d3" />

<img width="1908" height="802" alt="image" src="https://github.com/user-attachments/assets/5e9fa987-04a8-4278-8592-5d253eebacc2" />











### Then visit URl :
- http://localhost:5000
- https://webappportal-bffzhgfjcdhmfjc7.canadacentral-01.azurewebsites.net/
Note : URL will only work when app is running on azure or locally

### Demo Youtube URL -  
- (part1) https://youtu.be/OO5-5pQHF6Y
- (part2) 

