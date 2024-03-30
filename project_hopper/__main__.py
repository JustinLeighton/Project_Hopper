import sys
import click  # Importing Click instead of Typer
from .config import load_settings, write_settings, clean_setting_input, validate_settings_values
from .gui import display_projects

@click.group()
def cli():
    """This is the main command group."""


@cli.command()
@click.argument("message", nargs=-1)
def echo(message: tuple[str]):
    """Prints the provided message.

    Args:
        message (tuple[str]): Message to echo back
    """
    click.echo(' '.join(message))


@cli.command()
@click.argument("key")
@click.argument("value")
def set(key: str, value: str):
    """Sets a configuration value.

    Args:
        key (str): Either "directory" or "executable"
        value (str): path to either key
    """
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
    """Gets a configuration value.

    Args:
        key (str): Either "directory" or "executable"
    """
    settings = load_settings()
    if key in settings:
        click.echo(settings[key])
    else:
        click.echo("key not found")


def default():
    settings = load_settings()
    directory = settings["directory"]
    executable = settings["executable"]
    validate_settings_values(settings)
    display_projects(directory=directory, executable=executable)




def main():
    if len(sys.argv) == 1:
        default()
    else:
        cli()


if __name__ == "__main__":
    main()
