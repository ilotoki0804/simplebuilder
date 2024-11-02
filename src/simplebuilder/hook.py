from hatchling.plugin import hookimpl
from .plugin import MyBuildHook

@hookimpl
def hatch_register_build_hook():
    return MyBuildHook
