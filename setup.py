from setuptools import setup, find_packages

setup(
    name="Project Hopper",
    version="0.2.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dev = project_hopper.__main__:main"
        ],
    },
)
