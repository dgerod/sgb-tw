SGB-TW 
=====================

## What is this?

Simple tool that helps you to write your Software Guidebook using wiki syntax, 
PlantUML, etc. and TiddlyWiki as GUI 

## What is a Software Guide-Book (SGB)?

It is a document describes the software architecture and high-level design of a system. 
In addition to that, the document contains maps, sight and itineraries, history and culture 
and practical information about the software; it describes what the code does not. And it 
is an alive and evolve document. 

## Installation

1. Create a Python virtual environment. 
    * Using *Conda*, for more information see [this](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment).
        ``` bash
        $ conda create --name sgb python=3.7
        ```
    * Using *venv*, for more information see [this](https://docs.python.org/es/3.7/library/venv.html).
        ``` bash
        $ python3 -m sgb /path/to/new/virtual/environment
        ```
              
2. Activate the virtual environment
3. Install *Python* requirements by calling:
    ``` bash
    $ pip install -r requirements.txt
    ```
4. Install [Timini](https://ibnishak.github.io/Timimi) to be able to save the 
TiddlyWiki file from your web-browser.

Steps (1) and (2) are not mandatory but recomended, using virtual environments 
avoid mixing required packages of this application with your Python environment.

## How to use

Activate the virtual environment. For example using conda:
``` bash
$ conda activate sgb
```

Open TiddlyWiki HTML page in your web browse.
    
Start your daily work by opening TiddlyWiki HTML page in your web browse. After 
that synchronize TiddlyWiki with your tiddlers in the DB by executing:
```bash
$ git pull
$ python sgb-cli.py load_tiddlers
```

The sadac-cli command loads tiddlers from DB and add to TiddlyWiki file. Once this 
is done you have to reload the TiddlyWiki page in your web browser..

Once you whant to want to store the tiddlers in the DB, for doing that you have to
execute:
```bash
$ python sgb-cli.py save_tiddlers
$ git push
````

In case that there is a conflict in git, you should do load the tiddlers to the 
TiddlyWiki HTML file after solving it.

