# projectmlh (Mobile Local Helper)

A web platform to connect patients in need of domestic care with local helpers (nurses, caretakers, etc.) in their region.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How It Works (Example Scenario)](#how-it-works-example-scenario)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Database Persistence (Why use a Persistent Volume?)](#database-persistence-why-use-a-persistent-volume)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Introduction

**The Problem:**  
Domestic nursing care has become increasingly necessary, especially after COVID-19. Helpers (nurses, caretakers) often struggle to find good and convenient opportunities. Meanwhile, patients/families also have a hard time finding available and trustworthy helpers.

**The Solution:**  
**projectmlh** bridges this gap by connecting patients and helpers within a specific region, making it easier for both sides to find each other and arrange care.

![App Screenshot](https://github.com/parth721/projectmlh/assets/112557191/c78378a2-1b0b-48d0-b992-67b8fff59be7)

---

## Features

- Patient and Helper registration & login
- Helper profile creation (skills, experience, availability)
- Patients can post care requests and search for helpers
- In-app communication for requirement discussion and bookings
- Responsive web design (works on mobile/desktop)
- Data persistence even if the app restarts (details below)

---

## How It Works (Example Scenario)

1. **Helper joins:**  
   Priya is a nurse looking for local work opportunities. She registers as a Helper, creates her profile with her skills, experience, and available timings.

2. **Patient posts a request:**  
   Mr. Sharma needs post-surgery care at home. He registers as a Patient and posts his requirements on the platform.

3. **Matching and booking:**  
   Mr. Sharma searches for helpers in his area and finds Priya’s profile. He messages her to discuss details and they arrange a booking.

---

## Tech Stack

- **Backend:** Django (Python web framework)
- **Frontend:** Bootstrap (responsive design)
- **Database:** SQLite (user and booking info)
- **Containerization:** Docker (for easy setup and deployment)
- **Orchestration:** Minikube (Kubernetes for local development)
- **Data Persistence:** Persistent Volume (so you never lose user info if the app restarts!)

---

## Prerequisites

- Python 3.11
- Minikube
- Docker
- Git (optional, but recommended)

---

## Setup and Installation

### 1. Fork & Clone the repo
```sh
git clone https://github.com/parth721/mlh.git
cd mlh
```

### 2. Set up a virtual environment & install dependencies
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Local development (without Docker/K8s)
```sh
python3 manage.py runserver
```
Visit [http://localhost:8000](http://localhost:8000) in your browser.

### 4. With Docker & Minikube (recommended for deployment)
- Start minikube
- Build and deploy using your YAML files (pods, services, volumes).
- Check status of pods/services
- Run the app in the cluster:
  ```sh
  minikube service <service-name>
  ```

### 5. Try it with DockerHub image
- Pull the image from DockerHub
- Deploy it on Minikube
- Follow steps 1, 2, and then 6–9 from above setup instructions

![App Screenshot](https://github.com/parth721/projectmlh/assets/112557191/c1a8812e-0f51-467e-98b7-e2f71402046a)

---

## Usage

### 1. User Registration & Login
- Register as either a Patient or a Helper.
- Login is required to access platform features.

### 2. Helper Profile Creation
- Helpers can create profiles detailing their skills, experience, qualifications, and availability.

### 3. Search & Find Helpers
- Patients post requests with their care needs and availability.
- Search for matching Helpers based on location, skills, and availability.

### 4. Communication & Booking
- In-app messaging lets Patients and Helpers discuss needs and arrange bookings.

---

## Database Persistence (Why use a Persistent Volume?)

**What is a Persistent Volume (PV)?**  
In Kubernetes (Minikube), a Persistent Volume is like a USB drive attached to your application’s container. It stores important data—like your user info or bookings—outside the app itself.

**Why is this important?**  
If your app crashes or you update/restart the container (which happens a lot in the real world), all data inside the container would normally be lost. By keeping the SQLite database in a Persistent Volume, all user information and bookings are safe and survive restarts or crashes.

**Example scenario:**  
Suppose your app is running in a pod and users have registered/booked helpers. If the pod crashes, without a PV, all that data is gone! With a PV, the pod can restart and reconnect to the same database, so users don’t lose anything.

**How do we do this?**  
- The SQLite database file is stored in a directory mounted to a Persistent Volume.
- Your Kubernetes YAML files (for deployment) specify this mount.
- When you redeploy, your data is still there!

---

## Contributing

Want to improve the project? Here’s how:
1. Fork this repo
2. Clone your fork
3. Make changes (follow steps in Setup above)
4. Test your changes
5. Create a pull request with your improvements

---

## Contact

Maintainer: [@parth721](https://github.com/parth721)  
If you have questions or suggestions, feel free to open an issue or reach out.

---

## License

[MIT License](LICENSE)

