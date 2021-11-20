# %%

from scripts import add_package_to_path
add_package_to_path()

import argparse
from scripts.commands import add_tiddlers, retrieve_tiddlers


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str, 
                        help="load_tiddlers, save_tiddlers")
    
    command = parser.parse_args().command    
    if (command == 'load_tiddlers'):
        add_tiddlers()
        
    elif (command == 'save_tiddlers'):
        retrieve_tiddlers()
    else:
        print('Unknown command')

if __name__ == "__main__":
    main() 

