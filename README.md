# 📍 School Student Monitoring System using Geofencing

A real-time IoT-based student monitoring system that uses GPS and geofencing technology to track students' locations and automatically detect whether they are inside or outside predefined school and route boundaries. The system provides a web dashboard for administrators to manage students, create geofences, monitor live locations, and maintain movement logs.

---

## 🚀 Features

- 📍 Real-time GPS tracking
- 🗺️ Interactive map using Leaflet.js
- 🚸 Route Geofence Monitoring
- 🏫 Classroom Geofence Detection
- 👨‍🎓 Student Registration and Management
- 📡 Live location updates from IoT device
- 📊 Automatic Entry and Exit Detection
- 📜 Live Movement Logs
- 📥 Export logs to CSV
- 🌐 Responsive Web Dashboard

---

# 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Leaflet.js
- Leaflet Draw
- Turf.js

### Backend
- Python
- Flask
- Flask-CORS

### Database
- SQLite

### Communication
- REST API (HTTP)

---

# 🔧 Hardware Used

- ESP8266 WiFi Module
- NEO-6M GPS Module
- Mobile Hotspot / WiFi
- Laptop/Desktop (Dashboard)

---

# 📂 Project Structure

```
School-Monitoring-System
│
├── index.html          # Frontend Dashboard
├── server.py           # Flask Backend
├── locations.db        # SQLite Database
├── README.md
└── screenshots
    ├── dashboard.png
    ├── tracking.png
    └── logs.png
```

---

# ⚙️ How It Works

1. Register a student in the dashboard.
2. Create Route and Classroom geofences.
3. ESP8266 continuously reads GPS coordinates.
4. GPS coordinates are sent to the Flask server.
5. The dashboard retrieves the latest location.
6. The system checks whether the student is inside or outside the geofence.
7. Entry and exit events are automatically logged.
8. Administrators can export movement history as CSV.

---

# 📷 Dashboard Modules

- Student Management
- Geofence Creation
- Live GPS Tracking
- Route Status Indicator
- Classroom Detection
- Event Logs
- CSV Export

---

# 📊 Applications

- Smart Schools
- Student Safety Monitoring
- School Transportation
- Attendance Assistance
- Smart Campus Management

---

# ✅ Advantages

- Improves student safety
- Real-time monitoring
- Automatic geofence alerts
- Easy-to-use interface
- Low-cost implementation
- Lightweight web application
- Easy to expand for multiple schools

---

# 🚀 Future Enhancements

- Parent Mobile Application
- SMS/Email Notifications
- Push Notifications
- Cloud Database (Firebase/MongoDB)
- Google Maps Integration
- AI-based Route Prediction
- Attendance Automation
- RFID Integration
- Multiple School Management
- Admin Login & Authentication

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/your-username/School-Monitoring-System.git
```

Install dependencies

```bash
pip install flask flask-cors
```

Run the backend server

```bash
python server.py
```

Open the dashboard by launching **index.html** in your browser.

---

# 📚 Skills Demonstrated

- IoT System Development
- GPS Tracking
- Geofencing
- Flask Backend Development
- REST API Development
- JavaScript Programming
- SQLite Database
- Interactive Maps
- Frontend Development

---

# 👨‍💻 Author

**Mukesh M**

B.Tech – Electronics and Communication Engineering

Sri Manakula Vinayagar Engineering College

📧 Email: mukeshmuniraj2005@gmail.com

🔗 GitHub: https://github.com/Mukesh02-tech

🔗 LinkedIn: *(Add your LinkedIn profile URL)*

---

## ⭐ Star this repository if you found it useful!
