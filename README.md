# Mzansi Builds

A platform for developers to build in public. Share what you're working on, log your progress, leave comments on other people's projects, and celebrate when something ships.

Built as a technical assessment for Derivco.

![CI/CD](https://github.com/Reabetsweeee/derivco_code_skills/actions/workflows/ci.yml/badge.svg)

---

## Why I built it this way

I wanted the architecture to be simple and honest. Django handles the API and auth, PostgreSQL stores everything, and the frontend is plain HTML/CSS/JS — no framework overhead. Each Django app has one job and one job only, which makes the codebase easy to navigate and extend.

---

## Stack

- Python / Django 6
- Django REST Framework
- PostgreSQL
- JWT authentication
- Vanilla JS (ES6 modules)
- GitHub Actions for CI/CD

---

## Setup

You'll need Python 3.12+, PostgreSQL, and Git.

```bash
git clone https://github.com/Reabetsweeee/derivco_code_skills.git
cd derivco_code_skills

python -m venv venv
venv\Scripts\activate

pip install -r backend/requirements.txt
```

Create a `.env` file inside `backend/`:
SECRET_KEY=pick-something-long-and-random
DEBUG=True
DB_NAME=mzansi_builds
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

Then:

```bash
cd backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `frontend/pages/index.html` with Live Server in VS Code.

---

## Running the tests

```bash
cd backend
python manage.py test --verbosity=2
```

17 tests, all green.

---

## Folder layout
derivco_code_skills/
├── .github/workflows/    # CI/CD
├── backend/
│   ├── users/            # registration, login, profiles
│   ├── projects/         # project CRUD, live feed, celebration wall
│   ├── interactions/     # comments and collab requests
│   ├── milestones/       # milestone tracking per project
│   └── mzansi_builds/    # settings and root urls
├── frontend/
│   ├── pages/            # HTML
│   ├── css/              # styling
│   └── js/               # one file per concern
└── docs/

---

## API

| Method | Endpoint | Needs login |
|---|---|---|
| POST | `/api/v1/auth/register/` | No |
| POST | `/api/v1/auth/login/` | No |
| GET | `/api/v1/projects/` | No |
| POST | `/api/v1/projects/` | Yes |
| GET | `/api/v1/projects/completed/` | No |
| POST | `/api/v1/interactions/<id>/comments/` | Yes |
| POST | `/api/v1/interactions/<id>/raise-hand/` | Yes |
| GET | `/api/v1/milestones/<id>/milestones/` | No |

---

## Security notes

Passwords never stored in plain text — Django handles hashing. Auth runs through JWT so the API is stateless. Every write endpoint checks that the request is coming from the owner of that resource. Secrets live in `.env` which is gitignored.

---

## CI/CD

Every push to main triggers the pipeline. It spins up a Postgres instance, installs dependencies, runs migrations, and runs the full test suite. If anything breaks the build stops.