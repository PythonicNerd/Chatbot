import random
import time

class Bot: #This will be our main class that will hold all that we need for the bot
  
  def __init__(self):
    self.data = open("knowledge","r+")
    #getting info about the user
    self.name = ""
    self.age=""
    self.fv_color=""
    
    #geting info from file
    for line in data.readlines():
      key = line[0:2].lower()
      if key == "fvc":
        self.fv_color = line[2:len(line)]
    
