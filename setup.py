from setuptools import setup

setup(
    name="projecthopper",
    version="0.1.0",
    packages=["projecthopper"],
    entry_points={"console_scripts": ["dev = projecthopper.__main__:main"]},
)
