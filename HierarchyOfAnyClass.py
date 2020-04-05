"""
Created on Sun Apr  5 16:24:11 2020

@author: Shamita.Das
"""

def hierarchy(class__,space=0):
    print(space*' ',str(class__.__name__))
    
    if type(class__) is type:
        for subclass in class__.__subclasses__():
            hierarchy(subclass,space+4)
        
    
    
    
    
hierarchy(BaseException,space=0)#BaseException is parent for exception class
