import typer

from .deepwork import deep

app = typer.Typer()
app.command()(deep)

if __name__ == "__main__":
    app()
