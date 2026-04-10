# UML Diagrams

## Use Case

Guest users can browse the feed, view individual projects, see the celebration wall, and register.

Once logged in, a developer can create and manage their own projects, add milestones, post comments on any project, and send a collaboration request to join someone else's project.

        [ Guest ]                      [ Developer ]
             |                              |
     ________|________           ___________|__________
    |        |        |         |      |       |       |
 View      View    Register  Create  Comment   Raise   Add                                                   
Feed      Project            project           hand   milestone


---

## Class Diagram

CustomUser

username
email
password (hashed)
bio
github_url
linkedin_url
|
| 1 to many
|
Project

title
description
status (planning / in_progress / completed)
tech_stack
github_url
owner → CustomUser
|
| 1 to many (3 directions)
|
|______________
|            |            |
Milestone   Comment    CollabRequest


title     - body      - message
due_date  - author    - requester
is_done   - project   - status (pending/accepted/rejected)


---

## Sequence — Login
User fills in login form
→ auth.js collects username + password
→ api.js sends POST to /api/v1/auth/login/
→ Django checks credentials
→ returns access + refresh tokens
→ tokens saved to localStorage
→ user redirected to dashboard

---

## Sequence — Create a Project
User fills in project form on dashboard
→ dashboard.js collects form data
→ api.js sends POST to /api/v1/projects/ with Bearer token
→ Django validates the token
→ checks the user is authenticated
→ saves the project to PostgreSQL
→ returns 201
→ dashboard.js re-renders the project list

