# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:11:48 2018

@author: dhana
"""

class StringDemo():
    
    def getString(self):
        self.val=input("What is you're name: ")
        self.s=''.join(self.val.split())
        #print(self.s)
        
    def printString(self):
        print(self.s.upper())
        

if __name__=="__main__":
    d=StringDemo()
    d.getString()
    d.printString()