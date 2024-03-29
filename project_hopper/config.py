import json
import os


def get_settings_path() -> str:
    """
    Get the path to the settings JSON file located in the same directory as the script.

    Returns:
    - str: Path to the settings JSON file.
    """
    script_path: str = os.path.realpath(__file__)
    script_directory: str = os.path.dirname(script_path)
    settings_path = os.path.join(script_directory, "settings.json")
    return settings_path


def load_settings() -> dict[str, str]:
    """
    Load settings from a JSON file located in the same directory as the script.

    Returns:
    - dict[str, str]: Dictionary object representing the settings.
    """
    settings_path = get_settings_path()
    settings = read_settings(settings_path)
    validate_settings_keys(settings)
    return settings


def read_settings(file_path: str) -> dict[str, str]:
    """
    Read settings from a JSON file

    Args:
    - file_path (str): Path to the settings JSON file.

    Returns:
    - dict: Dictionary object representing the settings.
    """
    settings = {}
    with open(file_path, "r") as file:
        settings = json.load(file)
    validate_settings_keys(settings)
    return settings


def write_settings(data: dict[str, str]) -> None:
    """
    Write a dictionary to a JSON file.

    Args:
    - data (dict): Dictionary to be written to the JSON file.
    """
    settings_path = get_settings_path()
    with open(settings_path, "w") as file:
        json.dump(data, file)


def validate_settings_keys(settings: dict[str, str]) -> None:
    """
    Validate if specific keys are present in the settings dictionary.

    Args:
    - settings (dict[str, str]): Dictionary object representing the settings.

    Raises:
    - KeyError: If specific keys are missing in the settings object.
    """
    keys = ["directory", "callback"]
    missing_keys = [x for x in keys if x not in settings]
    if missing_keys:
        raise KeyError(f"The following key(s) is/are missing in the settings: {', '.join(missing_keys)}")


def clean_setting_input(input: str) -> str:
    """
    Clean the input string for settings.json

    Args:
    - input (str): The input string to be cleaned.

    Returns:
    - str: The cleaned string.
    """
    input = input.replace("/", "\\")
    return input
