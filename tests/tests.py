import pytest
import os
import json
from src.parser import HH
from src.Vacancy import Vacancy
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.file import JSONSaver

ROOT = os.path.dirname(__file__)
FILE_PATH = os.path.join(ROOT, 'tests', 'results.json')

@pytest.fixture
def sample_vacancies():
    # Создаем некоторые примеры вакансий для тестирования
    return [
        Vacancy("Software Engineer", 50000, 80000, "https://example.com", "Python, Java", "Develop software", "USD"),
        Vacancy("Data Scientist", 60000, 90000, "https://example.com", "Python, SQL", "Analyze data", "USD"),
        Vacancy("Product Manager", 70000, 100000, "https://example.com", "Agile, Scrum", "Manage product development", "USD"),
    ]

def test_filter_vacancies(sample_vacancies):
    filtered_vacancies = filter_vacancies(sample_vacancies, ["Python"])
    assert len(filtered_vacancies) == 2
    assert filtered_vacancies[0].name == "Software Engineer"
    assert filtered_vacancies[1].name == "Data Scientist"

def test_get_vacancies_by_salary(sample_vacancies):
    ranged_vacancies = get_vacancies_by_salary(sample_vacancies, 65000)
    assert len(ranged_vacancies) == 2
    assert ranged_vacancies[0].name == "Data Scientist"
    assert ranged_vacancies[1].name == "Product Manager"

def test_sort_vacancies(sample_vacancies):
    sorted_vacancies = sort_vacancies(sample_vacancies)
    assert sorted_vacancies[0].name == "Product Manager"
    assert sorted_vacancies[1].name == "Data Scientist"
    assert sorted_vacancies[2].name == "Software Engineer"

def test_get_top_vacancies(sample_vacancies):
    top_vacancies = get_top_vacancies(sample_vacancies, 2)
    assert len(top_vacancies) == 2
    assert top_vacancies[0].name == "Product Manager"
    assert top_vacancies[1].name == "Data Scientist"

def test_json_saver():
    file_path = os.path.join(ROOT, 'test_results.json')
    saver = JSONSaver(file_path)
    test_data = [{"name": "Test Vacancy", "salary_from": 50000, "salary_to": 70000, "url": "https://example.com", "requirement": "Test requirement", "responsibility": "Test responsibility", "currency": "USD"}]
    saver.save_data(test_data)
    assert os.path.exists(file_path)

    with open(file_path, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    assert loaded_data == test_data

    os.remove(file_path)
