import os

class Create_dir:
    def __init__(self, dir:str):
        self.dir = dir

    def create_dir(self):
        os.mkdir(self.dir)