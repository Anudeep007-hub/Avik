


# Real-Time Video Chat (Django + WebRTC)

A minimal real-time video conferencing application built using **Django**, **WebRTC**, and **Django Channels**.  
It allows two users to connect randomly (like Omegle), view each other’s video streams, and exchange messages in real time.

---

## Features

- Peer-to-peer video calling using WebRTC
    
- Real-time random user matching (Omegle-style)
    
- Chat messaging between connected users
    
- Django Channels for WebSocket-based communication
    
- Minimal frontend using HTML, CSS, and JavaScript
    
- Scalable backend architecture ready for deployment
    

---

## Tech Stack

- **Backend:** Django, Django Channels
    
- **Frontend:** HTML, CSS, JavaScript (WebRTC APIs)
    
- **Communication:** WebSockets (via Channels)
    
- **Server:** ASGI (Daphne)
    

---

## Project Structure

```
webrtc_project/
│
├── manage.py
├── webrtc_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── chat/
    ├── __init__.py
    ├── consumers.py
    ├── routing.py
    ├── templates/
    │   └── chat/
    │       └── index.html
    ├── urls.py
    └── views.py
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/django-webrtc-chat.git
cd django-webrtc-chat
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

### 6. Access the application

Open your browser and visit:  
`http://127.0.0.1:8000/`

---

## Usage

1. Open the site in two separate browser tabs or devices.
    
2. Click **Find Stranger** on both.
    
3. Once connected, both users can see each other’s video streams and chat in real-time.
    

---

## Future Enhancements

- Add room-based matching or group calls
    
- Integrate authentication and user profiles
    
- Enable text chat history with database storage
    
- Deploy to production using Docker + Nginx + Redis
    

---

## License

This project is open source under the **MIT License**.
