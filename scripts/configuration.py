import os
from pathlib import Path
import yaml


class Configuration:

    _ROOT_DIRECTORY = '.sadac-tw'    
    _TEMP_DIRECTORY = _ROOT_DIRECTORY + os.sep + '_tmp_'
    _CONFIGURATION_FILE = _ROOT_DIRECTORY + os.sep + 'settings.yaml'
    
    def __init__(self):
        self._work_directory = self._find_directory()
        self._configuration_file = os.path.join(self._work_directory, Configuration._CONFIGURATION_FILE)
        self._source_directory = self._work_directory
        self._tmp_directory = os.path.join(self._work_directory,
                                           Configuration._TEMP_DIRECTORY)

    def work_directory(self):
        return self._work_directory
    
    def temp_directory(self):
        return self._tmp_directory
    
    def source_directory(self):
        return self._source_directory
    
    def tw_name(self):
            
        if not os.path.exists(self._configuration_file):
            raise NotADirectoryError('Configuration file does not exist')
            
        with open(self._configuration_file, 'r') as stream:
            try:
                data = yaml.safe_load(stream)
                tw_name = data['tw_name']
                #if not os.path.isabs(source_directory):
                #    source_directory = os.path.abspath(os.path.join(self._work_directory, docs['source_directory']))
                    
            except yaml.YAMLError as ex:
                raise
    
        return tw_name

    @staticmethod
    def _find_directory():
        """
        Search directory where SADAC-TW stores all the information (.sadac)
        """
    
        directory = ""
        current_directory = os.getcwd()
        
        found = False
        checking = True
        while checking and not found:            
    
            found = Path(os.path.join(current_directory, Configuration._ROOT_DIRECTORY)).is_dir()
            
            if found:                
                directory = current_directory                                
            else:
                previous_directory = current_directory            
                current_directory = os.path.dirname(current_directory)
                checking = current_directory != previous_directory
                        
        if not found:
            raise NotADirectoryError('Directory not ready to work with SADAC-TW.')
    
        return directory
