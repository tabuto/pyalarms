#main.py
# This is a main file which will initialise and execute the run method of our application

# Importing our application file
from pyalarms import PyAlarms

if __name__ == "__main__":
    # Initialising our application
    app = PyAlarms() 
    # Running our application 
    app.run()  
