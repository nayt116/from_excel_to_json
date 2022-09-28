from dataclasses import dataclass, asdict


@dataclass
class Excel_name_data:
    ex_name: str
    directori_file: str


class Excel_data:
    def __init__(self, ex_name, directori_file):
        self.ex_name = Excel_name_data(ex_name, directori_file)
        self.ex_dict = self.ex_name.__dict__

    def get_value(self, key:str) -> str:
        self.data_ex =  self.ex_dict[key]
        print(self.data_ex)