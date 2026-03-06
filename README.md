# Slot Booking System

A full-stack web application built using **Django** and **MySQL** that allows users to view available service slots, filter services, and book appointments through a responsive and user-friendly interface.

---

## Features

- View available service slots
- Book slots instantly
- View booked slots
- Filter slots by service
- Responsive UI using Bootstrap
- MySQL database integration

---

## Tech Stack

**Backend**
- Django

**Frontend**
- HTML
- CSS
- Bootstrap

**Database**
- MySQL

**Environment Variables**
- python-dotenv

---

## Project Structure
slotbooking/
│
├── booking/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
│ └── templates/
│ ├── base.html
│ ├── slots.html
│ └── booked_slots.html
│
├── slotbooking/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
├── requirements.txt
├── Procfile
└── README.md
## Installation

### Clone the repository


git clone https://github.com/rahulpenta23/Task.git

cd slotbooking

### Install dependencies


pip install -r requirements.txt


### Configure environment variables

Create a `.env` file in the root directory:


SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=testdb
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306

## Deployment

This project is deployed in - Railway platform 

