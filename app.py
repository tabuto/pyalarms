#main.py
# This is a main file which will initialise and execute the run method of our application

# Importing our application file
from pyalarms import PyAlarms
import pyalarmslib as lib



if __name__ == "__main__":
	lib.log("INIT pyalarms")
	#load plugins
	plugins = lib.loadPlugins()
	cfg = lib.loadConfiguration()

	# Initialising our application
	app = PyAlarms( cfg, plugins ) 
	# Running our application 
	app.run()
	lib.log("CLOSE pyalarms")  
