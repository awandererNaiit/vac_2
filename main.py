import os
from src.parser import HH
from src.Vacancy import Vacancy
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.file import JSONSaver

ROOT = os.path.dirname(__file__)
FILE_PATH = os.path.join(ROOT, 'src', 'results.json')


def main():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split(' ')
    min_salary = int(input("Введите минимальную зарплату: "))
    print("\nРезультаты поиска:\n")
    hh = HH()
    vacancies = hh.load_vacancies(search_query)
    vacancies = Vacancy.from_json(vacancies)


    filtered_vacancies = filter_vacancies(vacancies, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, min_salary)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

    result = JSONSaver(FILE_PATH)
    result.save_data(top_vacancies)


if __name__ == "__main__":
    main()
