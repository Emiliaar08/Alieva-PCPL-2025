# test_main.py
import pytest
from pytest_unordered import unordered

from main import (
    Computer, Browser, ComputerBrowser,
    first_query, second_query, third_query
)

@pytest.fixture
def test_one_to_many_data():
    """Фикстура для тестов один-ко-многим"""
    computers = [
        Computer(1, 'Dell XPS 15', 'Intel i7', 16),
        Computer(2, 'HP Pavilion', 'AMD Ryzen 5', 8),
        Computer(3, 'Lenovo ThinkPad', 'Intel i5', 16),
    ]
    
    browsers = [
        Browser(1, 'Arc', '1.0', 320, 1),
        Browser(2, 'Chrome', '120.0', 512, 1),
        Browser(3, 'Firefox', '115.0', 256, 2),
        Browser(4, 'Alphabet', '1.0', 128, 3),
        Browser(5, 'Opera', '105.0', 192, 2),
    ]
    
    return computers, browsers

@pytest.fixture
def test_many_to_many_data():
    """Фикстура для тестов многие-ко-многим"""
    computers = [
        Computer(1, 'Dell XPS 15', 'Intel i7', 16),
        Computer(2, 'HP Pavilion', 'AMD Ryzen 5', 8),
        Computer(3, 'Apple MacBook', 'M1', 16),
        Computer(4, 'ASUS ROG', 'Intel i9', 32),
    ]
    
    browsers = [
        Browser(1, 'Chrome', '120.0', 512, 0),
        Browser(2, 'Firefox', '115.0', 256, 0),
        Browser(3, 'Safari', '17.0', 128, 0),
        Browser(4, 'Edge', '119.0', 384, 0),
        Browser(5, 'Opera', '105.0', 192, 0),
    ]
    
    relations = [
        ComputerBrowser(1, 1),  # Dell - Chrome
        ComputerBrowser(1, 2),  # Dell - Firefox
        ComputerBrowser(2, 2),  # HP - Firefox
        ComputerBrowser(2, 4),  # HP - Edge
        ComputerBrowser(3, 3),  # Apple - Safari
        ComputerBrowser(3, 1),  # Apple - Chrome
        ComputerBrowser(4, 5),  # ASUS - Opera
        ComputerBrowser(4, 4),  # ASUS - Edge
    ]
    
    return computers, browsers, relations

def test_first_query(test_one_to_many_data):
    """Тест первого запроса: браузеры, начинающиеся на 'A'"""
    computers, browsers = test_one_to_many_data
    
    expected = [
        ('Alphabet', '1.0', 128, 'Lenovo ThinkPad', 'Intel i5'),
        ('Arc', '1.0', 320, 'Dell XPS 15', 'Intel i7'),
    ]
    
    result = first_query(computers, browsers)
    
    assert len(result) == 2
    assert result == expected
    assert result[0][0] == 'Alphabet'  # Проверка сортировки по алфавиту
    assert result[1][0] == 'Arc'

def test_second_query(test_one_to_many_data):
    computers, browsers = test_one_to_many_data
    
    expected = [
        ('Lenovo ThinkPad', 128),
        ('Dell XPS 15', 320),
        ('HP Pavilion', 256),
    ]
    
    result = second_query(computers, browsers)
    
    assert len(result) == 3
    assert result == expected
    assert result[0][1] == 128  # Наименьшая минимальная память
    assert result[2][1] == 320  # Наибольшая минимальная память

def test_third_query(test_many_to_many_data):
    """Тест третьего запроса: связь многие ко многим с условием"""
    computers, browsers, relations = test_many_to_many_data
    
    # Ожидаемый результат для компьютеров Dell и Apple
    expected = unordered([
        ('Chrome', '120.0', 512, 'Apple MacBook', 'M1'),
        ('Chrome', '120.0', 512, 'Dell XPS 15', 'Intel i7'),
        ('Firefox', '115.0', 256, 'Dell XPS 15', 'Intel i7'),
        ('Safari', '17.0', 128, 'Apple MacBook', 'M1'),
    ])
    
    result = third_query(computers, browsers, relations, 
                        lambda model: "Dell" in model or "Apple" in model)
    
    assert len(result) == 4
    
    for item in result:
        assert "Dell" in item[3] or "Apple" in item[3]
    
    browser_names = [item[0] for item in result]
    sorted_browser_names = sorted(browser_names)
    assert browser_names == sorted_browser_names

def test_first_query_empty_result():
    """Тест первого запроса: когда нет браузеров на 'A'"""
    computers = [Computer(1, 'Test', 'CPU', 8)]
    browsers = [Browser(1, 'Chrome', '1.0', 100, 1)]
    
    result = first_query(computers, browsers)
    
    assert len(result) == 0
    assert result == []

def test_second_query_single_computer():
    """Тест второго запроса: один компьютер с несколькими браузерами"""
    computers = [Computer(1, 'Test PC', 'CPU', 8)]
    browsers = [
        Browser(1, 'Browser1', '1.0', 100, 1),
        Browser(2, 'Browser2', '1.0', 200, 1),
        Browser(3, 'Browser3', '1.0', 50, 1),
    ]
    
    result = second_query(computers, browsers)
    
    assert len(result) == 1
    assert result[0] == ('Test PC', 50)
