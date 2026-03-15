# AI Log Analyzer

AI Log Analyzer is a Django-based backend application that analyzes server log files and generates structured insights. The system allows users to upload log files through REST APIs, parses log entries, detects errors, and provides analytical summaries such as total errors, warnings, and the most frequent issue.

This project simulates a simplified log monitoring system similar to tools used in production environments.

---

## Features

* Upload server log files through REST APIs
* Parse log entries automatically
* Detect **ERROR, WARNING, and INFO** logs
* Identify the **most frequent error**
* Generate structured log analytics
* Store uploaded log files in a database

---

## Tech Stack

* **Python**
* **Django**
* **Django REST Framework**
* **SQLite**
* **Pandas (for log analytics)**

---

## Project Structure

ai_log_analyzer/

├── manage.py
├── analyzer/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── log_parser.py
│   ├── error_detector.py
│   ├── urls.py
│
├── ai_log_analyzer/
│   ├── settings.py
│   ├── urls.py
│
└── media/
  └── logs/

---

## Installation

Clone the repository:

```id="x34kq8"
git clone https://github.com/YOUR_USERNAME/ai-log-analyzer.git
```

Navigate into the project:

```id="7xw6d3"
cd ai-log-analyzer
```

Create virtual environment:

```id="6u0d4p"
python -m venv venv
```

Activate virtual environment:

Windows:

```id="z5j2gn"
venv\Scripts\activate
```

Install dependencies:

```id="m4nq29"
pip install django djangorestframework pandas
```

Run database migrations:

```id="g4yq1k"
python manage.py migrate
```

---

## Running the Server

Start the development server:

```id="c9nd81"
python manage.py runserver
```

Open in browser:

```id="u7m1bc"
http://127.0.0.1:8000
```

---

## API Endpoints

### Upload Log File

```id="c9e6lf"
POST /api/upload-log/
```

Upload a `.log` file using **multipart/form-data**.

Example Response:

```json id="o4e9ml"
{
 "message": "Log uploaded successfully",
 "log_id": 1
}
```

---

### Get Log Analysis

```id="4nq3p7"
GET /api/log-summary/<log_id>/
```

Example Response:

```json id="2jcl3x"
{
 "total_errors": 3,
 "most_common_error": "Database connection timeout",
 "error_count": 2,
 "warnings": 1,
 "info_logs": 2
}
```

---

## Example Log File

```id="0z9e0a"
INFO: Server started
ERROR: Database connection timeout
ERROR: Database connection timeout
WARNING: Slow API response
INFO: User login successful
ERROR: Null pointer exception
```

---

## Learning Outcomes

This project demonstrates:

* Django backend development
* REST API design using Django REST Framework
* File upload handling in web applications
* Log parsing and pattern detection
* Backend data processing and analytics

---

## Future Improvements

* Top 5 most frequent error detection
* Error frequency visualization using charts
* Real-time log monitoring dashboard
* Machine learning based anomaly detection

---

## Author

Rohit Saini
Computer Engineering Student | Backend Development | Python
