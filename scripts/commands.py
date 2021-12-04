# %%

import os
import typing
import shutil

from scripts import db
from scripts import tiddlers as td
from scripts.configuration import Configuration


def add_tiddlers():
    
    configuration = Configuration()
    
    tiddlers_directory = os.path.join(configuration.source_directory(), 'tiddlers')
    tw_directory = os.path.join(configuration.source_directory(), 'tw')        
    tw_name = configuration.tw_name() + '.html'
    tw_base_name = tw_name + '.base'
    new_tw_name = 'new_' + tw_name
    
    base_html_file = os.path.join(tw_directory, tw_base_name) 
    new_html_file = os.path.join(configuration.temp_directory(), new_tw_name)    
    
    tiddlers = db.load_tiddlers(tiddlers_directory)    
    td.upload_tiddlers(base_html_file, tiddlers, new_html_file)
        
    tw_html_file = os.path.join(tw_directory, tw_name)    
    shutil.copyfile(new_html_file, tw_html_file)
    
    
def retrieve_tiddlers():
    
    configuration = Configuration()
    
    tiddlers_directory = os.path.join(configuration.source_directory(), 'tiddlers')
    tw_directory = os.path.join(configuration.source_directory(), 'tw')        
    tw_name = configuration.tw_name() + '.html'
    source_tw_name = 'source_' + tw_name 
    
    tw_html_file = os.path.join(tw_directory, tw_name)    
    copied_html_file = os.path.join(configuration.temp_directory(), source_tw_name)        
    
    shutil.copyfile(tw_html_file, copied_html_file)          
    tiddlers = td.extract_tiddlers(copied_html_file)        
    db.save_tiddlers(tiddlers, tiddlers_directory)
