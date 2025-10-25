import os
from pathlib import path
class fileSaver:
    def __init__(self, base_dir:str=".")
        self.base_path =base_dir
        self.create_dir_exists(self.base_path)

    def create_dir_exists(self,):
        if not os.pathesixts(slef.base_path):
            os.makedir(self.base_path)
            print(f"Base directory '{self.base_path}' created.")
        else:
            print(f"Base directory '{self.base_path}' already exists.")

    def save_file(self,dir_name:str,file_name:str,content:):
        target_dir = self.base_path

