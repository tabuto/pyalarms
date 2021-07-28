
import pyalarmslib as lib
import json

class Plugin:
    # Define static method, so no self parameter 
    def process(self, cfg):
        # Some prints to identify which plugin is been used
        lib.log("pa_bitcoin plugin START") 
        myconf = cfg["plugins"]["pa_bitcoin"]
        lib.log("pa_bitcoin Configuration Loaded") 
        
        enable = myconf["enable"]
        if (not enable):
            lib.log("pa_bitcoin plugin END") 
            return;
        
        lib.log("pa_bitcoin plugin ENABLED") 
        lib.log("pa_bitcoin configurations is: "+str(myconf)) 
        
        
        min_val = myconf["min_val"]
        max_val = myconf["max_val"]
        valuta=myconf["type"]
        
        url="https://api.coindesk.com/v1/bpi/currentprice.json"
        resp = lib.get_url(url)
        bitcoinMap = json.loads(str(resp))
        price = float(bitcoinMap["bpi"][valuta]["rate"].replace(",","") )
        
        lib.log("pa_bitcoin "+ valuta  +" price: "+str(price))
        
        if(price>=max_val):
             lib.send_message("Bitcoin value reach uppperbound limit: "+price, cfg["TELEGRAM_TOKEN"],cfg["TELEGRAM_CHAT_ID"])

        if(price<=min_val):
             lib.send_message("Bitcoin value reach lowerbound limit: "+price, cfg["TELEGRAM_TOKEN"],cfg["TELEGRAM_CHAT_ID"])
             
        lib.log("pa_bitcoin plugin END") 
        
       
        
        
        
