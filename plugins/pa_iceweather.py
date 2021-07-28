import pyalarmslib as lib

class Plugin:
    # Define static method, so no self parameter 
    def process(self, cfg):
        # Some prints to identify which plugin is been used
        lib.log("pa_iceweather plugin START") 
        myconf = cfg["plugins"]["pa_iceweather"]
        
        lib.log("pa_iceweather Configuration Loaded") 
        enable = myconf["enable"]
        if (not enable):
            lib.log("pa_iceweather plugin END") 
            return;
        lib.log("pa_iceweather plugin ENABLED") 
        lib.log("pa_iceweather plugin  configurations is: "+str(myconf)) 
        lib.log("pa_iceweather plugin END") 
