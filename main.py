import random
import time

class Bot: #This will be our main class that will hold all that we need for the bot
  
  def __init__(self):
    self.data = open("knowledge","r+")
    self.data_lines = self.data.readlines()
    #getting info about the user
    
    
    #geting info from file
    for line in data.readlines():
      self.line = line
    
      self.fv_color = self.grab("fvc")
      self.name = self.grab("nme")
      self.age = self.grab("age")
      self.ses = int(self.grab("ses"))
      if self.ses:
        ses_line = line
      
    self.ses += 1 #Litterally just finds out if your on your first session
    self.data_line[ses_line] = self.ses + /n
    
    if self.ses == 1:
      for i in self.dataList:
        i = "Unknown"
      
    
  def grab(self,keywd):
    key = self.line[0:3]
    if key == keywd and self.line[3] == ":":
      info = self.line[4:len(self.line)]
      return info
      
  def findUndefined(self):
    for items in self.data:
      if items = "":
        self.undefinedList.append(items)
      
