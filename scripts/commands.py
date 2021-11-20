# %%

import os
import typing
from string import Template   
import yaml
import shutil
from bs4 import BeautifulSoup

from scripts import db
from scripts import tiddlers as td


def add_tiddlers():

    CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
       
    ROOT_DIRECTORY = os.path.dirname(CURRENT_DIRECTORY)    
    TEMP_DIRECTORY =  os.path.join(ROOT_DIRECTORY, 'tmp') 
    TW_DIRECTORY = os.path.join(ROOT_DIRECTORY, 'db', 'tw')
    
    tiddlers_directory = os.path.join(ROOT_DIRECTORY, 'db', 'tiddlers')
    tiddlers = db.load_tiddlers(tiddlers_directory)
    
    base_html_file = os.path.join(TW_DIRECTORY, 'sgb.html.base')    
    new_html_file = os.path.join(TEMP_DIRECTORY, 'new_sgb.html')    
    td.upload_tiddlers(base_html_file, tiddlers, new_html_file)
        
    tw_html_file = os.path.join(TW_DIRECTORY, 'sgb.html')    
    shutil.copyfile(new_html_file, tw_html_file)
    
    
def retrieve_tiddlers():

    CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    
    ROOT_DIRECTORY = os.path.dirname(CURRENT_DIRECTORY)
    TEMP_DIRECTORY =  os.path.join(ROOT_DIRECTORY, 'tmp')    
    TW_DIRECTORY = os.path.join(ROOT_DIRECTORY, 'db', 'tw')
        
    tw_html_file = os.path.join(TW_DIRECTORY, 'sgb.html')    
    copied_html_file = os.path.join(TEMP_DIRECTORY, 'source_sgb.html')        
    shutil.copyfile(tw_html_file, copied_html_file)
          
    tiddlers = td.extract_tiddlers(copied_html_file)    
    tiddlers_directory = os.path.join(ROOT_DIRECTORY, 'db', 'tiddlers')
    db.save_tiddlers(tiddlers, tiddlers_directory)

