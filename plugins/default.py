#deafult.py
# Define our default class 
import pyalarmslib as lib

class Plugin:
    # Define static method, so no self parameter 
    def process(self, cfg):
        # Some prints to identify which plugin is been used
        lib.log("default plugin START") 
        myconf = cfg["plugins"]["pa_default"]
        
        lib.log("pa_default Configuration Loaded") 
        enable = myconf["enable"]
        if (not enable):
            lib.log("pa_default plugin END") 
            return;
        
        lib.log("pa_default plugin ENABLED") 
        lib.log("default plugin configurations is: "+str(myconf)) 
        lib.log("default plugin END") 
