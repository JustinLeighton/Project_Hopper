import sys
import click  # Importing Click instead of Typer
from config import load_settings, write_settings, clean_setting_input
from gui import display_projects


@click.group()
def cli():
    pass


@cli.command()
@click.argument("message")
def echo(message: str):
    click.echo(message)


@cli.command()
@click.argument("key")
@click.argument("value")
def set(key: str, value: str):
    settings = load_settings()
    clean_value = clean_setting_input(value)
    if key in settings:
        settings[key] = clean_value
        write_settings(settings)
        click.echo(f"{key} set to {value}")
    else:
        click.echo("key not found")


@cli.command()
@click.argument("key")
def get(key: str):
    settings = load_settings()
    if key in settings:
        click.echo(settings[key])
    else:
        click.echo("key not found")


def main():
    settings = load_settings()
    directory = settings["directory"]
    callback = settings["callback"]
    display_projects(directory=directory, callback=callback)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        cli()
