import importlib
import  plugins.default

class PyAlarms:
    def __init__(self, plugins=[]):
        # Checking if plugin were sent
        if plugins != []:
            # create a list of plugins
            self._plugins = [
                # Import the module and initialise it at the same time
                importlib.import_module(plugin,".").Plugin() for plugin in plugins
            ]
        else:
            # If no plugin were set we use our default
            self._plugins = [importlib.import_module('plugins.default',".") .Plugin()]
    # This method will print the workflow of our application
    def run(self):
        print("Starting PyAlarms")
        print("-" * 10)
        print("This is my core system")

        # We is were magic happens, and all the plugins are going to be printed
        for plugin in self._plugins:
            plugin.process(5,3)

        print("-" * 10)
        print("Ending PyAlarms")
        print() 
