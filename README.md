# Nature Ninjas

## Prerequisites

Ensure you have the following installed:

- **Python 3.8+**: Check your version using `python --version`.
- **pip**: Included with Python installations.
- **Virtual Environment**: `venv` is built into Python.

---

## Setup Instructions

### 1. Clone the Repository

Run the following commands in your terminal:

```bash
git clone https://github.com/username/nature-ninjas.git
cd nature-ninjas
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment to ensure project-specific dependencies are used:

```bash
venv\Scripts\activate
```

### 4. Install Project Dependencies

Use the `requirements.txt` file to install all required Python packages:

```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations

Ensure the database is initialized and ready by running the migrations:

```bash
cd natureNinjas
python manage.py migrate
```
### 6. Install Tailwind
Install tailwind and other npm dependencies
```
npm install
```

### 6. Start the Development Server

Run the Django development server to serve the project locally, make sure you're in *natureNinjas* directory:

```bash
npm run start
```

Visit the following URL to access the project: [http://127.0.0.1:8000](http://127.0.0.1:8000).
