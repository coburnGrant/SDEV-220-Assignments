# Book API Lab

## Setup

Create python virtual environment
```bash
python -m venv .venv
```

```bash
pip install -r requirements.txt
```

Set environment variables

```bash
export FLASK_APP=app.py
```

```bash
export FLASK_ENV=development
```

Create books initial database
```bash
python init_db.py
```

## Run

Run the application using `flask`

```bash
flask run
```

