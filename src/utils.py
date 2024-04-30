def filter_vacancies(vacancies_list, words):
    filtered_vacancies = []
    for vacancy in vacancies_list:
        for word in words:
            if word in vacancy.responsibility or word in vacancy.requirement:
                filtered_vacancies.append(vacancy)
                break
    return filtered_vacancies


def get_vacancies_by_salary(vacancies_list, min_salary):
    list_by_salary = []
    for vacancy in vacancies_list:
        if vacancy <= min_salary:
            list_by_salary.append(vacancy)
    return list_by_salary

def sort_vacancies(vacancies_list):
    return sorted(vacancies_list, reverse=True)

def get_top_vacancies(vacancies_list, quantity):
    return vacancies_list[:quantity]

def print_vacancies(vacancies_list):
    for vacancy in vacancies_list:
        print(vacancy)