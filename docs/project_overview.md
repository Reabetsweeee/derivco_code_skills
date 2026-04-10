# Mzansi Builds Project Overview

# What is Mzansi Builds?
A platform where South African developers build in public, track milestones, collaborate, and celebrate completed projects.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript (ES6 modules)
- **Backend:** Django 6 + Django REST Framework
- **Database:** PostgreSQL
- **Auth:** JWT tokens via djangorestframework-simplejwt
- **CI/CD:** GitHub Actions
- **Version Control:** Git + GitHub

## Modules
| Module | Responsibility |
|---|---|
| `users` | Registration, login, JWT auth, profiles |
| `projects` | CRUD, live feed, celebration wall |
| `interactions` | Comments, raise-hand collaboration |
| `milestones` | Project milestone tracking |

## Security
- Passwords hashed using Django PBKDF2
- JWT tokens for stateless authentication
- Owner-only permissions on all write endpoints
- Secrets managed via `.env` file

## API Endpoints
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/v1/auth/register/` | No | Register |
| POST | `/api/v1/auth/login/` | No | Login |
| GET | `/api/v1/projects/` | No | Live feed |
| POST | `/api/v1/projects/` | Yes | Create project |
| GET | `/api/v1/projects/completed/` | No | Celebration wall |
| POST | `/api/v1/interactions/<id>/comments/` | Yes | Post comment |
| POST | `/api/v1/interactions/<id>/raise-hand/` | Yes | Request collab |
| GET | `/api/v1/milestones/<id>/milestones/` | No | View milestones |

## Testing
- 17 unit tests across all 4 apps
- All tests pass 
- CI/CD runs tests on every push

## Git Workflow
- Feature branches for each module
- Meaningful commits using conventional commits
- CI/CD blocks merges if tests fail