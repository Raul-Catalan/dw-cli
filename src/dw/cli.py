import typer

import database
import deepwork

app = typer.Typer()
# TODO: Clean up and order commands
app.add_typer(database.app, name="database")
app.add_typer(deepwork.app, name="deepwork")

if __name__ == "__main__":
    app()
