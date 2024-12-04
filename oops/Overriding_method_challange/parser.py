import re

#`TODO 1 - Create Parser class which has text attribute` 
class Partser:
    
    def __init__(self,text):
        self.text=text
    #TODO 2 - Create email parser method using regular expressions to find emails` 
    
    def email(self):
        match=re.search(r'[a-z0-9.\-+]+@[a-z0-9.\-+]+\.[a-z]+',self.text)
        if match:
            return match.group(0)
        return None
