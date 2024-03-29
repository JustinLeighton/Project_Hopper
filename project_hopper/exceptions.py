from click import UsageError

class ProjectHopperError(UsageError):
    """Custom base class"""
    pass

class InvalidProjectDirectory(ProjectHopperError):
    """Invalid project directory in settings.json"""
    pass

class InvalidExecutableProgram(ProjectHopperError):
    """Invalid executable in settings.json"""
    pass