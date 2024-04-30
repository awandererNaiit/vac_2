class Vacancy:
    def __init__(self, name, salary_from, salary_to, url, requirement, responsibility, currency):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement
        self.responsibility = responsibility
        self.currency = currency

    def is_salary(self, value):
        if value:
            return value
        return 0

    @staticmethod
    def check_data_str(value):
        """Валидатор для стороковых значений"""
        if value:
            return value
        return 'информация не была найдена'

    def __lt__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from < other.salary_from
        return self.salary_from < other

    def __eq__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from == other.salary_from
        return self.salary_from == other

    def __ne__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from != other.salary_from
        return self.salary_from != other

    def __le__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from <= other.salary_from
        return self.salary_from <= other

    def __ge__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from >= other.salary_from
        return self.salary_from >= other

    def __gt__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from > other.salary_from
        return self.salary_from > other

    def to_dict(self):
        pass

    def get_salary(self):
        if not (self.salary_from or self.salary_to):
            return "Заработная плата: не указана"
        else:
            if not self.salary_from:
                return (f"Заработная плата: до "
                        f"{self.salary_to} {self.currency}")
            if not self.salary_to:
                return (f"Заработная плата: от {self.salary_from} "
                        f"{self.currency}")
            if self.salary_from == self.salary_to:
                return (f"Заработная плата: {self.salary_from} "
                        f"{self.currency}")
            return (f"Заработная плата: от {self.salary_from} до "
                    f"{self.salary_to} {self.currency}")

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @classmethod
    def from_json(cls, data):
        returned_list = []
        for vacancy in data:
            name = vacancy['name']
            if vacancy['salary'] == None:
                salary_from = 0
                salary_to = 0
                currency = ''
            else:
                salary_from = vacancy['salary']['from']
                salary_to = vacancy['salary']['to']
                currency = vacancy['salary']['currency']
            url = vacancy['alternate_url']
            requirement = Vacancy.check_data_str(vacancy['snippet']['requirement'])
            responsibility = Vacancy.check_data_str(vacancy['snippet']['responsibility'])
            vacancy_obj = cls(name, salary_from, salary_to, url, requirement, responsibility, currency)
            returned_list.append(vacancy_obj)

        return returned_list

    def __str__(self):
        return (f"Название вакансии:{self.name}\n"
                f"{self.get_salary()}\n"
                f"Ссылка на вакансию {self.url}\n"
                f"Требования: {self.requirement} \n"
                f"Обязательства: {self.responsibility}\n")
