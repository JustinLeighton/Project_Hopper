Project Hopper's purpose is to allow for easier 'hopping' between projects and project folders via a CLI tool with minimal typing. The goal is simply having to type 'dev' in order to jump into any IDE form within any project folder.

To start using, run setup to register the "dev" command.

```console
pip install .
```

Then set your paths for your project directory and IDE executable.

```console
dev set directory <PATH>
dev set executable <PATH>
```

Where 'directory' is the path to your folder which contains any number of project folders, and 'executable', for example the path to Code.Exe for VSCode. Now you can begin hopping between projects with ease by calling 'dev'. This will bring up a GUI listing sortable projects in your project folder. Double clicking a project will bring you straight into your IDE of choice within that project folder. This is essentially just a GUI wrapper for calling 'code <PATH>', but can be generalized outside of software IDEs into any software where it's useful to open from specific project folders.