#deafult.py
# Define our default class 
class Plugin:
    # Define static method, so no self parameter 
    def process(self, num1,num2):
        # Some prints to identify which plugin is been used
        print("This is my default plugin") 
        print("Check events are %d and %d",num1,num2) 
