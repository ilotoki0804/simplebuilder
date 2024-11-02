from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class MyBuildHook(BuildHookInterface):
    PLUGIN_NAME = 'simplebuilder'

    def initialize(self, version, build_data):
        # Initialization code here
        print(f"Initializing build for version {version}")

    def finalize(self, version, build_data, artifact_path):
        # Finalization code here
        print(f"Finalizing build for version {version}")
