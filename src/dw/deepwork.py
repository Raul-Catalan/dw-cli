import time
import typer
from rich.live import Live
from rich.text import Text
from datetime import timedelta

app = typer.Typer()

DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'

# TODO: Create Textual TUI for deep work
@app.command()
def start():
    duration = timedelta(hours=0.5)
    text = Text()
    with Live(text, auto_refresh=False) as live:  # update 4 times a second to feel fluid
        for remaining in range(int(duration.total_seconds()), -1, -1):
            min, sec = divmod(remaining, 60)
            time_text = Text(f"{min:02d}:{sec:02d}")
            live.update(time_text, refresh=True)
            time.sleep(1)
        live.update(Text("Finished"))
    print(f"Finished {duration}")

if __name__ == "__main__":
    app()
