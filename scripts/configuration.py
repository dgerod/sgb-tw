import os

class Configuration:

    def __init__(self):    
        
        CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) 
        
        self.root_directory = os.path.dirname(CURRENT_DIRECTORY)              
        self.tmp_directory = os.path.join(self.root_directory, 'tmp') 
        self.tiddlers_directory = os.path.join(self.root_directory, 'db', 'tiddlers')
        self.tw_directory = os.path.join(self.root_directory, 'db', 'tw')
