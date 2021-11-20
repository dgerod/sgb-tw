import os
import sys


def add_package_to_path():
    CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))  
    PACKAGE_DIRECTORY = os.path.dirname(CURRENT_DIRECTORY)  
    sys.path.append(os.path.normpath(PACKAGE_DIRECTORY))
