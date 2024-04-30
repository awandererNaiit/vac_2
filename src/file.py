from abc import ABC,abstractmethod

class File(ABC):

    @abstractmethod
    def save_data(self):
        pass

    def get_data(self):
        pass

    def delete_value(self):
        pass

class JSONSaver(File):
    def save_data(self):
        pass

    def get_data(self):
        pass

    def delete_value(self):
        pass