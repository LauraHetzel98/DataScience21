
class ListKeeper:
#initialize dicionary
    def __init__(self): 
        self.dictionary=dict()
        self.dictionary["example"]=[1,2,3,4,5]
    
#show list
    def show(self):
          return self.dictionary.keys()
#show whole list
    def showwhole(self):
          return self.dictionary
#add list        
    def add(self, name, liste):
        self.dictionary[name] = liste
#delete list    
    def delete(self, name):
        self.dictionary.pop(name)
#sort list        
    def sort(self,name):
        self.dictionary[name].sort()

#append vaules to list       
    def append(self,name,liste):
        self.dictionary[name].extend(liste)  
        
    