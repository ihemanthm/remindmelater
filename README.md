
# Remind-me-later

Remind-me-later is a simple full-stack web application that allows users to set reminders with custom messages, dates, and times. The reminders can be sent via SMS or Email (message delivery not implemented in this version). This backend API is built using Django and Django REST Framework.

---

## Features

- Create reminders with a message, date, time, and reminder method (SMS or Email).
- Store reminders securely in a database.
- REST API endpoint to save reminders.
- Future-ready for extending delivery methods and frontend integrations.

---

## Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite (default Django database)

---

## Project Structure

```
remindmelater/
├── reminders/          # Django app containing models, views, serializers, urls
├── remindmelater/      # Project configuration
├── db.sqlite3          # SQLite database file
├── manage.py
├── requirements.txt    # (optional) dependencies
└── README.md
```

---

## Setup Instructions

### Prerequisites

- Python 3.8 or above installed on your system.
- `pip` package manager.

---

### Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/ihemanthm/remindmelater.git
cd remindmelater
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

3. **Install dependencies**

```bash
pip install django djangorestframework django-cors-headers
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create a superuser (optional for admin access)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

Your API will be accessible at `http://127.0.0.1:8000/`.

---

## API Endpoints

- **POST** `/api/reminder/`  
  Create a new reminder by sending JSON payload:

```json
{
  "message": "Doctor appointment",
  "date": "2025-05-20",
  "time": "14:00:00",
  "reminder_method": "EMAIL"
}
```

Response: `201 Created` with the saved reminder object.

- **GET** `/api/reminders/`  
  Get all reminders by sending a GET request.
Response: `200 OK` with a list of reminders.


---

## Testing with Postman

1. Start the Django server.
2. Create a POST request to `http://127.0.0.1:8000/api/reminder/`.
3. Set `Content-Type: application/json` header.
4. Use the sample JSON above as request body.
5. Send the request and check the response.

---

## Notes

- The app currently does **not** implement the actual sending of SMS or Email reminders.
- CORS is configured for local frontend development (e.g., React on `localhost:3000`).
- Extendable for additional reminder delivery methods.

---

## License

This project is open source and free to use under the MIT License.

---

Feel free to customize or ask if you want me to add instructions for deployment or frontend setup!
