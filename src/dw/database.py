import api
import os
import typer
from rich import print
from datetime import datetime, timedelta

# TODO: Maybe put this in the .config
DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'

app = typer.Typer()

# Initialize Our Database Command
@app.command()
def init():
    api.init_database()
    print("Database Successfully Initialized")

# Add to Database
@app.command()
def add(date=None, total=1, start=None, end=None, type_of_work=None, description=None):
    if date == None:
        date = datetime.now()
        date = date.strftime(DATE_FORMAT)
    total_hours = timedelta(hours=int(total))

    api.create((date, total_hours.total_seconds(), start, end, type_of_work, description))

@app.command()
def hours(hours):
    h = timedelta(hours=int(hours))
    date = datetime.now()
    date = date.strftime(DATE_FORMAT)
    # TODO: I am thinking when we create this we will have some kind of autocomplete such as when we create a new repo in gh cli, and that will be the banner for the timer as they work on it to get this specific thing done
    api.create((date, h.total_seconds(), None, None, 'Deep', None))

@app.command()
def delete(id):
    api.delete(id)
    print(f"Entry {id} Deleted!")

@app.command()
def view():
    rows = api.read_all()
    print(rows)

# Dev Testing Function
@app.command()
def test():
    tests = [
    ("2025-10-01", 5, "14:10:11", "15:01:59"),
    ("2025-10-03", 2, "03:45:00", "04:20:17"),
    ("2025-10-05", 1, "07:10:42", "08:03:25"),
    ("2025-10-07", 3, "00:15:00", "01:45:33"),
    ("2025-10-08", 2, "10:10:10", "11:11:11"),
    ("2025-10-10", 4, "13:50:20", "14:05:00"),
    ("2025-10-11", 5, "18:00:30", "18:30:30"),
    ("2025-10-12", 2, "02:02:02", "03:03:03"),
    ("2025-10-13", 4, "20:45:20", "21:15:15"),
    ("2025-10-14", 10, "06:06:06", "07:07:07")
    ]
    print("Deep Work")
    init()
    for test in tests:
        add(test)
    api.update(1, ("2025-01-00", 7, "99:99:99", "99:99:99"))
    api.delete(2)
    view()
    os.remove("data.db")

if __name__ == "__main__":
    app()
