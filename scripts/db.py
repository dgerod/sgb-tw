import os
import typing
import yaml


def load_tiddlers(tiddlers_directory: str) -> typing.List:
        
    tiddler_names = []
    [tiddler_names.append(os.path.splitext(_)[0]) 
         for _ in os.listdir(tiddlers_directory) if _.endswith('.content')]
        
    tiddlers = []
    for tiddler_name in tiddler_names:
    
        tiddler = {}
        file_name =  tiddler_name
        
        yaml_file = os.path.join(tiddlers_directory, file_name + '.meta')
        with open(yaml_file, 'r') as f:
            tiddler['meta'] = yaml.load(f, Loader=yaml.FullLoader)
            
        text_file = os.path.join(tiddlers_directory, file_name + '.content')
        with open(text_file, 'r') as f:
           tiddler['text'] = f.read()
           
        tiddlers.append(tiddler)
        
    return tiddlers
    

def save_tiddlers(tiddlers: typing.List, directory_path: str):

    for tiddler in tiddlers:
    
        file_name =  tiddler['title'].replace(' ', '___')
        
        meta = dict(tiddler)
        del meta['text']
        
        yaml_file = os.path.join(directory_path, file_name + '.meta')
        with open(yaml_file, 'w') as f:
            yaml.dump(meta, f, default_flow_style=False)
            
        text_file = os.path.join(directory_path, file_name + '.content')
        with open(text_file, 'w') as f:
            f.write(tiddler['text'])


def load_tw():
    pass

def save_tw():
    pass