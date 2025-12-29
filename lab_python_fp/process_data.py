import json
import sys
import os

from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1

path = None
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = 'data_light.json'

if not os.path.exists(path):
    print(f"Файл {path} не найден!")
    print("Создаем тестовые данные...")
    test_data = [
        {"job-name": "Программист Python", "location": "Москва", "salary": 150000},
        {"job-name": "Программист Java", "location": "Санкт-Петербург", "salary": 140000},
        {"job-name": "Аналитик данных", "location": "Москва", "salary": 120000},
        {"job-name": "Программист C++", "location": "Новосибирск", "salary": 130000},
        {"job-name": "Дизайнер", "location": "Москва", "salary": 90000},
        {"job-name": "Программист Python", "location": "Казань", "salary": 110000},
        {"job-name": "Менеджер проекта", "location": "Москва", "salary": 160000},
        {"job-name": "программист JavaScript", "location": "Екатеринбург", "salary": 125000},
        {"job-name": "Тестировщик", "location": "Москва", "salary": 80000}
    ]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)
    print(f"Создан тестовый файл {path}")

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    jobs = [item.get('job-name') for item in arg if item.get('job-name') is not None]
    unique_jobs = list(Unique(jobs, ignore_case=True))
    return sorted(unique_jobs, key=lambda x: str(x).lower())

@print_result
def f2(arg):
    return list(filter(lambda x: str(x).lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    salaries = list(gen_random(len(arg), 100000, 200000))
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salaries)]

if __name__ == '__main__':
    if not data:
        print("Нет данных для обработки!")
    else:
        print(f"Обработка данных из файла: {path}")
        print(f"Количество записей: {len(data)}")
        print("-" * 50)
        
        with cm_timer_1():
            result = f4(f3(f2(f1(data))))
        
        print("\n" + "=" * 50)
        print("Обработка завершена!")