# API Demo Tests

This project demonstrates the setup of robust API test automation, integrated with CI/CD pipelines, Allure reporting, and trend analysis.

---

## 📌 Project Goals

- Test critical backend API endpoints (e.g., login, profile updates)
- Early defect detection before frontend/UI work
- Full CI/CD integration with GitHub Actions
- Allure reporting and trend tracking
- Easy to extend and maintain

---

## ⚙️ Tech Stack

- **Python 3.11**
- **Pytest** — test runner
- **Allure-Pytest** — beautiful reporting
- **Requests** — HTTP client
- **dotenv** — environment variables management
- **GitHub Actions** — continuous integration and report publishing

---

## 🏧 Project Structure

```bash
api_demo_tests/
├── .github/workflows/          # GitHub Actions workflows (CI pipeline)
├── allure-results/             # Raw Allure results (generated)
├── allure-report/              # HTML Allure reports (generated)
├── assets/                     # Project assets (if needed)
├── tests/                      # Test cases
│   ├── test_client_login.py    # Login tests
│   └── test_client_profile.py  # Profile tests
├── conftest.py                  # Fixtures and configuration
├── requirements.txt             # Python dependencies
├── generate_allure_with_trend.sh # Local script to run tests and generate reports
└── README.md
```

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/evarnavs/api_demo_tests.git
cd api_demo_tests
```

### 2. Set up virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

Create a file called `.env` in the project root with the following content:

```env
BASE_URL=https://staging.usupport.online
EMAIL=your_test_email@example.com
PASSWORD=your_test_password
```

_(Never commit `.env` to GitHub!)_

---

## 🧺 Run Tests and Generate Allure Report Locally

Use the provided shell script:

```bash
bash generate_allure_with_trend.sh
```

This script will:
- Copy previous Allure history
- Run tests with Pytest
- Generate updated Allure report
- Open the report automatically in your browser

---

## 🔥 Continuous Integration

- Every `push` to `main` branch triggers GitHub Actions workflow
- Tests are run automatically
- Allure report is deployed to **GitHub Pages**

✅ [View the latest Allure Report](https://evarnavs.github.io/api_demo_tests/)

---

## 📄 License

This repository is currently intended for internal demonstration purposes.  

---

