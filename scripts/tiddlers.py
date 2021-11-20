# %%

import os
import typing
from string import Template   
import yaml
import json
from bs4 import BeautifulSoup


def extract_tiddlers(tw_file_path: str) -> typing.List:

    html_data = open(tw_file_path, encoding='UTF-8').read()
    
    soup = BeautifulSoup(html_data, features="html.parser")
    element = soup.find('script',class_="tiddlywiki-tiddler-store", type="application/json")
    all_tiddlers = json.loads(element.string) 
    print('All tiddlers:', len(all_tiddlers))

    our_tiddlers = []
    for element in all_tiddlers:
        if "note_type" in element:
            our_tiddlers.append(element)                     
    print('Extracted tiddlers:', len(our_tiddlers))
    
    information_tiddlers = []
    structure_tiddlers = []
    help_tiddlers = []
    
    for element in our_tiddlers:
        
        tiddler = {'title': element['title'],
                   'created': element['created'],
                   'creator': element['creator'],
                   'modified': element['modified'],
                   'modifier': element['modifier'],
                   'note_type': element['note_type'],
                   'tags': element['tags'],
                   'text': element['text']                  
                   }
        
        #print('TIDDLE ---')
        #print('Title:', tiddler['title'])
        #print('Type:', element['note_type'])
        #print('Tags:', tiddler['tags'])
        #print('Created:', tiddler['created'])
        #print('Creator:', tiddler['creator'])
        #print('Modified:', tiddler['modified'])
        #print('Modifier:', tiddler['modifier'])
        #print('Text:', tiddler['text'])
        
        if element['note_type'] == 'information':
            information_tiddlers.append(tiddler)
        elif element['note_type'] == 'structure':
            structure_tiddlers.append(tiddler)
        elif element['note_type'] == 'help':
            help_tiddlers.append(tiddler)
       
    
    print('Information tiddlers:', len(information_tiddlers))
    print('Structure tiddlers:', len(structure_tiddlers))
    print('Help tiddlers:', len(help_tiddlers))    
    return information_tiddlers


def upload_tiddlers(tw_file_path: str, tiddlers: typing.List, output_file_path: str):

    html_data = open(tw_file_path, encoding='UTF-8').read()
    soup = BeautifulSoup(html_data, features="html.parser")
    element = soup.find('script',class_="tiddlywiki-tiddler-store", type="application/json")
    #tiddlers_in_page = json.loads(element.string) 

    new_tiddlers = []
    for tiddler in tiddlers:
        
        {"created":"20211119055559095","creator":"me","text":"","title":"Scope","note_type":"help","tags":"","modified":"20211119060805814","modifier":"me"},
        
        new_tiddler = { 'created': tiddler['meta']['created'],
                        'creator': tiddler['meta']['creator'],
                        'text': tiddler['text'],
                        'title' : tiddler['meta']['title'],
                        'note_type': tiddler['meta']['note_type'],
                        'tags': tiddler['meta']['tags'],
                        'modified': tiddler['meta']['modified'],
                        'modifier': tiddler['meta']['modifier'] }
        
        new_tiddlers.append(new_tiddler)

    print('Uploaded tiddlers:', len(new_tiddlers))
    
    string = ''
    for tiddler in new_tiddlers:
        string = string + json.dumps(tiddler) + ',\n'    
    
    position_char_to_be_removed = -len('\n]')
    element.string = element.string[:position_char_to_be_removed] + ',\n' \
        + string[:position_char_to_be_removed] + '\n]'
        
    with open(output_file_path, "w", encoding='UTF-8') as f:
        f.write(str(soup))
