import json
from abc import ABC,abstractmethod

class File(ABC):

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def delete_value(self):
        pass

class JSONSaver(File):

    def __init__(self,file_path):
        self.file_path = file_path


    def save_data(self, vacancies_list):
        top_list = []
        with open(self.file_path, 'w', encoding='utf-8') as f:
            for vacancy in vacancies_list:
                top_list.append(vacancy.__dict__)
            json.dump(top_list, f, ensure_ascii=False, indent=4)


    def get_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            top_list = json.load(file)
        return top_list


    def delete_value(self):
        pass