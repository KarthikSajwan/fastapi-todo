# fastapi-todo

A feature-rich To-Do application built with FastAPI, SQLAlchemy, and Jinja2 templates. This app supports user authentication, admin management, and a modern, interactive front-end.

## Features

- **User Authentication:** Secure login/logout and protected routes.
- **CRUD Operations:** Create, read, update, and delete todos.
- **User Profile Management:** Change password and update phone number.
- **Admin Controls:** Admin can view and delete todos from all users.
- **Priority & Completion:** Todos have priority levels and a completion status.
- **Beautiful UI:** Responsive pages with Bootstrap, custom templates, and interactive JavaScript.
- **Data Persistence:** Uses PostgreSQL by default (see `database.py`).

## Data Models

### Users

- `id`: int (primary key)
- `email`, `username`, `first_name`, `last_name`
- `hashed_password`
- `role`: "user" or "admin"
- `phone_number`
- `is_active`: bool

### Todos

- `id`: int (primary key)
- `title`, `description`
- `priority`: 1–5
- `complete`: bool
- `owner_id`: ForeignKey to Users

## API Endpoints

### Auth (see `routers/auth.py`)
- `/auth/login-page` – Login form (HTML)
- `/auth/register-page` – Registration form (HTML)
- `/auth/login` – Login (POST)
- `/auth/register` – Register (POST)
- `/auth/logout` – Logout (GET)

### Todos (see `routers/todos.py`)
- `/todos/todo-page` – Main todos page (HTML)
- `/todos/add-todo-page` – Add todo form (HTML)
- `/todos/edit-todo-page/{todo_id}` – Edit todo form (HTML)
- `/todos/` – Get all todos for current user (GET, JSON)
- `/todos/{todo_id}` – Get a single todo by ID (GET, JSON)
- `/todos/todo` – Create a todo (POST, JSON)
- `/todos/todo/{todo_id}` – Update a todo (PUT, JSON)
- `/todos/todo/{todo_id}` – Delete a todo (DELETE)

### Users (see `routers/users.py`)
- `/user/` – Get current user's profile (GET)
- `/user/password` – Change password (PUT)
- `/user/phoneNumber` – Update phone number (PUT)

### Admin (see `routers/admin.py`)
- `/admin/todo` – Get all todos (GET, admin only)
- `/admin/todo/{todo_id}` – Delete any todo (DELETE, admin only)

## Front-End

- Jinja2 templates in `/templates/`
- Bootstrap UI components
- Interactive JS in `/static/js/base.js` (handles add/edit via AJAX)
- Pages: `home.html`, `todo.html`, `add-todo.html`, `edit-todo.html`, etc.

## Database

- Default: PostgreSQL (`database.py` has connection string)
- Models defined in `models.py`
- SQLAlchemy ORM

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL (or adjust for SQLite in `database.py`)
- pip

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/KarthikSajwan/fastapi-todo.git
   cd fastapi-todo
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create and configure your PostgreSQL database (or use SQLite).
4. Update connection string in `database.py` if needed.
5. Run:
   ```bash
   uvicorn main:app --reload
   ```

6. Visit [http://localhost:8000](http://localhost:8000).

## Example Usage

### Create a Todo (JSON API)
```bash
curl -X POST "http://localhost:8000/todos/todo" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","description":"Get 2L milk","priority":2,"complete":false}'
```

### Change Password
```bash
curl -X PUT "http://localhost:8000/user/password" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"password":"oldpass","new_password":"newpass123"}'
```



## Author
Karthik Sajwan
