
# Task Management Dashboard

A simple web-based task management application that allows users to manage tasks, view task details, add new tasks, and update or delete them. The system includes different user views for managing tasks and includes a "Thank You" page upon successful task submission.

## Features

- **View Tasks**: Display all tasks with details like name, status, priority, due date, and description.
- **Add Tasks**: Allows users to add new tasks via a form.
- **Edit Tasks**: Edit the name, status, priority, due date, and description of existing tasks.
- **Delete Tasks**: Remove tasks from the system.
- **Thank You Page**: A page confirming task submission.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Database**: SQLite (by default, but can be switched to other databases)
- **Version Control**: Git

## Installation

### Prerequisites

- Python 3.x
- Django 5.x (or higher)
- Basic understanding of Django for extending functionality.

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task-management.git
   cd task-management
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scriptsctivate  # For Windows
   ```


3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to:
   ```bash
   http://127.0.0.1:8000/
   ```

### Project Structure

```plaintext
.
├── README.md
└── Task_Management
    ├── Main_files
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-312.pyc
    │   │   ├── admin.cpython-312.pyc
    │   │   ├── apps.cpython-312.pyc
    │   │   ├── forms.cpython-312.pyc
    │   │   ├── models.cpython-312.pyc
    │   │   └── views.cpython-312.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-312.pyc
    │   │       └── __init__.cpython-312.pyc
    │   ├── models.py
    │   ├── static
    │   │   ├── css
    │   │   │   ├── Add_task.css
    │   │   │   ├── Homes.css
    │   │   │   └── Task.css
    │   │   └── js
    │   │       └── script.js
    │   ├── templates
    │   │   ├── Add_task.html
    │   │   ├── Edit_task.html
    │   │   ├── Home.html
    │   │   ├── Task.html
    │   │   └── Thankyou.html
    │   ├── tests.py
    │   └── views.py
    ├── Task_Management
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-312.pyc
    │   │   ├── settings.cpython-312.pyc
    │   │   ├── urls.cpython-312.pyc
    │   │   └── wsgi.cpython-312.pyc
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    └── manage.py
```

## URLs and Views

1. **Home Page** (`/`):
   - Displays all tasks with their current status, priority, due date, and description.
   - Provides options to add, edit, or delete tasks.

2. **Task Page** (`/task/`):
   - Displays a table of all tasks with options to edit or delete.

3. **Add Task Page** (`/add_task/`):
   - A form to add new tasks with fields for name, description, priority, status, and due date.
   - Redirects to the "Thank You" page upon successful submission.

4. **Task Details Page** (`/task_detail/`):
   - Currently a placeholder for task details. Can be enhanced to show task-specific information.

5. **Thank You Page** (`/thank_you/`):
   - Displays a thank you message after a task has been successfully added.

## Adding New Features

1. **Add a Search Functionality**: Implement search functionality to filter tasks by name, status, or priority.
2. **Add User Authentication**: Allow users to log in and only see their tasks.
3. **Enhance Task Details Page**: Show more detailed information for each task, such as comments or history.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. Please ensure that your code adheres to the existing style and includes tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

© 2024 Ayuktha. All rights reserved.
