import random
import time

class Bot: #This will be our main class that will hold all that we need for the bot
  
  def __init__(self):
    self.data = open("knowledge","r+")
    #getting info about the user
    self.name = ""
    self.age=""
    self.fv_color=""
    self.undefinedList = []
    
    #geting info from file
    for line in data.readlines():
      self.line = line
    
      self.fv_color = self.grab("fvc")
      self.name = self.grab("nme")
      self.age = self.grab("age")
      
    
  def grab(self,keywd):
    key = self.line[0:3]
    if key == keywd and self.line[3] == ":":
      info = self.line[4:len(self.line)]
      return info
      
  def findUndefined(self):
    for items in self.data:
      if items = "":
        self.undefinedList.append(items)
      
