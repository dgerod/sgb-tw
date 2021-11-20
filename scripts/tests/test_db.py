import os
import sys


def add_root_package_to_the_path():
    here = os.path.abspath(os.path.dirname(__file__))
    root_package_path = os.path.dirname(here)
    sys.path.append(root_package_path)


add_root_package_to_the_path()

from scripts import db

