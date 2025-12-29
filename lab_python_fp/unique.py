class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            item = next(self.items)
            
            if isinstance(item, str) and self.ignore_case:
                key = item.lower()
            else:
                key = item
            
            if key not in self.seen:
                self.seen.add(key)
                return item

if __name__ == "__main__":
    print("Тест 1 - числа:")
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data1):
        print(item, end=" ")
    print()
    
    print("\nТест 2 - строки без ignore_case:")
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data2):
        print(item, end=" ")
    print()
    
    print("\nТест 3 - строки с ignore_case:")
    for item in Unique(data2, ignore_case=True):
        print(item, end=" ")
    print()
    
    print("\nТест 4 - с генератором случайных чисел:")
    import random
    def test_gen_random(num_count, begin, end):
        for _ in range(num_count):
            yield random.randint(begin, end)
    
    data3 = test_gen_random(10, 1, 3)
    for item in Unique(data3):
        print(item, end=" ")
    print()