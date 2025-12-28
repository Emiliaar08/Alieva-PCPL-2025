from typing import List, Any, Callable
from dataclasses import dataclass
from operator import itemgetter
@dataclass
class Computer:
    """Класс для представления компьютера"""
    id: int
    model: str
    processor: str
    ram_gb: int
@dataclass
class Browser:
    """Класс для представления браузера"""
    id: int
    name: str
    version: str
    memory_usage: int
    computer_id: int
@dataclass
class ComputerBrowser:
    """Класс для реализации отношения многие ко многим"""
    computer_id: int
    browser_id: int

def get_computers() -> List[Computer]:
    """Функция для генерации данных компьютеров"""
    return [
        Computer(1, 'Dell XPS 15', 'Intel i7', 16),
        Computer(2, 'HP Pavilion', 'AMD Ryzen 5', 8),
        Computer(3, 'Lenovo ThinkPad', 'Intel i5', 16),
        Computer(4, 'Apple MacBook Pro', 'M1 Pro', 32),
        Computer(5, 'ASUS ROG', 'Intel i9', 64),
    ]

def get_browsers() -> List[Browser]:
    """Функция для генерации данных браузеров"""
    return [
        Browser(1, 'Chrome', '120.0', 512, 1),
        Browser(2, 'Firefox', '115.0', 256, 2),
        Browser(3, 'Edge', '119.0', 384, 3),
        Browser(4, 'Safari', '17.0', 128, 4),
        Browser(5, 'Opera', '105.0', 192, 5),
        Browser(6, 'Chrome', '121.0', 520, 2),
        Browser(7, 'Firefox', '116.0', 265, 3),
        Browser(8, 'Arc', '1.0', 320, 1),
    ]

def get_computer_browsers() -> List[ComputerBrowser]:
    """Функция для генерации связей многие ко многим"""
    return [
        ComputerBrowser(1, 1),
        ComputerBrowser(1, 8),
        ComputerBrowser(2, 2),
        ComputerBrowser(2, 6),
        ComputerBrowser(3, 3),
        ComputerBrowser(3, 7),
        ComputerBrowser(4, 4),
        ComputerBrowser(5, 5),
        ComputerBrowser(1, 2),
        ComputerBrowser(3, 1),
    ]

def print_data(data: List[Any], headers: List[str], title: str, column_width: int = 20) -> None:
    total_length = len(headers) * column_width
    columns = len(headers)
    
    print(f"{title:=^{total_length}}")
    print(("{:<" + str(column_width) + "}") * columns).format(*headers)
    print()
    
    for row in data:
        if isinstance(row, tuple):
            print(("{:<" + str(column_width) + "}") * columns).format(*row)
        else:
            print(("{:<" + str(column_width) + "}") * columns).format(row)
    print()

def first_query(computers: List[Computer], browsers: List[Browser]) -> List[Any]:
    """Реализация первого запроса: браузеры, начинающиеся на 'A'"""
    result = list()
    for computer in computers:
        for browser in browsers:
            if computer.id == browser.computer_id and browser.name.startswith('A'):
                result.append((browser.name, browser.version, browser.memory_usage, 
                              computer.model, computer.processor))
    
    result.sort(key=itemgetter(0))  # Сортировка по названию браузера
    return result

def second_query(computers: List[Computer], browsers: List[Browser]) -> List[Any]:
    computer_memory: dict[str, list[int]] = {}
    
    for computer in computers:
        for browser in browsers:
            if computer.id == browser.computer_id:
                if computer.model not in computer_memory:
                    computer_memory[computer.model] = []
                computer_memory[computer.model].append(browser.memory_usage)
    
    result = list()
    for computer_model, memories in computer_memory.items():
        min_memory = min(memories)
        result.append((computer_model, min_memory))
    
    result.sort(key=itemgetter(1))  # Сортировка по минимальной памяти
    return result

def third_query(computers: List[Computer], browsers: List[Browser], 
               relations: List[ComputerBrowser], condition: Callable) -> List[Any]:
    result = list()
    
    for relation in relations:
        computer = next((c for c in computers if c.id == relation.computer_id), None)
        browser = next((b for b in browsers if b.id == relation.browser_id), None)
        
        if computer and browser and condition(computer.model):
            result.append((browser.name, browser.version, browser.memory_usage,
                          computer.model, computer.processor))
    
    result.sort(key=itemgetter(0))  # Сортировка по названию браузера
    return result

def main() -> None:
    computers = get_computers()
    browsers = get_browsers()
    computer_browsers = get_computer_browsers()
    
    # Первый запрос
    print_data(
        first_query(computers, browsers),
        ["Браузер", "Версия", "Память (МБ)", "Компьютер", "Процессор"],
        "Запрос 1: Браузеры, начинающиеся на 'A'",
    )
    
    # Второй запрос
    print_data(
        second_query(computers, browsers),
        ["Компьютер", "Мин. память (МБ)"],
        "Запрос 2: Минимальная память браузеров"
    )
    
    # Третий запрос
    print_data(
        third_query(computers, browsers, computer_browsers, 
                   lambda model: "Dell" in model or "Apple" in model),
        ["Браузер", "Версия", "Память", "Компьютер", "Процессор"],
        "Запрос 3: Браузеры на Dell и Apple компьютерах"
    )

if __name__ == "__main__":
    main()
